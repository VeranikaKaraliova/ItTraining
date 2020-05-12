def gen():
    count = 1
    while True:
        yield count
        count += 1
        if count % 3 == 0:
            print('Вася')
            count += 1   
my_gen = gen()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))