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
