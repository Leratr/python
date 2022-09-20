price1=int(input())
price2=int(input())
price3=int(input())
price=price1+price2+price3
if price1<price2<price3:
    print('Акция!') or print(price//2)
elif price1>price2>price3:
    print('Акция!') or print(price//3)
else:
    print(price)
    


