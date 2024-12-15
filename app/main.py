import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from functions.functionsMenu import getMenu, getLoggedMenu, printLine, getTransactionMenu
from functions.functionsGet import getOption, getFloat, getCpf
from functions.functionsHome import createAccount, login
from functions.functionsLogged import makeTransaction, viewInfo
from functions.searches import searchAccountByCpf, searchAccountByNum

from classes.accountClass import Account
from classes.personClass import Person

# Variáveis globais
from globalsVar import accounts, persons
loggedAccount = False

#TODO -> criar class transação
#TODO -> cada transação deve ser uma instancia da class Transação
#TODO -> guardar o histórico de transações

osoas = Person("osoas", 23, "11111111111")
roni = Person("roni", 50, "99999999999")
persons.append(osoas)
persons.append(roni)


accounts.append(Account(osoas, "123"))
accounts.append(Account(roni, "123"))


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
            transactionOption = getOption(getTransactionMenu(), [1, 2, 3])
            destinationAccount = False     
            
            if transactionOption == 1:
                destinationCpf = getCpf("Insira o cpf da conta destino: ")
                destinationAccount = searchAccountByCpf(destinationCpf)
            if transactionOption == 2:
                destinationNum = input("Insira o numero da conta destino: ")
                destinationAccount = searchAccountByNum(destinationNum)
                
            value = getFloat("insira o valor da transação: ")
            makeTransaction(loggedAccount, destinationAccount, value)
        if option == 3:
            #TODO -> cadastro de chave pix nova
            return
        if option == 4:
            #TODO -> ver os contatos salvos para efetuar pix rápidamente
            return
        if option == 5:
            loggedAccount.peDeMeia()    
        
        if option == 6:
            loggedAccount = False
            main()
            
        # 1 ver infos 
        # 2 realizar transação 
        # 3 cadastrar pix TODO
        # 4 contatos salvos TODO
        # 5 pé de meia
        # 6 sair da conta
        
        
        

main()
