a = int(input())
b = int(input())
c = int(input())
if a != 0 and b != 0 and c != 0:
    print('Нет нулевых значений!!!')
if a == 0 and b == 0 and c == 0:
    print('Введены все нули!')
elif a == 0:
    print(a)
elif a != 0 and b == 0:
    print(b)
elif a != 0 and b != 0 and c == 0:
    print(c)
if a > b + c:
    print(a - b - c)
elif a < b + c:
    print(b + c - a)
if a > 50 and (b > a or c > a):
    print('Вася')
if a > 5 or (b == 7 and c == 7):
    print('Петя')