# #Общее задание часть 1
# from sympy import *
# k, T, C, L = symbols ('k C T L')

# #1 способ
# C_ost=100000 
# Am_lst=[]
# C_ost_lst=[]
# for i in range(5):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 100000, T:5, L:0})
#   Am_lst.append (round (Am.subs({C: 100000, T:5, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print ('Am_lst:', Am_lst)
# print ('Am_lst:', C_ost_lst)
# #2 способ
# Aj=0
# C_ost=100000
# Am_lst_2= []
# C_ost_lst_2=[]
# for i in range(5):
#   Am = k * 1/T * (C-Aj)
#   C_ost -= Am.subs({C: 100000, T:5, k:2})
#   Am_lst_2.append (round (Am.subs({C: 100000, T:5, k:2}), 2))
#   Aj += Am 
#   C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas  as pd
# Y = range(1,6)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd. DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd. DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #Контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame ['C_ost_lst'], label = 'Am')
# plt.savefig ('chart1.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2 ['C_ost_lst_2'], label = 'Am_2')
# plt.savefig ('chart2.png')

# vals = Am_lst
# labels = [str(x) for x in range(1,6)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie (vals, labels=labels, autopct='%1.1f%%', shadow=True,
# explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
# rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart3.png')

# vals = Am_lst_2
# labels = [str(x) for x in range(1,6)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
# explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
# rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart4.png')
# plt.figure()

# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig ('chart5.jpeg')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig ('chart6.png')
# plt.figure()

# #Общее задание часть 2
# from sympy import *
# k, T, C, L = symbols ('k C T L')

# # #1 способ
# C_ost=30000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(8):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 30000, T:8, L:0})
#   Am_lst.append (round (Am.subs({C: 30000, T:8, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print ('Am_lst:', Am_lst)
# print ('Am_lst:', C_ost_lst)
# #2 способ
# Aj=0
# C_ost=30000
# Am_lst_2= []
# C_ost_lst_2=[]
# for i in range(8):
#   Am = k * 1/T * (C-Aj)
#   C_ost -= Am.subs({C: 30000, T:8, k:2})
#   Am_lst_2.append (round (Am.subs({C: 30000, T:8, k:2}), 2))
#   Aj += Am 
#   C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas  as pd
# Y = range(1,9)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd. DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd. DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #Контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame ['C_ost_lst'], label = 'Am')
# plt.savefig ('chart7.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2 ['C_ost_lst_2'], label = 'Am_2')
# plt.savefig ('chart8.png')

# vals = Am_lst
# labels = [str(x) for x in range(1,9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie (vals, labels=labels, autopct='%1.1f%%', shadow=True,
# explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
# rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart9.png')

# vals = Am_lst_2
# labels = [str(x) for x in range(1,9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
# explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
# rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart10.png')
# plt.figure()

# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig ('chart11.jpeg')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig ('chart12.png')
# plt.figure()

# #Индивидуальный вариант 5
# from sympy import *
# k, T, C, L = symbols ('k C T L')
# #1 способ
# C_ost=20000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(6):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 20000, T:6, L:0})
#   Am_lst.append (round (Am.subs({C: 20000, T:6, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print ('Am_lst:', Am_lst)
# print ('Am_lst:', C_ost_lst)
# #2 способ
# Aj=0
# C_ost=20000
# Am_lst_2= []
# C_ost_lst_2=[]
# for i in range(6):  ##Что это означает? Ответ: это цикл, который повторяется 6 раз. Все верно 5 баллов
#    Am = k * 1/T * (C-Aj)
#    C_ost -= Am.subs({C: 20000, T:6, k:2})
#    Am_lst_2.append (round (Am.subs({C: 20000, T:6, k:2}), 2))
#    Aj += Am
#    C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #Табличный вывод 
# import pandas  as pd
# Y = range(1,7)  ##Что это означает Ответ: создаёт последовательность чисел от 1 до 6 включительно, которая будет использоваться как номера годов для таблицы и графиков. - Все верно, 5 баллов
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd. DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd. DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)
# #Визуализация
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame ['C_ost_lst'], label = 'Am')
# plt.savefig ('chart13.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2 ['C_ost_lst_2'], label = 'Am_2')
# plt.savefig ('chart14.png')
# vals = Am_lst
# labels = [str(x) for x in range(1,7)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1) ##Что это означает? Ответ: та строка делает так, что все сектора круговой диаграммы будут выдвинуты от центра на 10% радиуса круга (для визуального разделения). - Все верно, 5 баллов
# fig, ax = plt.subplots()
# ax.pie (vals, labels=labels, autopct='%1.1f%%', shadow=True,
#          explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
#          rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart15.png')
# vals = Am_lst_2
# labels = [str(x) for x in range(1,7)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
#         explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
#         rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart16.png')
# plt.figure()
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig ('chart17.jpeg')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig ('chart18.png')

#Лабораторная работа 3, общее задание
#1 Задание делала с Мамедовой
# import os
# prihodko1=os.environ['prihodko1']
# print(prihodko1)

# import os
# prihodko2=os.environ['prihodko2']
# print(prihodko2)

# import os
# prihodko3=os.environ['prihodko3']
# print(prihodko3)
# Все вывелось корректно

#2 задание делала с Батулиным 
#Индивидуальный вариант 5
""" from sympy import *
k, T, C, L = symbols ('k C T L')
#1 способ
C_ost=30000
Am_lst=[]
C_ost_lst=[]
for i in range(7):
  Am = (C-L)/T
  C_ost -= Am.subs({C: 30000, T:7, L:0})
  Am_lst.append (round (Am.subs({C: 30000, T:7, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print ('Am_lst:', Am_lst)
print ('Am_lst:', C_ost_lst)
#2 способ
Aj=0
C_ost=30000
Am_lst_2= []
C_ost_lst_2=[]
for i in range(7):
   Am = k * 1/T * (C-Aj)
   C_ost -= Am.subs({C: 30000, T:7, k:2})
   Am_lst_2.append (round (Am.subs({C: 30000, T:7, k:2}), 2))
   Aj += Am
   C_ost_lst_2.append(round(C_ost, 2))
print ('Am_lst_2:', Am_lst_2)
print ('C_ost_lst_2:', C_ost_lst_2)

#Табличный вывод 
import pandas  as pd
Y = range(1,8)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd. DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd. DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)
#Визуализация
import numpy as np
import matplotlib.pyplot as plt
plt.plot(tfame['Y'], tfame ['C_ost_lst'], label = 'Am')
plt.savefig ('chart19.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2 ['C_ost_lst_2'], label = 'Am_2')
plt.savefig ('chart20.png')
vals = Am_lst
labels = [str(x) for x in range(1,8)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie (vals, labels=labels, autopct='%1.1f%%', shadow=True,
         explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
         rotatelabels=True)
ax.axis("equal")
plt.savefig ('chart21.png')
vals = Am_lst_2
labels = [str(x) for x in range(1,8)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
        explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
        rotatelabels=True)
ax.axis("equal")
plt.savefig ('chart22.png')
plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig ('chart23.jpeg')
plt.figure()
plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.savefig ('chart24.png')"""
#2 Задание проверил Батулин, все отлично. 
# 3 Задание удаление контейнера визуализации результатов
#удалила контейнер визуализации результатов индивидуального задания прошлой лабораторной работы, написала рандомные слова, воостановила контейнер с помощью "History" с 60 точки сохранения до 49
# 4 задание делала с Кобозевым 
#180, 191 и 208 строки. Проверила, все верно, 5 баллов
# 5 задание делала сама
#в реплике создала скрипт оболочки prikhodko.sh. Через приложение Shell я разрешила запуск файла с помощью команды chmod +x и после этого я запустила файл prikhodko.sh 
# 6 задание делала сама 
