import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from functions.functionsMenu import getMenu, getLoggedMenu, printLine
from functions.functionsGet import getOption, getFloat
from functions.functionsHome import createAccount, login
from functions.functionsLogged import viewInfo, transaction, registerKey, makeDeposit, viewContacts

loggedAccount = None

#TODO -> criar class transação
#TODO -> cada transação deve ser uma instancia da class Transação
#TODO -> guardar o histórico de transações
#TODO -> as contas são bloqueadas mas não são impedidas de fazer transações. Faça isso acontecer

def main() -> None:
    global loggedAccount
    
    while True:
        option = getOption(getMenu(), [1, 2, 0])
        
        if option == 1:
            createAccount()
            input()
    
        if option == 2:
            loggedAccount = login()
            if not loggedAccount:
                continue
            input()
            break
            
        if option == 0:
            printLine()
            print("Obrigado por usar o IFbank!")
            return

    while True:
        option = getOption(getLoggedMenu(), [1, 2, 3, 4, 5, 6])
        if option == 1:
            print(viewInfo(loggedAccount))
            input()
        
        if option == 2:
            transaction(loggedAccount)
            input()
        if option == 3:
            registerKey(loggedAccount)
            input()
        if option == 4:
            viewContacts(loggedAccount)
            return
        if option == 5:
            loggedAccount = None
            main()
        if option == 6:
            value = getFloat("Digite o valor do deposito: ")
            makeDeposit(loggedAccount, value) 
            input()

        
        
        

main()
