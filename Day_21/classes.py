# Exercice Jour21
# Exercice Niveau 1

from collections import Counter
import math


class Statistics:
    def __init__(self, data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return self.data[0]

    def max(self):
        return self.data[-1]

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]

    def mode(self):
        frequency = Counter(self.data)
        max_count = max(frequency.values())
        mode_values = [k for k, v in frequency.items() if v == max_count]
        if len(mode_values) == 1:
            return (mode_values[0], max_count)
        else:
            return [(val, max_count) for val in mode_values]

    def variance(self):
        mean = self.mean()
        var = sum((x - mean) ** 2 for x in self.data) / self.count()
        return var

    def std(self):
        return math.sqrt(self.variance())

    def freq_dist(self):
        frequency = Counter(self.data)
        total_count = self.count()
        return sorted(
            [
                (round((count / total_count) * 100, 1), value)
                for value, count in frequency.items()
            ],
            reverse=True,
        )

    def percentile(self, p):
        """Calcul du percentile p (0-100)"""
        if not 0 <= p <= 100:
            raise ValueError("Percentile doit être entre 0 et 100")
        n = self.count()
        k = (n - 1) * p / 100
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return self.data[int(k)]
        d0 = self.data[f] * (c - k)
        d1 = self.data[c] * (k - f)
        return d0 + d1

    def describe(self):
        description = f"""Count: {self.count()}
Sum: {self.sum()}
Min: {self.min()}
Max: {self.max()}
Range: {self.range()}
Mean: {round(self.mean())}
Median: {self.median()}
Mode: {self.mode()}
Variance: {round(self.variance(), 1)}
Standard Deviation: {round(self.std(), 1)}
Frequency Distribution: {self.freq_dist()}
"""
        return description


ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]

data = Statistics(ages)
print(data.describe())


# Exercice Niveau 2 class PersonAccount:


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        # Incomes et expenses sont des sets de tuples (description, montant)
        self.incomes = set()
        self.expenses = set()

    def total_income(self):
        return sum(amount for desc, amount in self.incomes)

    def total_expense(self):
        return sum(amount for desc, amount in self.expenses)

    def account_info(self):
        incomes_str = ", ".join([f"{desc}: {amount}" for desc, amount in self.incomes])
        expenses_str = ", ".join(
            [f"{desc}: {amount}" for desc, amount in self.expenses]
        )
        return (
            f"Nom: {self.firstname} {self.lastname}\n"
            f"Revenus: {incomes_str}\n"
            f"Dépenses: {expenses_str}"
        )

    def add_income(self, description, amount):
        if amount > 0:
            self.incomes.add((description, amount))
        else:
            raise ValueError("Le montant du revenu doit être positif.")

    def add_expense(self, description, amount):
        if amount > 0:
            self.expenses.add((description, amount))
        else:
            raise ValueError("Le montant de la dépense doit être positif.")

    def account_balance(self):
        return self.total_income() - self.total_expense()


# Exemple d'utilisation
person = PersonAccount("Moukitat", "LASSISI")
person.add_income("Salaire", 2500)
person.add_income("Dividendes", 200)
person.add_expense("Loyer", 900)
person.add_expense("Courses", 300)

print(person.account_info())
print("Solde du compte:", person.account_balance())
