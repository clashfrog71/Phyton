import subprocess
import time
def tudo():
   print('opções')
   print('1 registrar um restaurante')
   print('2 listar restaurantes')
   opcao_escolhida = int(input())
   match opcao_escolhida:
      case 1:
         print('1 registrar um restaurante')
      case 2:
         print('2 listar restaurantes')
      case _:
         print('opção invalida! encerrando aplicação')
         time.sleep(2)
         subprocess.check_call("cls", shell=True)
         print('aplicação encerrada')             
def main():
   tudo()
if __name__ == '__main__': 
   main() 
  