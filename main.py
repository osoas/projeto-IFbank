import random

# Variáveis globais
nums = []
pessoas = []
contas = []
contaLogada = None

def main() -> None:
    while True:
        option = getOption(getMenu(), [1, 2, 0])
        
        if option == 1:
            criar_conta()
        elif option == 2:
            realizar_login()
        elif option == 0:
            printLine()
            print("Obrigado por usar o IFbank! Até logo!")
            break
        
        
class Pessoa:
    def __init__(self, nome: str, idade: str, cpf: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade
        
    def getCpf(self) -> str:
        return self.__cpf

    def getNome(self) -> str:
        return self.__nome

class Conta:
    def __init__(self, num: str, titular: Pessoa, senha: str, saldoReal: float = 0, saldoDol: float = 0):
        self.__num = num
        self.__saldoReal = saldoReal
        self.__saldoDol = saldoDol
        self.__titular = titular
        self.__senha = senha

    def getNum(self) -> str:
        return self.__num
    
    def getTitular(self) -> Pessoa:
        return self.__titular

    def getSenha(self) -> str:
        return self.__senha        
        

def criar_conta() -> None:
    printLine()
    nome = input("Insira seu nome: ")        
    idade = getInt("Insira sua idade: ")        
    cpf = input("Insira seu CPF: ")        
    senha = input("Crie uma senha: ")
    
    newPessoa = Pessoa(nome, idade, cpf)
    newNum = gerarNum()
    nums.append(newNum)
    
    newConta = Conta(newNum, newPessoa, senha)
    pessoas.append(newPessoa)
    contas.append(newConta)
    printLine()
    print(f"Conta criada com sucesso! Número da conta: {newNum}")
    printLine()

def realizar_login() -> None:
    printLine()
    optionLogin = getOption(getMenuLogin(), [1, 2])
    contaLogin = None

    if optionLogin == 1:
        cpfInserido = input("Insira o CPF do titular: ")
        contaLogin = buscar_conta_por_cpf(cpfInserido)
    elif optionLogin == 2:
        numInserido = input("Insira o número da conta: ")
        contaLogin = buscar_conta_por_num(numInserido)

    if contaLogin:
        print(f"Olá, {contaLogin.getTitular().getNome()}")
        autenticar_senha(contaLogin)
    else:
        printLine()
        print("Conta não encontrada.")

def buscar_conta_por_cpf(cpf: str) -> Conta | None:
    for pessoa in pessoas:
        if cpf == pessoa.getCpf():
            for conta in contas:
                if conta.getTitular() == pessoa:
                    return conta
    return None

def buscar_conta_por_num(num: str) -> Conta | None:
    for conta in contas:
        if num == conta.getNum():
            return conta
    return None

def autenticar_senha(conta: Conta) -> None:
    printLine()
    numTentativas = 0

    while numTentativas < 3:
        senhaInserida = input("Insira a senha da conta: ")
        if senhaInserida == conta.getSenha():
            printLine()
            print("Conta logada com sucesso!")
            return
        else:
            numTentativas += 1
            print(f"Senha incorreta! Tentativas restantes: {3 - numTentativas}")

    printLine()
    print("Número máximo de tentativas alcançado. Tente novamente mais tarde.")



def getMenu() -> str:
    return """
========================================
            Bem-vindo ao IFbank
========================================
1. Criar Conta
2. Logar
0. Finalizar
========================================
"""

def getMenuLogin() -> str:
    return """
========================================
            Como deseja logar
========================================
1. CPF titular
2. Número da conta
========================================
    """

def getOption(txt: str, valid_options: list[int]) -> int:
    while True:
        print(txt)
        try:
            option = int(input())
            if option in valid_options:
                return option
            else:
                print("Essa opção não existe.")
        except ValueError:
            print("Valor incorreto. Digite um número válido.")

def getInt(txt: str) -> int:
    while True:
        try:
            num = int(input(txt))
            if num >= 18:
                return num
            else:
                print("Apenas maiores de 18 anos são aceitos.")
        except ValueError:
            print("Valor incorreto. Digite um número inteiro válido.")

def gerarNum() -> str:
    num = str(random.randint(100000, 999999))
    while num in nums:
        num = str(random.randint(100000, 999999)) 
    return num

def printLine() -> None:
    print("========================================")

main()