import random

while True:
    pada = random.choice([True, False])
    odpowiedz = input("Czy pada deszcz? (tak/nie): ").lower()
    
    if (odpowiedz == "tak" and pada) or (odpowiedz == "nie" and not pada):
        print("Brawo! Zgadłeś!")
        break
    else:
        print("Nie zgadłeś, spróbuj ponownie!")
