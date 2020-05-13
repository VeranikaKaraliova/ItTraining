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
