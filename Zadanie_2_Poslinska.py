from operator import attrgetter

class Movie:
    def __init__(self, title, year, rate, length):
        self.title = title if isinstance(title, str) else ""
        self.year = year if isinstance(year, int) else 0
        self.rate = rate if isinstance(rate, float) else 0.0
        self.length = length if isinstance(length, int) else 1

    def get_film_duration(self):
        return self.length

    def __lt__(self, other):
        # wprowadza sortowanie po ocenie wewnątrz funkcji
        return self.rate < other.rate

    def __repr__(self):
        return f"\nTytuł: {self.title}, Rok produkcji: {self.year}, Ocena IMDB: {self.rate}, Długość: {self.length}"


movies = [
    Movie("God Father", 1972, 9.2, 175),
    Movie("Shawshank Redemption", 1994, 9.3, 142),
    Movie("God Father Part Two", 1974, 9.0, 202),
    Movie("Inception", 2010, 8.8, 148),
    Movie("Fight Club", 1999, 8.8, 139),
    Movie("The Lord of the Rings: Fellowship of the Ring", 2001, 8.9, 178),
    Movie("The Matrix", 1999, 8.7, 136),
    Movie("The Seven", 1995, 8.6, 127),
    Movie("The Lord of the Rings: Return of the King", 2003, 9.0, 201),
    Movie("The Lord of the Rings: The Two Towers", 2002, 8.8, 179)
]

# Print klasy movies bez sortowania
print(f"Print bez sortowania {movies}")

# 1. Sortowanie po tytule, alfabetycznie i roku produkcji - od starszego
movies.sort(key=attrgetter('title', 'year'))
print(f"\n1. Sortowanie po tytule, alfabetycznie: {movies}")

# 2. Dzięki wbudowanej funkcji umożliwia sortowanie po ocenach, od najniżej ocenianego filmu
# Funkcja sort() nadaje sortowanie bezpośrednio na obiekt
movies.sort()
print(f"\n2. Sortowanie po ocenie filmu - wbudowana funkcja least: {movies}")

# 3. Sortowania po latach produkcji od najstarszego filmu
# Funkcja sorted() tworzy nową listę posortowanego obiektu
print(f"\n3. Sortowanie po latach produkcji: {sorted(movies, key=attrgetter('year'), reverse=False)}")

# 4. Sortowanie po ocenie IMDB i tytule, od najniższej oceny. Niektóre filmy posiadają tą samą ocenę,
# więc jako drugi parametr jest użyty title, czyli tytuł - alfabetycznie
print(f"\n4. Sortowanie po ocenie i alfabetycznie: {sorted(movies, key=lambda x: (x.rate, x.title), reverse=False)}")

# 5. Sortowania po długości tytułu filmu, od najkrótszego
movies.sort(key=lambda x: x.get_film_duration())
print(f"\n5. Sortowanie po długości filmu: {movies}")