pada = False
licznik_nie = 0

while not pada:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem) ").lower()
    
    if odpowiedz == "tak":
        print("Liczba odpowiedzi 'nie':", licznik_nie)
        break
    elif odpowiedz == "nie":
        licznik_nie += 1
    elif odpowiedz == "nie wiem":
        print("wpisz t lub n")
    else:
        print("Nie rozumiem tej odpowiedzi, spróbuj jeszcze raz.")
