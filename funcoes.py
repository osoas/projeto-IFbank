from funcoesMenu import getMenuLogin, printLine
from globais import pessoas, contas, nums
from classConta import Conta
from classPessoa import Pessoa
from funcoesGet import getIdade, getCpf, getOption 
            
from buscas import buscar_conta_por_cpf, buscar_conta_por_num

def criar_conta() -> None:
    global pessoas, contas, nums
    
    printLine()
    nome = input("Insira seu nome: ")        
    idade = getIdade("Insira sua idade: ")        
    cpf = getCpf("Insira seu CPF: ")        
    senha = input("Crie uma senha: ")
    
    newPessoa = Pessoa(nome, idade, cpf)
    
    newConta = Conta(newPessoa, senha)
    newNum = newConta.getNum()
    
    nums.append(newNum)
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
        cpfInserido = getCpf("Insira o CPF do titular: ")
        contaLogin = buscar_conta_por_cpf(cpfInserido)
    elif optionLogin == 2:
        numInserido = input("Insira o número da conta: ")
        contaLogin = buscar_conta_por_num(numInserido)

    if contaLogin:
        print(f"Olá, {contaLogin.getTitular().getNome()}")
        logou = autenticar_senha(contaLogin)
        if logou:
            return contaLogin
        else:
            return False
    else:
        printLine()
        print("Conta não encontrada.")



def autenticar_senha(conta: Conta) -> bool:
    printLine()
    numTentativas = 0

    while numTentativas < 3:
        senhaInserida = input("Insira a senha da conta: ")
        if senhaInserida == conta.getSenha():
            printLine()
            print("Conta logada com sucesso!")
            return True
        else:
            numTentativas += 1
            print(f"Senha incorreta! Tentativas restantes: {3 - numTentativas}")

    printLine()
    print("Número máximo de tentativas alcançado. Tente novamente mais tarde.")
    return False




