# Importação de biblioteca
import os

# Lista de dicionarios representando os restaurantes
restaurantes = [{'nome' : 'praça', 'categoria':'japonesa', 'ativo': false },
               {'nome' : 'pizza suprema', 'categoria':'Pizza', 'ativo': True },
               {'nome' : 'cantina', 'categoria':'Italiano', 'ativo': false }]

def exibir_nome_do_programa ():
    print("""
          
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
  """ )
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair/n ')

def finalizar_app():
    exibir_subtitulo('Finalizando o app/n ')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()