from functions.functionsMenu import getLoginMenu, printLine
from globalsVar import persons, accounts, nums
from classes.accountClass import Person
from functions.functionsGet import getAge, getCpf, getOption 

from functions.searches import searchAccountByNum, searchAccountByCpf
from classes.accountClass import Account

def createAccount() -> None:
    printLine()
    name = input("Insira seu nome: ")        
    age = getAge("Insira sua idade: ")        
    cpf = getCpf("Insira seu CPF: ")        
    password = input("Crie uma senha: ")
    
    newPerson = Person(name, age, cpf)
    
    newAccount = Account(newPerson, password)
    newNum = newAccount.getNum()
    
    nums.append(newNum)
    persons.append(newPerson)
    accounts.append(newAccount)
    
    printLine()
    print(f"Conta criada com sucesso! Número da conta: {newNum}")
    printLine()

def login() -> Account | bool:
    printLine()
    optionLogin = getOption(getLoginMenu(), [1, 2])
    loginAccount = None
    
    if optionLogin == 1:
        cpfInserted = getCpf("Insira o CPF do titular: ")
        loginAccount = searchAccountByCpf(cpfInserted)
    if optionLogin == 2:
        numInserted = input("Insira o número da conta: ") #TODO -> função usando regex para validar o numero da conta, criar um padrão de numero
        loginAccount = searchAccountByNum(numInserted)

    if loginAccount:
        print(f"Olá, {loginAccount.getHolder().getName()}")
        isValid = authenticatePass(loginAccount)
        if isValid:
            return loginAccount
        else:
            return False
    else:
        printLine()
        print("Conta não encontrada.")
        return False



def authenticatePass(account: Account) -> bool:
    printLine()
    attemps = 0

    while attemps < 3:
        passEntered = input("Insira a senha da conta: ")
        if passEntered == account.getPass():
            printLine()
            print("Conta logada com sucesso!")
            return True
        else:
            attemps += 1
            #TODO -> se passar o numero de tentativas, bloquar conta
            print(f"Senha incorreta! Tentativas restantes: {3 - attemps}")

    printLine()
    print("Número máximo de tentativas alcançado. Tente novamente mais tarde.")
    return False




