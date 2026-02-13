from math import sqrt
a = int(input('Digite o número A da equação: '))
b = int(input('Digite o número B da equação: '))
c = int(input('Digite o número C da equação: '))

#Delta 
delta = float((b ** 2) - 4 * a * c)

#E se

if delta <0:
       print('Delta é negativo, a conta acaba por aqui')
else:
        print((f'DELTA = {b}² - 4 x {a} x {c} é igual a: {delta}'))
        print(f' X1 positivo = {b} + {sqrt(delta)} / 2 x {a} é igual a: {(-b + sqrt(delta)) / (2 * a)}')
        print(f' X2 negativo = {b} - {sqrt(delta)} / 2 x {a} é igual a: {(-b - sqrt(delta)) / (2 * a)}')