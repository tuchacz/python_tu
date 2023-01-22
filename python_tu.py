print("Mam na imię Tomek i program do wyświetlania liczb podzielnych przez 3, 5, 7")  # tutaj wpisz swoje imię

#program Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
#określonego przez użytkownika.

a=int(input("Podaj dolny zakres: "))
z=int(input("Podaj górny zakres: "))

for i in range(a,z+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i)
