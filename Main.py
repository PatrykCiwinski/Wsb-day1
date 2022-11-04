import random
zgadywanki=[]
losowa_liczba=random.randint(1,100)
game_is_on=True
life=6
while game_is_on:
    user = int(input('podaj liczbę od 0 do 100: '))
    if user==losowa_liczba:
        print('Wygrałeś')
        game_is_on=False


