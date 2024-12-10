import random

def main() -> None:
    
    #variáveis de controle
    nums = []
    
    option = getOption(getMenu(), [1,2,3,0])
    if option == 1:
        #criação de conta
        nome = input("Insira seu nome: ")        
        idade = input("Insira sua idade: ")        
        cpf = input("Insira seu CPF: ")        
        
        newPessoa = Pessoa(nome, idade, cpf)
    
    return

class Pessoa:
    def __init__(self, nome, idade, cpf):
      self.cpf = cpf
      self.nome = nome
      self.idade = idade

class Conta:
    def __init__(self, num: str, titular: Pessoa, saldoReal: float = 0, saldoDol: float = 0):
      self.num = num
      self.saldoReal = saldoReal
      self.saldoDol = saldoDol
      self.titular = titular

def getMenu() -> str:
    
    menu = """
    ========================================
              Bem-vindo ao IFbank
    ========================================
    1. Criar Conta
    2. Logar
    3. Sair
    ========================================
    """
    return menu

def getOption(txt: str, valid_options: list[int]) -> int:
    while True:
        print(txt)
        try:
            option = int(input())
            if option in valid_options:
                return option
            else:
                print("Essa opção não existe")
        except ValueError:
            print("Valor incorreto.")
            
def gerarNum() -> str:
    return str(random.randint(100000, 999999))
main()