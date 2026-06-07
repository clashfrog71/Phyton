import subprocess
import time
restaurantes = ['pizza','tomate']
def tudo():
   try:
      print('opções')
      print('1 registrar um restaurante')
      print('2 listar restaurantes')
      print('3 Sair da aplicação')
      opcao_escolhida = int(input())
      match opcao_escolhida:
         case 1:
            cadastrar_restaurante()
         case 2:
            listar_restaurantes()
         case 3:
            print('encerrando aplicação...')
            time.sleep(1)
            subprocess.check_call("cls", shell=True)
            print('Aplicação encerrada')
            exit
         case _:
            print('opção invalida! encerrando aplicação')
            time.sleep(2)
            subprocess.check_call("cls", shell=True)
            print('aplicação encerrada')             
   except:
      
      opcao_invalida()
def cadastrar_restaurante():
   subprocess.check_call("cls", shell=True)
   print('cadastrar restaurante')
   nomeRestaurante = input('digite o nome do restaurante que deseja cadastrar: \n')
   restaurantes.append(nomeRestaurante)
   print(f'o {nomeRestaurante} foi cadastrado com sucesso!')
   voltar_MenuPrincipal()
def listar_restaurantes():
   subprocess.check_call("cls", shell=True)
   print('listando restaurantes:\n')
   for restaurante in restaurantes:
      print(restaurante)
   voltar_MenuPrincipal()
def opcao_invalida():
   print('Opção Ivalida')
   voltar_MenuPrincipal()
def voltar_MenuPrincipal():
   input('aperte qualquer tecla para voltar')
   subprocess.check_call("cls", shell=True)
   main()

   
def main():
   tudo()  
if __name__ == '__main__': 
   main()
   
