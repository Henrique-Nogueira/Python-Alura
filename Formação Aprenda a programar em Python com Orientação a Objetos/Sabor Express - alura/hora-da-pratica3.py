def exercicio_1():
    print('\n1 - Crie uma lista para cada informação a seguir: \nLista de números de 1 a 10; \nLista com quatro nomes; \nLista com o ano que você nasceu e o ano atual.\n')
    
    numeros = list(range(1, 11))
    nomes = ['Ana', 'Bruno', 'Carlos', 'Diana']
    ano_nascimento = 2004
    ano_atual = 2025
    anos = [ano_nascimento, ano_atual]

    print(f'Lista de números de 1 a 10: {numeros}')
    print(f'Lista com quatro nomes: {nomes}')   
    print(f'Lista com o ano que você nasceu e o ano atual: {anos}\n')

def exercicio_2():   
    print('2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.\n')
    numeros = [1, 2, 3, 4, 5]
    for numero in numeros:
        print(numero)

def exercicio_3():
    print('3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.\n')
    soma = 0
    for numero in range(1, 11):
        if numero % 2 != 0:
            soma += numero
    print(f'A soma dos números ímpares de 1 a 10 é: {soma}\n')

def exercicio_4():
    print('4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.\n')
    for numero in range(10, 0, -1):
        print(numero)

def exercicio_5():
    print('5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.\n')
    numero = int(input('Digite um número para ver sua tabuada: '))
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}') 

def exercicio_6():
    print('6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.\n')
    numeros = [1, 2, 3, "três", 4, "quatro", 5]
    soma = 0
    for numero in numeros:
        try:
            soma += numero
        except TypeError:
            print(f'Valor inválido: {numero}, não é um número.')

def exercicio_7():
    print('7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.\n')
    numeros = [10, 20, 30, 40]
    try:    
        media = sum(numeros) / len(numeros)
        print(f'A média dos números é: {media}')
    except ZeroDivisionError:
        print('A lista está vazia, não é possível calcular a média.')

def hora_da_pratica3():
   escolha = int(input('\nDigite qual exercício entre 1 e 7 você gostaria de visualizar, caso queira sair digite 8: '))

   match escolha:
         case 1:
              exercicio_1()
              hora_da_pratica3()
         case 2:
              exercicio_2()
              hora_da_pratica3()
         case 3:
              exercicio_3()
              hora_da_pratica3()
         case 4:
              exercicio_4()
              hora_da_pratica3()
         case 5:
             exercicio_5()
             hora_da_pratica3()
         case 6:
                exercicio_6()
                hora_da_pratica3()
         case 7:
                exercicio_7()
                hora_da_pratica3()
         case 8:
                print('Finalizando o app\n')
         case _:
              print('Escolha uma opção válida entre 1 e 7.')

hora_da_pratica3()