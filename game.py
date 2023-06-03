# Warsztat: Gra w zgadywanie liczb.
# Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
# 
# Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
# Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", 
# po czym wrócić do pkt. 1
# Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "Too small!", 
# po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest większa niż wylosowana, 
# wyświetlić komunikat "Too big!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", 
# po czym zakończyć działanie programu.

import random

# generate a random int
number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number: "))

        if guess == number:
            print("You win!")
            break
        elif guess < number:
            print("Too small!")
        elif guess > number: 
            print("Too big!")

    except ValueError:
        print("It's not a number! Try again.")







