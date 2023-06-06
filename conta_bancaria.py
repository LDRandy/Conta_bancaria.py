# type: ignore
import datetime

from colorama import Fore, Back, init, Style
init(autoreset=True)

######################################################


class Extrato_conta:

     lista = []
          
class Conta_bancaria(Extrato_conta):
     
     def __init__(self, nome_completo, nome_usuario, renda_mensal, extrato_usuario, saldo_conta=0, saldofisico=0):
          
          self.nome_completo = nome_completo.title()
          self.nome_usuario = nome_usuario
          self.renda_mensal = renda_mensal
          self.saldo_conta = saldo_conta
          self.saldofisico = saldofisico
          self.extrato_usuario = extrato_usuario
          
          self.extrato_usuario = Extrato_conta.lista
          self.saldofisico = self.renda_mensal
          
     def depositar(self):

          while True:
               
               print("( 1 ) - Depositar\n( 2 ) - Voltar\n")
               
               result = input('------> ')
               
               if result == '1':
                    valor = input("\tQual o valor que você deseja depositar? R$")

                    if valor.isnumeric():
                         valor = float(valor)

                         if self.saldofisico >= valor:
                              time_now = datetime.datetime.now()
                              
                              self.saldo_conta += valor
                              self.saldofisico -= valor
                              self.extrato_usuario.append(f"DEPOSITO -> R${valor} | {time_now.date()} / {time_now.strftime('%H:%M:%S')}")
                              
                              return f"\t{Fore.BLACK + Back.GREEN + ' Deposito concluido com Sucesso! ' + Style.RESET_ALL}"
                              
                         else:
                              return f"\t{Fore.BLACK + Back.RED + ' Infelizmente Você não tem saldo suficiente para fazer o deposito. ' + Style.RESET_ALL}"
                              
                    else:
                         print("\tPor favor, Digite O valor de Deposito corretamente.\n")
               
               if result == '2':
                    return ''
                    
     def sacar(self):
          
          while True:
                              
               print("( 1 ) - Sacar\n( 2 ) - Voltar\n")
               
               result = input('------> ')
               
               if result == '1':
               
                    valor = input("\tQual o valor que você deseja Sacar? R$")
                    
                    if valor.isnumeric():
                         valor = float(valor)
               
                         if self.saldo_conta >= valor:
                              time_now = datetime.datetime.now()
                              
                              self.saldofisico += valor
                              self.saldo_conta -= valor
                              self.extrato_usuario.append(f"SAQUE -> R${valor} | {time_now.date()} / {time_now.strftime('%H:%M:%S')}")
                              
                              return f"\t{Fore.BLACK + Back.GREEN + ' Saque concluido com Sucesso! ' + Style.RESET_ALL}"
                         else:
                              return f"\t{Fore.BLACK + Back.RED + ' Infelizmente Você não tem deposito suficiente para fazer o saque. ' + Style.RESET_ALL}"
                              
                    else:
                         print("\tPor favor, Digite O valor de Saque corretamente.\n")
                         
               if result == '2':
                    return ''
                    
     def usuario_extrato(self):
          if self.extrato_usuario == []:
               print("Você ainda não possui movimentação para ter o Extrato.")
               print()
               return
          for acoes in self.extrato_usuario:
               print(acoes)
               print()
               
     def config_conta(self):
          
          print("Agora você esta nas configuraçoes da sua conta.")
          
          print(f"\n( 1 ) - Nome Completo: {self.nome_completo}\n( 2 ) - Nome de Usuario: {self.nome_usuario}\n( 3 ) - Renda Mensal: {self.renda_mensal}\n")

          while True:

               print("Deseja fazer alguma alteração acima? (SIM) / (NÃO)")
               pergunta1 = input("-> ")
               
               if pergunta1.upper() == "SIM":
                    
                    while True:
                    
                         pergunta2 = input("\tDigite o numero do item -> ")
                         
                         if pergunta2.isnumeric():

                              pergunta2 = int(pergunta2)
                              
                              if pergunta2 == 1:
                                   alterar = input(f"\t\t{self.nome_completo} => ")
                                   self.nome_completo = alterar
                                   print("Alteração feita com Sucesso!")
                                   print()
                                   return True

                              if pergunta2 == 2:
                                   alterar = input(f"\t\t{self.nome_usuario} => ")
                                   self.nome_usuario = alterar
                                   print("Alteração feita com Sucesso!")
                                   print()
                                   return True
                              
                              if pergunta2 == 3:
                                   while True:
                                        alterar = input(f"\t\tR${self.renda_mensal} => R$")
                                        if alterar.isnumeric():
                                             alterar = float(alterar)
                                             if alterar > 0:
                                                  self.renda_mensal = alterar
                                                  print("Alteração feita com Sucesso!")
                                                  print()
                                                  return True
                    
                         else:
                              print("\tResponda corretamente a pergunta.")
                                        
               elif pergunta1.upper() in ["NÃO" , "NAO"]:
                    print("Certo, NENHUMA alteração foi feita.")
                    print()
                    return False
               
               print("Responda corretamente a pergunta.")
    
#######################################################################

def pegar_renda():
     while True:
          renda = input("Digita sua renda renda mensal: R$")
          if renda.isnumeric():
               renda = float(renda)
               if renda > 0:
                    return renda
     

print()

pessoa_usuario = Conta_bancaria( input("Digite seu nome completo: ") , input("Defina seu nome de usuario: ") , pegar_renda() , True )

print()

while True:
     
     print(f"|- Logado como ( {pessoa_usuario.__dict__['nome_usuario']} )\n|- Nome Completo: {pessoa_usuario.__dict__['nome_completo']}\n|- Saldo: {pessoa_usuario.__dict__['saldo_conta']}\n|- ( Saldo_Dinheiro_Fisico: {pessoa_usuario.__dict__['saldofisico']} )")
     
     print()
     
     print("Escolha uma das opções para interagir com a plataforma.")
     print("( 1 ) - Depositar")
     print("( 2 ) - Sacar")
     print("( 3 ) - Ver Extrato")
     print("( 4 ) - Configurações")
     print("( 000 ) - Sair")
     
     opcao = input("\n-> ")
     
     if opcao == '000':
          exit()
     
     elif opcao.isnumeric():
          opcao = int(opcao)
          
          if opcao == 1:
               print(pessoa_usuario.depositar())
               print()
               
          if opcao == 2:
               print(pessoa_usuario.sacar())
               print()
               
          if opcao == 3:
               print()
               pessoa_usuario.usuario_extrato()
               
          if opcao == 4:
               pessoa_usuario.config_conta()
