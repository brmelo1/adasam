a=int(input('manda um nuemro: '))
b=int(input('manda um nuemro: '))
if a<5 and b<5:
    c=a+b
    print(f'a soma de {a} + {b} = {c}')
elif a==5 or b==5:
    c=a-b
    print(f'a sub de {a} - {b} = {c}')
elif a>5 and b>5:
    c=a*b
    print(f'a multi de {a} x {b} = {c}')
else:
    c=a/b
    print(f'a multi de {a} x {b} = {c:.2f}')
