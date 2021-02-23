from random import randint
from dice_class import *

def get_poz_s(p):
    if p == "1":
        poz = 0
        s = 1
    elif p == "2":
        poz = 1
        s = 2
    elif p == "3":
        poz = 2
        s = 3
    elif p == "4":
        poz = 3
        s = 4
    elif p == "5":
        poz = 4
        s = 5
    elif p == "6":
        poz = 5
        s = 6
    else:
        p = p.upper()
        if p == "A":
            poz = 6
            s = 12
        elif p == "B":
            poz = 7
            s = 24
        elif p == "C":
            poz = 8
            s = 15
        elif p == "D":
            poz = 9
            s = 20
        elif p == "E":
            poz = 10
            s = 18
        elif p == "F":
            poz = 11
            s = 28
        elif p == "G":
            poz = 12
            s = 24
        elif p == "H":
            poz = 13
            s = 30
        elif p == "I":
            poz = 14
            s = 30
    return poz, s


z = []


print("----------")
print("START")
print("----------")

number_of_players = 2
number_of_rounds = 3
number_of_queue = 15

dice = Dice()
sc = Score(number_of_players)
sc.print(sc.score, 1)


print(' ')
print('S T R U K T U R A   G R Y')

_queue = 0
while _queue != number_of_queue:

    print("")
    print("Kolejka = ", _queue + 1)

    _player = 0
    while _player != number_of_players:

        print("")
        print("   --- Zawodnik = ", _player + 1)
        print("")

        _round = 0
        while _round != number_of_rounds:
            # k = randint(1, 100)
            # z.append(k)
            print("       --- runda = ", _round + 1)

            if _round == 0:
                random = dice.many_dice_roll()
                random.sort()

            print('---------')
            print("Wylosowane liczby:", random)

            index = dice.numbers_counter_list(random)
            print('---------')
            print("Wystąpienia liczb:", index)
            print('---------')
            # wyświetlenie tabeli
            dice.score_report(random)

            print('---------')
            s = str(input('Czy chcesz coś zmienić? [T/N]'))
            print('---------')

            if s == 'n' or s == 'N':
                break
            else:
                print('---------')
                change = int(input('Liczba pozycji do zmiany: '))
                print('---------')

                selected_list = []

                while change != 0:
                    index_change = int(input('Pozycja do ponownego losowania [1..5]? '))
                    selected_list.append(index_change - 1)
                    change -= 1
                    print('licznik', change)

                print('---------')
                print('Pozycje do zmiany (licząc od zera): ', selected_list)
                print('---------')

                random = dice.selected_dice_roll(random, selected_list)
                random.sort()

                print('---------')
                print('Wylosowane liczby (posortowane): ', random)
                print('---------')

            poz = 0         
            _round += 1

        w = str(input('Czy zapisać dane [T/N]? '))
        w.upper()
        if w == 'T':
            print('---------')
            p = str(input('Podaj pozycja w tabeli do zapisu: '))
            print('---------')
            poz, s = get_poz_s(p)

            print("pozycja", poz, s)
            # wskazać pozycję do zapisania
            sc.score[_player][poz] = dice.position_to_score(p, random)
        sc.print(sc.score, 1)
        z = []

        _player += 1

    _queue += 1

print(" ")
sc.print(sc.score, 1)
print(" ")

print("----------")
print("KONIEC")
print("----------")