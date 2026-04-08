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
# 7 задание


#Вариант индивидуальный реализация модуля верификации маркера аутентификации (контроль подлинности маркера) для защиты от угрозы подмены субъекта сетевого доступа

from sympy import symbols
import time
import hashlib
import base64
import json
import pandas as  pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'DejaVu Sans'

#Время жизни маркера 10 минут (по умолчанию в DDS OAuth 2.0)
TOKEN_TTL = 600

#КОНТЕЙНЕР РАСЧЁТА
#Формулы для метрик маркера аутентификации

t, TTL_sym, t0 = symbols('t TTL_sym t0')
#Формула оставшегося времени действия маркера 
validity_remaining = TTL_sym -  (t - t0)

#Формула процента оставшегося срока действия 
validity_pct = validity_remaining / TTL_sym * 100

def generate_token(user_id, role, offset=0):
    now = int(time.time()) + offset
    payload = {
        "user_id": user_id,
        "role": role,
        "iat": now,
        "exp": now + TOKEN_TTL
    }
    payload_json = json.dumps(payload, separators=("," ,":")).encode()
    payload_b64 = base64.urlsafe_b64encode(payload_json).decode().rstrip("=")
    signature =  hashlib.sha256(payload_b64.encode()).hexdigest()
    return  f"{payload_b64}.{signature}", now


def verify_token(token):
    result = {"valid": False, "reason":"", "payload": None}


    #Уровеень 1: проверка структуры маркера
    parts = token.split(".")
    if len(parts) != 2:
        result["reason"] = "Неверная структура маркера"
        return result

    payload_b64, received_signature = parts[0], parts[1]

    #Уровень 2: проверка целостности маркера (подпись SHA-256)
    expected_signature = hashlib.sha256(payload_b64.encode()).hexdigest()
    if expected_signature != received_signature:
        result["reason"] = "Подпись недействительна"
        return  result

    #Декодирование полезной нагрузки
    padding = 4 - len(payload_b64) % 4
    if padding  != 4:
        payload_b64 += "=" * padding
    try:
       payload = json.loads(base64.urlsafe_b64decode(payload_b64).decode())
    except  Exception:
       result["reason"] = "Ошибка декодирования"
       return result

    #Уровень 3: проверка срока действия маркера
    current_time = int(time.time())
    if current_time >  payload["exp"]:
        result["reason"] = "Маркер просрочен"
        return result
    if current_time  < payload["iat"]:
        result["reason"] = "Время выпуска в будущем"
        return result

    result["valid"] = True
    result["reason"] = "Верифицирован"
    result["payload"] = payload
    return  result

#6 сценариев проверки 
scenarios = [
    {"desc": "Легитимный (свежий)",    "offset": 0,    "tamper": False},
    {"desc": "Легитимный (1/3 срока)", "offset": -200, "tamper": False},
    {"desc": "Легитимный (2/3 срока)", "offset": -400, "tamper": False},
    {"desc": "Просроченный",           "offset": -700, "tamper": False},
    {"desc": "Подделанная подпись",    "offset": 0,    "tamper": "sign"},
    {"desc": "Подмена содержимого",    "offset": 0,    "tamper": "payload"},
]

current_time = int(time.time())
remaining_lst = []
pct_lst = []
result_lst = []
access_lst = []

for i, s in enumerate(scenarios):
    token, iat = generate_token(f"user_{i+1}", "analyst", offset=s["offset"])
    exp = iat + TOKEN_TTL

    #Применение атаки в случае необходимости
    if  s["tamper"] == "sign":
        token = token[:-4] + "XXXX"
    elif s["tamper"] == "payload":
        forged = base64.urlsafe_b64encode(
            json.dumps({"user_id": f"user_{i+1}", "role": "admin",
                        "iat": iat, "exp": exp}, 
                       separators=(",", ":")).encode()
        ).decode().rstrip("=")
        token = forged + "." + token.split(".")[1]

    #Символьный расчёт по формулам
    rem = float(validity_remaining.subs({TTL_sym: TOKEN_TTL, t: current_time,
t0: iat}))
    rem = max(0.0, rem)
    pct = float(validity_pct.subs({TTL_sym: TOKEN_TTL, t: current_time, t0:
iat}))
    pct = max(0.0, min(100.0, pct))

    res  = verify_token(token)

    remaining_lst.append(round(rem,1))
    pct_lst.append(round(pct,1))
    result_lst.append(res["reason"])
    access_lst.append("ДА" if res["valid"] else "НЕТ")

print("remaining_lst:", remaining_lst)
print("pct_lst:", pct_lst)
print("result_lst:", result_lst)
print("access_lst:", access_lst)

#КОНТЕЙНЕР ТАБЛИЧНОГО ВЫВОДА

N = list(range(1,7))
desc_lst = [s["desc"] for s in scenarios]
table = list(zip(N, desc_lst, remaining_lst, pct_lst, result_lst, access_lst))
df =  pd.DataFrame(
      table, 
      columns=["N", "Сценарий", "Осталось (сек.)", "Действителен (%)",
"Результат", "Доступ"]
)
print("\n" + "=" * 70)
print("Проверка маркеров аутентификации")
print("=" * 70)
print(df.to_string(index=False))

#КОНТЕЙНЕР ВИЗУАЛИЗАЦИИ РЕЗУЛЬТАТОВ
#график 1 Легитимный пользователь - убывание срока действия (сценарии 1-4)
df_user = df[df["N"] <= 4]
plt.figure()
plt.plot(df_user["N"], df_user["Осталось (сек.)"], marker='o', color='steelblue')
plt.xlabel("№ маркера")
plt.ylabel("Осталось (сек.)")
plt.title("Срок действия маркера (легитимный пользователь)")
plt.xticks(df_user["N"])
plt.grid(True)
plt.savefig("chart25.png")


#график 2. Злоумышленник - атакованные маркеры (сценарии 5-6)
df_attack = df[df["N"] >= 5]
plt.figure()
plt.bar(df_attack["Сценарий"], df_attack["Осталось (сек.)"], color = 'red')
plt.xlabel("Сценарий атаки")
plt.ylabel("Осталось (сек.)")
plt.title("Маркеры злоумышленника - заблокированы")
plt.savefig ("chart26.png")


#график 3 круговая диаграмма - доля разрешенных и запрещенных доступов
outcomes =  df["Доступ"].value_counts()
labels_pie = ["доступ разрешен" if x== "ДА" else "доступ запрещен"
              for x in outcomes.index]
explode = [0.05] * len(outcomes)
fig, ax = plt.subplots()
ax.pie(outcomes.values, labels=labels_pie, autopct='%1.1f%%', shadow=True,
       explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
       rotatelabels=False)
ax.axis("equal")
plt.title("Распределение результатов верификации")
plt.savefig("chart27.png")


#график 4 Столбчатая диаграмма - процент оставшегося срока по всем сценариям
plt.figure()
colors = ["green" if d == "ДА" else "red" for d in df["Доступ"]]
plt.bar(df["N"], df["Действителен (%)"], color=colors)
plt.xlabel("№ Маркера")
plt.ylabel("Действителен (%)")
plt.title("Процент оставшегося срока действия маркера")
plt.xticks(N)
plt.savefig  ("chart28.png")

