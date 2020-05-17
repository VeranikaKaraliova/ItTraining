import re
from collections import Counter

# Подсчет строк
with open('apache_logs.txt') as fp:
    file_text = fp.readline()
    a = len(file_text)
    print('1.Файл состоит из', a, 'строк.')

# Вычленение ip адресов
regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
with open('apache_logs.txt') as f:
    log = f.read()
    ip_list = re.findall(regexp, log)
#print(ip_list) 

# Подсчет всех ip адресов
count_ip = len(ip_list)
print('2.Количество всех ip адресов составляет:', count_ip)

# Подсчет уникальных ip адресов
unic_iplist = set(ip_list)
#print(unic_iplist)
print('3.Количество уникальных ip адресов составляет:', len(unic_iplist))

#Сколько safari
safari = re.findall(r'Safari', log)
print('4.Количество запросов, выполненных через safari:', len(safari))

#Сколько firefox
firefox = re.findall(r'Firefox', log)
print('5.Количество запросов, выполненных через firefox:', len(firefox))

#Количество ip адреслв всего и уникальных на 17 мая
with open('apache_logs.txt') as f:
    ip_data17 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[17'
    log = f.read()
    ip_list17 = re.findall(ip_data17, log)
#print(ip_list17) 
count_ip17 = len(ip_list17) #Подсчет всех ip адресов
print('6.Количество всех ip адресов на 17 мая составляет:', count_ip17)
unic_iplist17 = set(ip_list17) # Подсчет уникальных ip адресов
print('7.Количество уникальных ip адресов на 17 мая составляет:', len(unic_iplist17))

#Количество ip адреслв всего и уникальных на 18 мая
with open('apache_logs.txt') as f:
    ip_data18 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[18'
    log = f.read()
    ip_list18 = re.findall(ip_data18, log)
#print(ip_list18) 
count_ip18 = len(ip_list18) #Подсчет всех ip адресов
print('8.Количество всех ip адресов на 18 мая составляет:', count_ip18)
unic_iplist18 = set(ip_list18) # Подсчет уникальных ip адресов
print('9.Количество уникальных ip адресов на 18 мая составляет:', len(unic_iplist18))

#Количество ip адреслв всего и уникальных на 19 мая
with open('apache_logs.txt') as f:
    ip_data19 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[19'
    log = f.read()
    ip_list19 = re.findall(ip_data19, log)
#print(ip_list19) 
count_ip19 = len(ip_list19) #Подсчет всех ip адресов
print('10.Количество всех ip адресов на 19 мая составляет:', count_ip19)
unic_iplist19 = set(ip_list19) # Подсчет уникальных ip адресов
print('11.Количество уникальных ip адресов на 19 мая составляет:', len(unic_iplist19))

#Количество ip адреслв всего и уникальных на 20 мая
with open('apache_logs.txt') as f:
    ip_data20 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s\-\s\[20'
    log = f.read()
    ip_list20 = re.findall(ip_data20, log)
#print(ip_list20) 
count_ip20 = len(ip_list20) #Подсчет всех ip адресов
print('12.Количество всех ip адресов на 20 мая составляет:', count_ip20)
unic_iplist20 = set(ip_list20) # Подсчет уникальных ip адресов
print('13.Количество уникальных ip адресов на 20 мая составляет:', len(unic_iplist20))