from fastapi import FastAPI, HTTPException, Depends, status, Query, Path
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Field, SQLModel, create_engine, Session, select, or_
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from datetime import datetime, timedelta
import uvicorn
import jwt  

# Config 
JWT_SECRET = "CHANGE_ME_SECRET"  # à mettre en .env
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# FastAPI 
app = FastAPI(title="API Patrimoine Africain", version="0.1")

#  Database setup
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

#  Enums 
class Role(str, Enum):
    visitor = "visitor"
    contributor = "contributor"
    admin = "admin"

class Category(str, Enum):
    place = "place"
    museum = "museum"
    structure = "structure"
    animal = "animal"
    monument = "monument"
    bridge = "bridge"
    skyscraper = "skyscraper"
    pyramid = "pyramid"
    site = "site"

class Status(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    archived = "archived"

#  Models 
class UserBase(SQLModel):
    email: str = Field(index=True)
    role: Role = Role.visitor

class User(UserBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(SQLModel):
    email: str
    password: str  
    role: Optional[Role] = Role.contributor

class UserRead(UserBase):
    id: UUID

def fake_hash_password(password: str) -> str:
    return "fakehashed" + password

# Main Item model 
class ItemBase(SQLModel):
    name: str = Field(min_length=3)
    title: Optional[str] = None
    category: Category
    country: str = Field(min_length=2, max_length=2, description="ISO Alpha-2 code")
    city: Optional[str] = None
    year: Optional[int] = None
    event_date: Optional[datetime] = None
    era: Optional[str] = None
    description: str = Field(min_length=200)
    abstract: str = Field(min_length=280, max_length=600)
    tags: List[str] = []
    image_url: Optional[str] = None
    image_credit: Optional[str] = None
    official_url: Optional[str] = None
    references: List[str] = []
    status: Status = Status.pending
    submitted_by: Optional[str] = None
    reviewed_by: Optional[UUID] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: Optional[datetime] = None

class Item(ItemBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    slug: str = Field(index=True, unique=True)

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: UUID
    slug: str
    status: Status

class ItemUpdate(SQLModel):
    name: Optional[str]
    title: Optional[str]
    category: Optional[Category]
    country: Optional[str]
    city: Optional[str]
    year: Optional[int]
    event_date: Optional[datetime]
    era: Optional[str]
    description: Optional[str]
    abstract: Optional[str]
    tags: Optional[List[str]]
    image_url: Optional[str]
    image_credit: Optional[str]
    official_url: Optional[str]
    references: Optional[List[str]]
    status: Optional[Status]

#  OAuth2 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm="HS256")
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    payload = decode_access_token(token)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    with Session(engine) as session:
        user = session.get(User, UUID(user_id))
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

def require_role(min_role: Role):
    def role_checker(user: User = Depends(get_current_user)):
        roles_hierarchy = [Role.visitor, Role.contributor, Role.admin]
        if roles_hierarchy.index(user.role) < roles_hierarchy.index(min_role):
            raise HTTPException(status_code=403, detail="Insufficient privileges")
        return user
    return role_checker

#  Utils 
def generate_slug(name: str, existing_slugs: List[str]) -> str:
    slug_base = name.lower().replace(" ", "-")
    slug = slug_base
    suffix = 1
    while slug in existing_slugs:
        slug = f"{slug_base}-{suffix}"
        suffix += 1
    return slug

#  Startup to create tables 
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

#  Auth routes 
@app.post("/auth/register", response_model=UserRead)
def register(user_in: UserCreate):
    with Session(engine) as session:
        existing = session.exec(select(User).where(User.email == user_in.email)).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")
        user = User(
            email=user_in.email,
            password_hash=fake_hash_password(user_in.password),
            role=user_in.role or Role.contributor,
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

@app.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.email == form_data.username)).first()
        if not user or user.password_hash != fake_hash_password(form_data.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": str(user.id), "role": user.role})
        return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=UserRead)
def me(user: User = Depends(get_current_user)):
    return user

#  Public endpoints $
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items", response_model=List[ItemRead])
def list_items(
    q: Optional[str] = Query(None, description="Recherche full-text"),
    category: Optional[Category] = None,
    country: Optional[str] = None,
    city: Optional[str] = None,
    tags: Optional[List[str]] = Query(None),
    page: int = 1,
    page_size: int = 20
):
    with Session(engine) as session:
        query = select(Item).where(Item.status == Status.approved, Item.deleted_at == None)

        if q:
            q_like = f"%{q.lower()}%"
            query = query.where(or_(
                Item.name.ilike(q_like),
                (Item.title != None) & (Item.title.ilike(q_like)),
                Item.abstract.ilike(q_like)
            ))
        if category:
            query = query.where(Item.category == category)
        if country:
            query = query.where(Item.country == country)
        if city:
            query = query.where(Item.city == city)
        if tags:
            for tag in tags:
                query = query.where(Item.tags.contains([tag]))
        total = session.exec(query).count()
        items = session.exec(query.offset((page-1)*page_size).limit(page_size)).all()
        return items

@app.get("/items/{item_id_or_slug}", response_model=ItemRead)
def get_item(item_id_or_slug: str = Path(...)):
    with Session(engine) as session:
        item = None
        try:
            uid = UUID(item_id_or_slug)
            item = session.get(Item, uid)
        except ValueError:
            item = session.exec(select(Item).where(Item.slug == item_id_or_slug)).first()
        if not item or item.status != Status.approved or item.deleted_at is not None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

# Contributor routes 
@app.post("/submissions", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_submission(item_in: ItemCreate, current_user: User = Depends(require_role(Role.contributor))):
    with Session(engine) as session:
        dup = session.exec(select(Item).where(
            Item.name == item_in.name,
            Item.city == item_in.city,
            Item.country == item_in.country,
            Item.deleted_at == None
        )).first()
        if dup:
            raise HTTPException(status_code=400, detail="Duplicate item exists")
        slugs = [i.slug for i in session.exec(select(Item)).all()]
        slug = generate_slug(item_in.name, slugs)
        item = Item(**item_in.dict())
        item.slug = slug
        item.status = Status.pending
        item.submitted_by = current_user.email
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.get("/submissions/mine", response_model=List[ItemRead])
def list_my_submissions(current_user: User = Depends(require_role(Role.contributor))):
    with Session(engine) as session:
        items = session.exec(select(Item).where(Item.submitted_by == current_user.email)).all()
        return items

@app.patch("/submissions/{item_id}", response_model=ItemRead)
def update_submission(item_id: UUID, item_update: ItemUpdate, current_user: User = Depends(require_role(Role.contributor))):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item or item.submitted_by != current_user.email:
            raise HTTPException(status_code=404, detail="Submission not found")
        if item.status != Status.pending:
            raise HTTPException(status_code=400, detail="Can only update pending submissions")
        for key, val in item_update.dict(exclude_unset=True).items():
            setattr(item, key, val)
        item.updated_at = datetime.utcnow()
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

#  Admin routes 
@app.get("/admin/submissions", response_model=List[ItemRead])
def list_pending_submissions(
    status: Status = Query(Status.pending),
    current_user: User = Depends(require_role(Role.admin))
):
    with Session(engine) as session:
        items = session.exec(select(Item).where(Item.status == status)).all()
        return items

@app.post("/admin/submissions/{item_id}/approve", response_model=ItemRead)
def approve_submission(item_id: UUID, current_user: User = Depends(require_role(Role.admin))):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item or item.status != Status.pending:
            raise HTTPException(status_code=404, detail="Submission not found or not pending")
        item.status = Status.approved
        item.reviewed_by = current_user.id
        item.updated_at = datetime.utcnow()
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.post("/admin/submissions/{item_id}/reject")
def reject_submission(item_id: UUID, reason: str = Query(..., description="Reason for rejection"), current_user: User = Depends(require_role(Role.admin))):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item or item.status != Status.pending:
            raise HTTPException(status_code=404, detail="Submission not found or not pending")
        item.status = Status.rejected
        item.reviewed_by = current_user.id
        item.updated_at = datetime.utcnow()
        session.add(item)
        session.commit()
        return {"detail": f"Submission rejected: {reason}"}

@app.patch("/admin/items/{item_id}", response_model=ItemRead)
def update_item(item_id: UUID, item_update: ItemUpdate, current_user: User = Depends(require_role(Role.admin))):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item or item.status != Status.approved:
            raise HTTPException(status_code=404, detail="Item not found or not approved")
        for key, val in item_update.dict(exclude_unset=True).items():
            setattr(item, key, val)
        item.updated_at = datetime.utcnow()
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.delete("/admin/items/{item_id}")
def soft_delete_item(item_id: UUID, current_user: User = Depends(require_role(Role.admin))):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item or item.deleted_at is not None:
            raise HTTPException(status_code=404, detail="Item not found or already deleted")
        item.deleted_at = datetime.utcnow()
        session.add(item)
        session.commit()
        return {"detail": "Item soft deleted"}

@app.post("/admin/items/{item_id}/restore")
def restore_item(item_id: UUID, current_user: User = Depends(require_role(Role.admin))):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item or item.deleted_at is None:
            raise HTTPException(status_code=404, detail="Item not found or not deleted")
        item.deleted_at = None
        session.add(item)
        session.commit()
        return {"detail": "Item restored"}

#  Run 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
