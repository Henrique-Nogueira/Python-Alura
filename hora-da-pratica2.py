def exercicio_1():
    print('\n1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.\n')
    numero_escolhido = int(input('Digite um número:'))

    if numero_escolhido % 2 == 0:
        print(f'O número {numero_escolhido} é par')
    else:
        print(f'O número {numero_escolhido} é ímpar')

def exercicio_2():
    print('\n2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:\n ')
    print('Criança: 0 a 12 anos', 'Adolescente: 13 a 18 anos', 'Adulto: acima de 18 anos', sep='\n')
    
    idade = int(input('Digite sua idade: '))

    if idade <= 12:
        print(f'Você é uma criança de {idade} anos')
    elif idade <= 18:
        print(f'Você é um adolescente de {idade} anos')
    else:
        print(f'Você é um adulto de {idade} anos')

def exercicio_3():
    print('\n3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.\n')
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    if usuario == 'alura' and senha == '123456':
        print('Usuário e senha corretos!')
    else:
        print('Usuário ou senha incorretos!')

def exercicio_4():
    print('\n4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:\n')
    print('Primeiro Quadrante: os valores de x e y devem ser maiores que zero;', 'Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;', 'Terceiro Quadrante: os valores de x e y são menores que zero;', 'Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero.', 'Caso Contrário: o ponto está localizado no eixo ou origem',  sep='\n')
    
    x = float(input('Digite a coordenada x: '))
    y = float(input('Digite a coordenada y: '))

    if x > 0 and y > 0:
        print(f'O ponto ({x}, {y}) está no primeiro quadrante')
    elif x < 0 and y > 0:
        print(f'O ponto ({x}, {y}) está no segundo quadrante')
    elif x < 0 and y < 0:
        print(f'O ponto ({x}, {y}) está no terceiro quadrante')
    elif x > 0 and y < 0:
        print(f'O ponto ({x}, {y}) está no quarto quadrante')
    else:
        print(f'O ponto ({x}, {y}) está localizado no eixo ou origem')

def hora_da_pratica2():
   escolha = int(input('\nDigite qual exercício entre 1 e 4 você gostaria de visualizar, caso queira sair digite 5: '))

   match escolha:
         case 1:
              exercicio_1()
              hora_da_pratica2()
         case 2:
              exercicio_2()
              hora_da_pratica2()
         case 3:
              exercicio_3()
              hora_da_pratica2()
         case 4:
              exercicio_4()
              hora_da_pratica2()
         case 5:
             print('Finalizando o app\n')
         case _:
              print('Escolha uma opção válida entre 1 e 4.')

hora_da_pratica2()