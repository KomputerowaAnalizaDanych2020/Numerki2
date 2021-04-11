# Menu główne
print("Rozwiazywanie ukladu N rownan liniowych z N niewiadomymi za pomoca metody iteracyjnej Jacobiego")
# Podanie funkcji jako odczyt z pliku
fileName = input("Nazwa pliku, z ktorego zostanie pobrana macierz (nalezy pamietac o rozszerzeniu pliku):")
# Sprawdzamy, czy plik istnieje
try:
    file = open(fileName)
    # Operacja na pliku - odczyt macierzy
except IOError:
    print("Plik nie istnieje.")
    fileName = input("Prosze podac prawidlowa nazwe pliku: ")
finally:
    file.close()

print("Wybierz kryterium zatrzymania:")
print("1. Spelnienie warunku nalozonego na dokladnosc")
print("2. Osiagniecie zadanej liczby iteracji")
stopChoice = input()
if stopChoice == 1:
    epsilon = input("Podaj epsilon: ")
if stopChoice == 2:
    counter = input("Podaj liczbe iteracji: ")

