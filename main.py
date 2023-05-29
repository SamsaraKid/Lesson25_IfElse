# num = int(input('Number\n'))
# if num > 0:
#     print('positive')
# else:
#     print('negative')
#
# if num > 0:
#     print('ok')
#     if num > 10:
#         print('ok10')
#         if num > 20:
#             print('ok20')
# else:
#     print('notok')
#
# print('===================')
#
# if num > 0:
#     print('ok')
# elif num == 0:
#     print('ok10')
# elif num < 0:
#     print('ok20')
# else:
#     print('notok')

# =====================================================================

# age = int(input('Сколько лет коту?\n'))
#
# if 1 >= age >= 0:
#     print('Котик')
# elif 5 >= age > 1:
#     print('Кот')
# elif age > 5:
#     print('Котище')
# else:
#     print('Ваш кот непонятный')

# =====================================================================

# slovo = input('слово\n')

# if 'a' in slovo:
#     print('a in')
# if 'c' in slovo:
#     print('c in')
# if 't' in slovo:
#     print('t in')

# if 'a' in slovo:
#     print('a in')
# elif 'c' in slovo:
#     print('c in')
# elif 't' in slovo:
#     print('t in')

# if 'a' in slovo:
#     print('a in')
#     if 'c' in slovo:
#         print('c in')
#         if 't' in slovo:
#             print('t in')


# =====================================================================

# ask1 = int(input('Сколько будет 2 + 2?\n'))
# n = 0
#
#
# if ask1 == 4:
#     n += 1
#     print('Верно. Следующий вопрос\n')
#     ask2 = int(input('Квадратный корень из 121?\n'))
#     if ask2 == 11:
#         n += 1
#         print('Верно. Последний вопрос\n')
#         ask3 = input('Самое глубокое озеро в мире?\n')
#         if ask3 == 'Байкал':
#             n += 1
#             print('Вы умница')
#
# print('Вы набрали %d баллов' % n)


# =====================================================================


# n1 = '2'
# n2 = '2'
# print(n1+n2)
# print('hello'*10)
#
# name = 'Barsik'
# print('hello', name, sep='###', end='\t')
# print('hello', name, sep='***', end='end')

# =====================================================================

# def f1():
#     print('hello')
#     pass
#
# def f2(n='cow',x=11):
#     print('hello', n, x)
#     pass
#
# f1()
# f2('cat')
# f2()

# =====================================================================



# def f3():
#     n = 1
#     while True:
#         x = input('Куда хотите: b - банк, c - цирк, p - поликлиника, e - для завершения работы\n')
#         if x == 'b':
#             talon = 'Б' + str(n)
#             print('Ваш талон', talon)
#             n += 1
#         elif x == 'c':
#             talon = 'Ц' + str(n)
#             print('Ваш талон', talon)
#             n += 1
#         elif x == 'p':
#             talon = 'П' + str(n)
#             print('Ваш талон', talon)
#             n += 1
#         elif x == 'e':
#             break
#         else:
#             print('Таких мест нет')
#
# f3()

nomer = 1

def talon(bukva):
    print('ваш номер', bukva, nomer)
    pass

while True:
    otvet = input('Куда хотите: 1 - банк, 2 - цирк, 3 - поликлиника\n')
    if otvet == '1':
        talon('Б')
        nomer += 1
    elif otvet == '2':
        talon('Ц')
        nomer += 1
    elif otvet == '3':
        talon('П')
        nomer += 1
    elif otvet == 'q':
        break
