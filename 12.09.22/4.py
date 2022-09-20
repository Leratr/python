category=str(input())
price=int(input())
if category=='Продукты':
    print(price)
    if price<100:
        print('Попробуйте нашу выпечку!')
    if price>=100 and price<500:
        print('Как насчёт орехов в шоколаде?')
    if price>=500:
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома!')
    

