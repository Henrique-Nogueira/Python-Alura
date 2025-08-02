import os

lista_de_restaurantes = ['Casa da Pizza', 'Coco Bambu', 'Outback']


def exibir_nome_do_programa():
      print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)


def voltar_ao_menu():
    input('\nPressione Enter para voltar ao menu principal...')
    main()

def subtitulo(texto):
      os.system('cls' if os.name == 'nt' else 'clear')
      print(texto)

def finalizar_app():
    subtitulo('Finalizando o app\n')

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair\n')

def opcao_invalida():
      print('Opção inválida, tente novamente.\n')
      exibir_opcoes()
      escolher_opcao()

def cadastrar_restaurante():
      subtitulo('Cadastro de restaurante\n')
      nome_do_restaurante = input('Digite o nome do restaurante: ')
      lista_de_restaurantes.append(nome_do_restaurante)
      print(f'Restaurante "{nome_do_restaurante}" cadastrado com sucesso!\n')
      voltar_ao_menu()

def listar_restaurantes():
      subtitulo('Lista de Restaurantes\n')
      if lista_de_restaurantes:
            for i, restaurante in enumerate(lista_de_restaurantes, start=1):
                print(f'{i}. {restaurante}')
      else:
            print('Nenhum restaurante cadastrado.')
      voltar_ao_menu()

def escolher_opcao():

      try:   
      
            opcao_escolhida = int(input('Escolha uma opção: '))
            
            if opcao_escolhida == 1: 
                  cadastrar_restaurante()

            elif opcao_escolhida == 2:
                  listar_restaurantes()

            elif opcao_escolhida == 3:
                  print('Ativar restaurante')
            
            elif opcao_escolhida == 4:
                  finalizar_app()
            
            else:
                  opcao_invalida()

      except:
            opcao_invalida()

def main():
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__': 
      main()