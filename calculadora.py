'''Calculadora com while'''

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)

        operadores_permitidos = '+-/*'
        if operador not in operadores_permitidos:
           print('Operador inválido')
           continue

        if len(operador) > 1:
            print('Digite apenas um operador')
            continue
        
        print('Realizando sua conta, confira o resultado: ')
        if operador == '+':
            print(num_1 + num_2)
        elif operador == '-':
            print(num_1 - num_2)
        elif operador == '/':
            print(num_1 / num_2)
        elif operador == '*':
            print(num_1 * num_2)


    except:
        print('Digite apenas numeros')



    sair = input('Quer sair? [s]im: ').lower().startswith('s')
   
    if sair is True:
        break