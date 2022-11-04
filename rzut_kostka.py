import random
suma=0
ilosc_rzutów=100000
for i in range(ilosc_rzutów):
    for j in range(3):
        wynik = random.randrange(1, 7)
        if wynik ==6:
            suma+=1
            break
print(suma/ilosc_rzutów*100, '%')



