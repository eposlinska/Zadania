from datetime import date


class Car:
    """Klasa opisująca samochody wraz z aktualkizacją przebiegu oraz kalkulacją ceny"""

    def __init__(self, make, model, year, mileage, price):
        self.make = make if isinstance(make, str) else ""
        self.model = model if isinstance(model, str) else ""
        self.year = year if isinstance(year, int) else 2024
        self.mileage = mileage if isinstance(mileage, int) else 0
        self.price = price if isinstance(price, int) and mileage > 0 else 0

    def drive(self):
        est_mileage = 0
        for y in range(date.today().year - self.year):
            est_mileage += 10000
        if est_mileage > self.mileage:
            return f"Podany przebieg jest o {est_mileage - self.mileage} km niższy niż planowany. Dobry egzemplarz!"
        else:
            return f"Przebieg wynosi {self.mileage}. To {self.mileage - est_mileage} km za dużo! Rozważ inny samochód."

    def calculate_depreciation(self):
        # Nie udało mi się znaleźć odpowiedniego rozwiązania. Jedyny pomysł jaki przyszedł mi do głowy, to próba stworzenia słownika
        # z cenami podstawowymi (z salonu, na rok 2024) i na podstawie tej ceny wyjściowej obliczenie narzuconego %. W poniższym
        # przypadku, zastosowano obliczenie wieku samochodu, kalkulację procentu narastającego w zależności od wieku, oraz założono,
        # że na każde 10k km przebiegu doliczany będzie % spadku wartości.
        age = 2024 - self.year
        pct_year = 100 * (1 - 0.05) ** age
        pct_mileage = self.mileage / 10000
        depreciation = (pct_year + pct_mileage)
        return f"Spadek wartości {self.model} wynosi : {round(100 - depreciation)}%"

    def __str__(self):
        return f"Marka: {self.make},  model: {self.model}, rok produkcji: {self.year},  przebieg: {self.mileage},  cena: {self.price} zł |"

    def __repr__(self):
        return f"Car(make: {self.make} | model: {self.model} | year: {self.year} | mileage: {self.mileage} | price: {self.price})"


# Testowanie klasy
cars = [
    Car("Subaru", "Forester", 2023, 5000, 150000),
    Car("Ford", "Mondeo", 2015, 46000, 75000),
    Car("Volkswagen", "Polo", 2005, 195000, 7000),
    Car("Honda", "Civic", 2020, 30000, 99000),
    Car("Ford", "Kuga", 2014, 35000, 55000),
]

for car in cars:
    # Przedstawia informacje o samochodzie
    print(car.__str__())
    # Przedstawia techniczną stronę obiektu
    print(car.__repr__())
    # Szacuje przebieg
    print(car.drive())
    # Drukuje funkcję obliczającą spadek wartości dla przykładu z listy
    print(car.calculate_depreciation())