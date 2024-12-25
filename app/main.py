import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from functions.functionsMenu import getMenu, getLoggedMenu, printLine
from functions.functionsGet import getOption
from functions.functionsHome import createAccount, login
from functions.functionsLogged import viewInfo, transaction, registerKey, makeDeposit

from classes.accountClass import Account
from classes.personClass import Person

# Variáveis globais
from globalsVar import accounts, persons
loggedAccount = None

#TODO -> criar class transação
#TODO -> cada transação deve ser uma instancia da class Transação
#TODO -> guardar o histórico de transações

osoas = Person("osoas", 23, "11111111111")
roni = Person("roni", 50, "99999999999") 
persons.append(osoas)
persons.append(roni)
contaOsoas = Account(osoas, "123")
contaRoni = Account(roni, "123")
accounts.append(contaOsoas)
accounts.append(contaRoni)


def main() -> None:
    global loggedAccount
    
    while True:
        option = getOption(getMenu(), [1, 2, 0])

        if option == 1:
            createAccount()
            input()
    
        if option == 2:
            loggedAccount = login()
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
            #TODO -> salvar os contatos 
            transaction(loggedAccount)
            input()
        if option == 3:
            #DOING by isaias -> cadastro de chave pix nova
            registerKey(loggedAccount)
            input()
        if option == 4:
            #TODO -> ver os contatos salvos para efetuar pix rápidamente
            return
        if option == 5:
            loggedAccount.peDeMeia()    
        
        if option == 6:
            loggedAccount = None
            

        if option == 7:
            makeDeposit(loggedAccount) 
            input()
            main()
            
        # 1 ver infos 
        # 2 realizar transação 
        # 3 cadastrar pix
        # 4 contatos salvos TODO
        # 5 pé de meia
        # 6 sair da conta
        # 7 Realizar depósito
        
        
        

main()
