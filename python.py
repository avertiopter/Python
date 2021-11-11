n = int(input())
 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b)

#hex

n = int(input())
 
s = ''
h = '0123456789ABCDEF'
 
while n > 0:
    s = h[n % 16] + s
    n = n // 16
 
print(s)


#Простые числа:
#дано натуральное число, вычислить простое ли оно или составное


 import math
n = int(input())

 
if n < 2:
    print("Число должно быть больше 1")
    quit()
elif n == 2:
    print("Это простое число")
    quit()
 
i = 2 
 
limit = int(math.sqrt(n))
 
while i <= limit:
    if n % i == 0:
        print("Это сложное число")
        quit() 
    i += 1 
 
print("Это простое число")

#вывести все простые числа от 2 до n

from math import sqrt
n = int(input())
for x in range(2, n + 1):
    if all(x % i != 0 for i in range(2, int(sqrt(x)) + 1)):
        print(x, end=" ")

#Списки.
#Дан список чисел, найти:
#сумму всех элементов (реализовать встроенную функцию sum)
a = [1,2,3,4]
b = [2,4,5,6]
c = a+b
summa = (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7])
print (summa)

#максимальный элемент (реализовать встроенную функцию max)

a = [1,2,3,4]
b = [2,4,5,6]
c = a+b
maxi = c[0]
for i in range(1, len(c)):
    if c[i] > maxi:
        maxi = c[i]
print(maxi)

#среднее арифметическое
a = [1,2,3,4]
b = [2,4,5,6]
c = a+b
suma = (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7])
print (suma /len (c))


#медианное значение (указание: предварительно упорядочить c помощью mylist.sort())

#количество нулей (реализовать функцию count, которая повторяет функционал соответствующего метода для списков)

#Дан список слов, найти:
#самое длинное слово
word = ["Кошка", "Ложка","Ножка","Сапог","Радостный"]
max(word,key = len)


#Дано 2 упорядоченных списка. Объединить их 
#в один упорядоченный список. Указание: встроенная функция sort ухудшает алгоритмическую сложность и ее использовать в данной задаче нельзя.
#[1, 5, 9], [2, 5, 13] -> [1, 2, 5, 5, 13]

a = [1, 5, 9]
b = [2, 5, 13]
c = []

N = len(a)
M = len(b)

i = 0
j = 0
while i < N and j < M:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

c += a[i:] + b[j:]
print(c)

#Реализовать функцию zip: из пары списков сделать список пар:
#zip([1, 2, 3], ['a', 'b', 'c']) -> [(1, 'a'), (2, 'b'), (3, 'c')]

a = ['a', 'b','c','d']
b = [1,2,3,4]
c = {}
for i in range(len(a)):
   c[a[i]] = b[i]
   print(c)

#Строки.
#Дана строка латинских букв.
#посчитать количество слов в ней
s='addsp'
len (s)

#превратить в заголовок ('the best' -> 'The Best') (реализовать встроенный метод title)
fin_stroka = 'the best'
f_S = fin_stroka.split()
result_list = []
for x in f_S :
    for y in list(x):
        result_list.append(y)
        
result_list[0] = "T"
result_list[3] = "B"
print(" ".join (result_list))

#заменить все гласные на звездочки (hello -> h*ll*)
s='hello'
s1=s.replace('o','*',1)
s2=s1.replace('e','*',1)
print (s2)
#выбросить из нее все слова короче 4 букв
words = ['cat', 'hot-dog', 'information', 'sad', 'exchange']
result_words = [x for x in words if len(x) > 4]
print(result_words)
#Словари.
#Дано 2 списка: ключи и значения. Создать из них словарь.
Dict1 = [1,2,3,4,5]
Dict2 = ['a','b','c','d','e']
Dict12 = dict(zip(Dict1,Dict2))
print(Dict12)

#Дана строка, представляющая число в двоичной, десятичной или шестадцатиричной системе счисления. Написать функцию, которая переводит эту строку в целое число. Т.е. реализовать часть функциональности встроенной функции int. Указание: воспользоваться функцией ord.

def myint(s, base=10):
    n = 0
    for c in s:
        n *= base
        d = digit(c)
        n += d
        return n

def digit(c):
    return ord(c) - ord('0')
