from math import sqrt

def validador(tqsn):
        while True:
                     valor = input(tqsn)
                     try: 
                            return float(valor)
                     except ValueError:
                             print('Tente novamente digitando apenas números.')
                     

a = validador('Digite o número A da equação: ')
b = validador('Digite o número B da equação: ')
c = validador('Digite o número C da equação: ')

#Delta 
delta = float((b ** 2) - 4 * a * c)
print((f'🔺 = {b}² - 4 x {a} x {c} ='))
print(f'🔺 = {b ** 2} - {4 * a * c} = \n🔺 = {delta}')

#E se

if delta <0:
       print('Delta 🔺 é negativo, a conta acaba por aqui')
else:
        raiz_delta = sqrt(delta)
        print(f'X1 (adição) = {(-b)} + {raiz_delta} / (2 x {a}) é igual a: {(-b + raiz_delta) / (2 * a)}')
        print(f'X2 (subtração) = {(-b)} - {raiz_delta} / (2 x {a}) é igual a: {(-b - raiz_delta) / (2 * a)}')