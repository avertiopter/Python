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

n = int(input())
def prost_chisl(chis):
    for i in range (2, chis):
        if chis // i == 1:
            print (chis)
            break
        elif chis % i == 0:
            break
for i in range (2, n):
    prost_chisl(i)
