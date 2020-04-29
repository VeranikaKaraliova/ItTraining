m = float(input("Введите массу тела в килограммах: "))
h = float(input("Введите рост в метрах: "))
bmi = m / h**2
print("Ваш индекс массы тела:", '%.2f' % bmi)
print('15' + ("=" *(int(bmi) - 15)) + '|' + ('=' * (35 - (int(bmi) - 15)) + '50'))
# Min value = 15, max value = 50.