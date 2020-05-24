import datetime, time
import os

num = u"\u2593" *2
zero = [num * 3, '\n', f'{num}  {num}', '\n', f'{num}  {num}', '\n', f'{num}  {num}', '\n', num * 3,'\n']
one = [num, '\n', num, '\n', num, '\n', num, '\n', num, '\n']
two = [num *3, '\n', f'    {num}', '\n', num * 3, '\n', f'{num}    ','\n', num *3, '\n']
three = [num * 3, '\n', f'    {num}', '\n', num * 3, '\n', f'    {num}', '\n', num * 3, '\n']
four = [f'{num}  {num}', '\n', f'{num}  {num}', '\n', num * 3, '\n', f'    {num}', '\n', f'    {num}', '\n']
five = [num *3, '\n', f'{num}    ', '\n', num * 3, '\n', f'    {num}', '\n', num *3, '\n']
six = [num *3, '\n', f'{num}    ', '\n', num * 3, '\n', f'{num}  {num}', '\n', num *3, '\n']
seven = [num *3, '\n', f'    {num}', '\n', f'    {num}', '\n', f'    {num}', '\n', f'    {num}', '\n']
eight = [num * 3, '\n', f'{num}  {num}', '\n', num *3, '\n', f'{num}  {num}', '\n', num *3, '\n']
nine = [num * 3, '\n', f'{num}  {num}', '\n', num *3, '\n', f'    {num}', '\n', num * 3, '\n']
dot = ['  ','\n', '  ', '\n', num, '\n', '  ', '\n', '  ', '\n']
sl = {'0' : zero, '1' : one, '2' :two, '3' : three, '4' : four, '5' : five, '6' : six, '7' : seven, '8' : eight, '9' : nine, '10' : dot}

def search(obj):
    for a in range(len(obj)):
        print(obj[a], sep='', end='')

def read(n):
    i = 0
    for a in range(0,10,2):
        print(n[0][i], n[1][i], n[2][i], n[3][i], n[4][i],n[5][i], n[6][i], n[7][i], sep=' ', end='\n')
        i +=2
        
while True:
    time_now = datetime.datetime.now().time()
    st_time = time.strftime('%H.%M.%S')
    x = [(sl.get(st_time[0])), (sl.get(st_time[1])), dot, (sl.get(st_time[3])),
    (sl.get(st_time[4])), dot, (sl.get(st_time[6])), (sl.get(st_time[7]))]
    read(x)
    time.sleep(1)
    os.system('cls')