def teste(numero):
    while True:
        try:
            tqsn = float(input(numero))
            return tqsn
        except ValueError:
            print('Tem que ser numero')

a = teste('Digite um número: ')