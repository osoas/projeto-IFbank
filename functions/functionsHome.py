from classes.accountClass import Account
from functions.functionsGet import getAge, getCpf, getOption, getPassword
from functions.searches import searchAccountByCpf, searchAccountByNum
from functions.functionsMenu import printLine, getLoginMenu
from functions.generates import generateNum
from firebase.config import db

def createAccount() -> None:
    printLine()
    cpf = getCpf("Insira seu CPF: ")

    userRef = db.collection("users").document(cpf)
    if userRef.get().exists:
        printLine()
        print("Já existe uma conta associada a este CPF.")
        printLine()
        return

    name = input("Insira seu nome: ")
    age = getAge("Insira sua idade: ")
    password = getPassword("Crie uma senha: ")


    userRef.set({
        "name": name,
        "age": age,
        "cpf": cpf
    })

    accountNumber = generateNum()  
    newAccount = Account(password=password, holderId=cpf, num=accountNumber)

    db.collection("accounts").document(accountNumber).set({
        "password": password,
        "holderId": cpf, 
        "num": newAccount.getNum(),
        "realValue": 0,
        "keys": [],
        "contacts": []  
    })

    printLine()
    print(f"Conta criada com sucesso! Número da conta: {newAccount.getNum()}")
    printLine()



def login() -> Account | bool:
    printLine()
    optionLogin = getOption(getLoginMenu(), [1, 2])
    loginAccount = None
    
    if optionLogin == 1:
        cpfInserted = input("Insira o CPF do titular: ")
        loginAccount = searchAccountByCpf(cpfInserted)
    if optionLogin == 2:
        numInserted = input("Insira o número da conta: ")
        loginAccount = searchAccountByNum(numInserted)

    if loginAccount:
        isValid = authenticatePass(loginAccount)
        if isValid:
            holderId = loginAccount.getHolderId()

            usersRef = db.collection("users")
            userDoc = usersRef.document(holderId).get()

            if userDoc.exists:
                user_data = userDoc.to_dict()
                print(f"Olá, {user_data['name']}")  
                return loginAccount
            else:
                printLine()
                print("Usuário não encontrado.")
                return False
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
            print(f"Senha incorreta! Tentativas restantes: {3 - attemps}")

    printLine()
    print("Número máximo de tentativas alcançado. A conta foi bloqueada.")
    account.blockAccount() 

    
    return False




