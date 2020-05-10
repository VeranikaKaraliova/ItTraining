print('Калькулятор ИМС с рекомендациями для женщин')

def fc_menu():
    menu = {
        1 : "Новый пользователь", 
        2 : "Завершить программу"}
    print(menu)

def fc_choice():
    choice = int(input('выберите 1 или 2: '))
    count = 1
    users = {} 
    users[count] = {}
    data = str('height.weight.age')
    if choice == 1:
        while True:
            users[count]['name'] = input('Введите имя: ')
            users[count]['lastname'] = input('Введите фамилию: ')
            users[count][data] = input('Введите данные в формате рост.вес.возраст: ')
            for key, value in users.items():
               print(key, value)
            hwa = users[count][data]
            print(hwa)
            x = hwa.rsplit('.')
            m = float(x[1]) # Вес
            h = float(x[0]) # Рост
            age = int(x[2])
            bmi = m / (h/100)**2
            print("Ваш индекс массы тела:", '%.2f' % bmi)
            print('15' + ("=" *(int(bmi) - 15)) + '|' + ('=' * (35 - (int(bmi) - 15)) + '50'))
            if (19.5<= bmi < 23.3 and 19 <= age < 25) or (23.3 <= bmi <23.5 and 25<= age <35) or (23.5 <= bmi and 35<= age):
                print('Вам ИМС в пределах нормы. Оставайтесь в форме!')
            elif (19.5 > bmi and 19 <= age < 25) or (23.3 > bmi and 25<= age <35) or (23.5 > bmi and 35<= age):
                print('Ваш ИМС ниже нормы! Вам нужно больше кушать!')
            else:
                print('Ваш ИМС выше нормы! Вам нужно избавиться от холодильника!')
            count +=1
            new = int(input('Выберите номер пункта: 1.Добавить еще пользователя. 2.Вывести список и завершить. 3. Выйти. : '))
            if new ==2:
                for key, value in users.items():
                    print(key, value)
                break
            elif new == 1:
                users[count] = {}
            else:
                print('The end.')
                break
    elif choice == 2:
        print('The end.')


def main():
    fc_menu()
    fc_choice()
    


if __name__ == "__main__":
    main()