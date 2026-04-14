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
#Индивидуальный вариант 5 поменяла вариант 3
# from sympy import *
# k, T, C, L = symbols ('k C T L')
# #1 способ
# C_ost=30000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(7):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 30000, T:7, L:0})
#   Am_lst.append (round (Am.subs({C: 30000, T:7, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print ('Am_lst:', Am_lst)
# print ('Am_lst:', C_ost_lst)
# #2 способ
# Aj=0
# C_ost=30000
# Am_lst_2= []
# C_ost_lst_2=[]
# for i in range(7):
#    Am = k * 1/T * (C-Aj)
#    C_ost -= Am.subs({C: 30000, T:7, k:2})
#    Am_lst_2.append (round (Am.subs({C: 30000, T:7, k:2}), 2))
#    Aj += Am
#    C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #Табличный вывод 
# import pandas  as pd
# Y = range(1,8)
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
# plt.savefig ('chart19.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2 ['C_ost_lst_2'], label = 'Am_2')
# plt.savefig ('chart20.png')
# vals = Am_lst
# labels = [str(x) for x in range(1,8)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie (vals, labels=labels, autopct='%1.1f%%', shadow=True,
#          explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
#          rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart21.png')
# vals = Am_lst_2
# labels = [str(x) for x in range(1,8)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
#         explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
#         rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart22.png')
# plt.figure()
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig ('chart23.jpeg')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig ('chart24.png')
#2 Задание проверил Батулин, все отлично. 
# 3 Задание удаление контейнера визуализации результатов
#удалила контейнер визуализации результатов индивидуального задания прошлой лабораторной работы, написала рандомные слова, воостановила контейнер с помощью "History" с 60 точки сохранения до 49
# 4 задание делала с Кобозевым 
#180, 191 и 208 строки. Проверила, все верно, 5 баллов
# 5 задание делала сама
#в реплике создала скрипт оболочки prikhodko.sh. Через приложение Shell я разрешила запуск файла с помощью команды chmod +x и после этого я запустила файл prikhodko.sh 
# 6 задание делала сама 
# 7 задание
# #Вариант 4
# from sympy import *
# k, T, C, L = symbols ('k C T L')
# #1 способ
# C_ost=40000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(10):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 40000, T:10, L:0})
#   Am_lst.append (round (Am.subs({C: 40000, T:6, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print ('Am_lst:', Am_lst)
# print ('Am_lst:', C_ost_lst)
# #2 способ
# Aj=0
# C_ost=20000
# Am_lst_2= []
# C_ost_lst_2=[]
# for i in range(10):  
#    Am = k * 1/T * (C-Aj)
#    C_ost -= Am.subs({C: 20000, T:6, k:2})
#    Am_lst_2.append (round (Am.subs({C: 20000, T:10, k:2}), 2))
#    Aj += Am
#    C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #Табличный вывод 
# import pandas  as pd
# Y = range(1,11)  
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
# labels = [str(x) for x in range(1,11)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 
# fig, ax = plt.subplots()
# ax.pie (vals, labels=labels, autopct='%1.1f%%', shadow=True,
#          explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
#          rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart15.png')
# vals = Am_lst_2
# labels = [str(x) for x in range(1,11)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
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


#Вариант индивидуальный реализация модуля верификации маркера аутентификации (контроль подлинности маркера) для защиты от угрозы подмены субъекта сетевого доступа

from sympy import symbols
import os
import time
import hashlib
import hmac
import base64
import json
import pandas as  pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'DejaVu Sans'

#Время жизни маркера 10 минут (по умолчанию в DDS OAuth 2.0)
TOKEN_TTL = 600

# Секретный ключ для HMAC-подписи маркеров (компонент интеграции)
TOKEN_SECRET_KEY = os.environ.get("TOKEN_SECRET_KEY", "")

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
     # Если ключ задан — HMAC-SHA256, иначе простой SHA-256
    if TOKEN_SECRET_KEY:
        signature = hmac.new(TOKEN_SECRET_KEY.encode(), payload_b64.encode(), hashlib.sha256).hexdigest()
    else:
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

    #Уровень 2: проверка целостности маркера (подпись HMAC-SHA256 или SHA-256)
    if TOKEN_SECRET_KEY:
        expected_signature = hmac.new(TOKEN_SECRET_KEY.encode(), payload_b64.encode(), hashlib.sha256).hexdigest()
    else:
        expected_signature = hashlib.sha256(payload_b64.encode()).hexdigest()
    if not hmac.compare_digest(expected_signature, received_signature):
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

def level_label(reason):
    if reason == "Верифицирован":
        return "Все пройдены"
    elif reason in ("Маркер просрочен", "Время выпуска в будущем"):
        return "Уровень 3 (срок)"
    elif reason == "Подпись недействительна":
        return "Уровень 2 (подпись)"
    else:
        return "Уровень 1 (структура)"

N = list(range(1, 7))
desc_lst    = [s["desc"] for s in scenarios]
level_lst   = [level_label(r) for r in result_lst]

df = pd.DataFrame(
    list(zip(N, desc_lst, remaining_lst, pct_lst, level_lst, result_lst, access_lst)),
    columns=["N", "Сценарий", "Осталось (сек.)", "Действителен (%)",
             "Уровень блокировки", "Результат верификации", "Доступ"]
)

print("\n" + "=" * 80)
print("  КОНТЕЙНЕР ВЕРИФИКАЦИИ МАРКЕРОВ АУТЕНТИФИКАЦИИ — РЕЗУЛЬТАТЫ")
print("=" * 80)
print(df.to_string(index=False))

# Сводная таблица по уровням
summary_data = {
    "Уровень 1 — Структура маркера":      level_lst.count("Уровень 1 (структура)"),
    "Уровень 2 — Подпись SHA-256":        level_lst.count("Уровень 2 (подпись)"),
    "Уровень 3 — Срок действия":          level_lst.count("Уровень 3 (срок)"),
    "Верифицировано (все уровни пройдены)": level_lst.count("Все пройдены"),
}
df_summary = pd.DataFrame(
    list(summary_data.items()),
    columns=["Уровень проверки", "Кол-во маркеров"]
)
print("\n" + "-" * 50)
print("  СВОДКА ПО УРОВНЯМ КОНТЕЙНЕРА")
print("-" * 50)
print(df_summary.to_string(index=False))
print("=" * 80)

#КОНТЕЙНЕР ВИЗУАЛИЗАЦИИ РЕЗУЛЬТАТОВ
import numpy as np

short_labels = [
    "1: Свежий",
    "2: 1/3 срока",
    "3: 2/3 срока",
    "4: Просрочен",
    "5: Подд. подпись",
    "6: Подм. содержимого",
]

# Определяем на каком уровне остановился каждый маркер
def failed_at_level(reason):
    if reason == "Верифицирован":
        return None
    elif reason in ("Маркер просрочен", "Время выпуска в будущем"):
        return 3
    elif reason == "Подпись недействительна":
        return 2
    else:
        return 1

fail_levels = [failed_at_level(r) for r in result_lst]

# График 1: Оставшийся срок действия всех маркеров
fig, ax = plt.subplots(figsize=(10, 5))
bar_colors = ["#2ecc71" if d == "ДА" else "#e74c3c" for d in access_lst]
bars = ax.bar(short_labels, remaining_lst, color=bar_colors, edgecolor="black", linewidth=0.7)

for bar, pct, res in zip(bars, pct_lst, result_lst):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 8,
            f"{pct}%\n{res}", ha="center", va="bottom", fontsize=8.5,
            color="black")

ax.axhline(y=TOKEN_TTL, color="gray", linestyle="--", linewidth=1, label=f"TTL = {TOKEN_TTL} сек.")
ax.set_ylim(0, TOKEN_TTL + 180)
ax.set_ylabel("Осталось (сек.)")
ax.set_title("График 1. Срок действия маркеров по сценариям\n(зелёный — доступ разрешён, красный — заблокирован)")
ax.legend()
ax.grid(axis="y", alpha=0.4)
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig("chart25.png")
plt.close()

# График 2: Матрица прохождения уровней проверки
level_names = ["Уровень 1\nСтруктура", "Уровень 2\nПодпись SHA-256", "Уровень 3\nСрок действия"]
n_scenarios = len(scenarios)
n_levels = 3

# cell_state: 1 = пройден (зелёный), 0 = заблокирован (красный), -1 = не достигнут (серый)
cell_state = []
for fl in fail_levels:
    row = []
    for lvl in range(1, n_levels + 1):
        if fl is None:
            row.append(1)          # прошёл все уровни
        elif lvl < fl:
            row.append(1)          # пройден до уровня блокировки
        elif lvl == fl:
            row.append(0)          # заблокирован здесь
        else:
            row.append(-1)         # не достигнут
    cell_state.append(row)

color_map = {1: "#2ecc71", 0: "#e74c3c", -1: "#bdc3c7"}
label_map  = {1: "Пройден", 0: "Заблокирован", -1: "Не достигнут"}

fig, ax = plt.subplots(figsize=(9, 5))
for row_i, row in enumerate(cell_state):
    for col_i, state in enumerate(row):
        ax.add_patch(plt.Rectangle((col_i, row_i), 1, 1,
                                   color=color_map[state], ec="white", lw=2))
        ax.text(col_i + 0.5, row_i + 0.5, label_map[state],
                ha="center", va="center", fontsize=9, fontweight="bold", color="black")

ax.set_xlim(0, n_levels)
ax.set_ylim(0, n_scenarios)
ax.set_xticks([0.5, 1.5, 2.5])
ax.set_xticklabels(level_names, fontsize=10)
ax.set_yticks([i + 0.5 for i in range(n_scenarios)])
ax.set_yticklabels(short_labels, fontsize=9)
ax.set_title("График 2. Прохождение уровней верификации контейнера\n(по каждому сценарию)")
ax.tick_params(length=0)
plt.tight_layout()
plt.savefig("chart26.png")
plt.close()

# График 3: Количество маркеров, заблокированных на каждом уровне / прошедших
blocked_l1 = sum(1 for fl in fail_levels if fl == 1)
blocked_l2 = sum(1 for fl in fail_levels if fl == 2)
blocked_l3 = sum(1 for fl in fail_levels if fl == 3)
passed_all  = sum(1 for fl in fail_levels if fl is None)

categories = [
    "Заблокировано\nна уровне 1\n(структура)",
    "Заблокировано\nна уровне 2\n(подпись)",
    "Заблокировано\nна уровне 3\n(срок действия)",
    "Верифицировано\n(все уровни пройдены)",
]
counts = [blocked_l1, blocked_l2, blocked_l3, passed_all]
bar_colors3 = ["#e74c3c", "#e74c3c", "#e74c3c", "#2ecc71"]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(categories, counts, color=bar_colors3, edgecolor="black", linewidth=0.7, width=0.5)

for bar, cnt in zip(bars, counts):
    if cnt > 0:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                str(cnt), ha="center", va="bottom", fontsize=13, fontweight="bold")

ax.set_ylim(0, max(counts) + 1)
ax.set_ylabel("Количество маркеров")
ax.set_title("График 3. Итог работы контейнера верификации\n(на каком уровне и сколько маркеров заблокировано)")
ax.grid(axis="y", alpha=0.4)
plt.tight_layout()
plt.savefig("chart27.png")
plt.close()

