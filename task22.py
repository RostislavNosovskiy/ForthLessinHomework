# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
firstlist =[]
secondlist =[]
firstlistlen = int(input('Введите длину первого набора чисел:'))
for i in range (firstlistlen):
    firstlist.append(randint(0,100))
secondlistlen = int(input('Введите длину второго набора чисел:'))
for i in range (secondlistlen):
    secondlist.append(randint(0,100)) 
print(firstlist)
print(secondlist)  
ounlist = []
for i in range (firstlistlen):
    for j  in range (secondlistlen):
        if firstlist[i] == secondlist [j]:
            ounlist.append(firstlist[i])
Ounlist = set(ounlist)
Ounlist = list(Ounlist)
for i in range (len(Ounlist)-1):
    for j in range (len(Ounlist)-i-1):
        if Ounlist[j] > Ounlist[j+1]:
            Ounlist[j], Ounlist[j+1] = Ounlist[j+1],Ounlist[j]
print(Ounlist)            
        

        
        