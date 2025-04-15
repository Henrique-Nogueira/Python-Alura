def exercicio_1():
    print('\n1- Imprima a frase: Python na Escola de Programação da Alura.\n')

    print('Python na Escola de Programação da Alura\n')

def exercicio_2():

    print('\n2- Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.\n')

    nome = 'Henrique Nogueira dos Santos'
    idade = 21

    print(f'Meu nome é {nome} e tenho {idade} anos\n')

def exercicio_3():

    print('\n3- Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:\n')

    print('A', 'L', 'U', 'R', 'A' , sep='\n')
    # Ou podemos utilizar também: 
    # print('''A
    # L
    # U
    # R
    # A''')

def exercicio_4():
        
    print('\n4- Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:\n')

    pi = 3.14159
    pi_arredondado = round(pi, 2)

    print(f'O valor arredondado de pi é: {pi_arredondado}\n')

def hora_da_pratica1():
   escolha = int(input('\nDigite qual exercício entre 1 e 4 você gostaria de visualizar, caso queira sair digite 5: '))

   match escolha:
         case 1:
              exercicio_1()
              hora_da_pratica1()
         case 2:
              exercicio_2()
              hora_da_pratica1()
         case 3:
              exercicio_3()
              hora_da_pratica1()
         case 4:
              exercicio_4()
              hora_da_pratica1()
         case 5:
             print('Finalizando o app\n')
         case _:
              print('Escolha uma opção válida entre 1 e 4.')

hora_da_pratica1()