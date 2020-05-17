import re
from collections import Counter

with open('text.txt') as f:
    tx = f.readlines()
    #print(tx)
    safari = 'Safari'
    data1 = '17/May'
    data2 = '18/May'
    data3 = '19/May'
    data4 = '20/May'

    count = 0
    for line in tx:
        if safari in line:
            if data1 in line:
                count +=1
    print('Количество запросов слеланных 17 мая через Safari:', count)
    count = 0
    firefox =  'Firefox'
    for line in tx:
        if firefox in line:
            if data1 in line:
                count +=1
    print('Количество запросов слеланных 17 мая через Firefox:', count)

    count = 0
    for line in tx:
        if safari in line:
            if data2 in line:
                count +=1
    print('Количество запросов слеланных 18 мая через Safari:', count)

    count = 0
    for line in tx:
        if firefox in line:
            if data2 in line:
                count +=1
    print('Количество запросов слеланных 18 мая через Firefox:', count)

    count = 0
    for line in tx:
        if safari in line:
            if data3 in line:
                count +=1
    print('Количество запросов слеланных 19 мая через Safari:', count)

    count = 0
    for line in tx:
        if firefox in line:
            if data3 in line:
                count +=1
    print('Количество запросов слеланных 19 мая через Firefox:', count)

    count = 0
    for line in tx:
        if safari in line:
            if data4 in line:
                count +=1
    print('Количество запросов слеланных 20 мая через Safari:', count)

    count = 0
    for line in tx:
        if firefox in line:
            if data4 in line:
                count +=1
    print('Количество запросов слеланных 20 мая через Firefox:', count)

#Количество ip адреслв всего и уникальных на 17 мая
with open('text.txt') as f:
    ip_data17 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[17'
    log = f.read()
    ip_list17 = re.findall(ip_data17, log)
#print(ip_list17) 
count_ip17 = len(ip_list17) #Подсчет всех ip адресов
print('Количество всех ip адресов на 17 мая составляет:', count_ip17)
unic_iplist17 = set(ip_list17) # Подсчет уникальных ip адресов
print('Количество уникальных ip адресов на 17 мая составляет:', len(unic_iplist17))

#Количество ip адреслв всего и уникальных на 18 мая
with open('text.txt') as f:
    ip_data18 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[18'
    log = f.read()
    ip_list18 = re.findall(ip_data18, log)
#print(ip_list18) 
count_ip18 = len(ip_list18) #Подсчет всех ip адресов
print('Количество всех ip адресов на 18 мая составляет:', count_ip18)
unic_iplist18 = set(ip_list18) # Подсчет уникальных ip адресов
print('Количество уникальных ip адресов на 18 мая составляет:', len(unic_iplist18))

#Количество ip адреслв всего и уникальных на 19 мая
with open('text.txt') as f:
    ip_data19 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[19'
    log = f.read()
    ip_list19 = re.findall(ip_data19, log)
#print(ip_list19) 
count_ip19 = len(ip_list19) #Подсчет всех ip адресов
print('Количество всех ip адресов на 19 мая составляет:', count_ip19)
unic_iplist19 = set(ip_list19) # Подсчет уникальных ip адресов
print('Количество уникальных ip адресов на 19 мая составляет:', len(unic_iplist19))

#Количество ip адреслв всего и уникальных на 20 мая
with open('text.txt') as f:
    ip_data20 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[20'
    log = f.read()
    ip_list20 = re.findall(ip_data20, log)
#print(ip_list20) 
count_ip20 = len(ip_list20) #Подсчет всех ip адресов
print('Количество всех ip адресов на 20 мая составляет:', count_ip20)
unic_iplist20 = set(ip_list20) # Подсчет уникальных ip адресов
print('Количество уникальных ip адресов на 20 мая составляет:', len(unic_iplist20))