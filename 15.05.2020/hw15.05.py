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
