import os
import sys
import subprocess
import platform
from pathlib import Path

def create_project_with_venv(project_path, venv_name='venv'):
    project_dir = Path(project_path).expanduser().resolve()
    if not project_dir.exists():
        project_dir.mkdir(parents=True)
        print(f"Création du dossier projet : {project_dir}")
    else:
        print(f"Le dossier projet existe déjà : {project_dir}")

    venv_path = project_dir / venv_name

    if venv_path.exists():
        print(f"L'environnement virtuel {venv_name} existe déjà dans le projet.")
    else:
        print(f"Création de l'environnement virtuel '{venv_name}' ...")
        subprocess.check_call([sys.executable, '-m', 'venv', str(venv_path)])
        print(f"Environnement virtuel créé dans : {venv_path}")

    os_name = platform.system()
    if os_name == 'Windows':
        activate_command = f"{venv_name}\\Scripts\\activate"
        print("\nPour activer votre environnement virtuel sous Windows PowerShell, tapez :")
        print(activate_command)
    else:
        activate_command = f"source {venv_name}/bin/activate"
        print("\nPour activer votre environnement virtuel sous Mac/Linux, tapez :")
        print(activate_command)

    print("\nUne fois activé, installez Flask avec :")
    print("pip install Flask")

    print("\nPour désactiver l'environnement virtuel, tapez :")
    print("deactivate")

if __name__ == '__main__':
    create_project_with_venv('./flask_project')
