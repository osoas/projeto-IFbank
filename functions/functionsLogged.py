from classes.accountClass import Account
from functions.functionsMenu import getNewKeyMenu
from functions.functionsGet import getOption, getCpf, getFloat, getNum
from functions.functionsMenu import getTransactionMenu
from functions.searches import searchAccountByKey

def viewInfo(account: Account) -> str:
    
    return f"""
{"=" * 40}
Titular: {account.getHolder().getName()}
Idade: {account.getHolder().getAge()}
CPF: {account.getHolder().getCpf()}
{"=" * 40}
Número: {account.getNum()} 
saldo em real: {account.getRealValue()}
Chaves pix: {account.getKeys()}
{"=" * 40}
"""
   
   
def makeTransaction(senderAccount: Account, destinationAccount: Account, value: float) -> bool:
    removed = senderAccount.take(value)
    if removed:        
        received = destinationAccount.receive(value)
        if not received:
            senderAccount.receive(value)
       
    return removed and received



def transaction(loggedAccount: Account) -> None:
    transactionOption = getOption(getTransactionMenu(), [1, 2, 3])
    destinationAccount = False     
    
    if transactionOption == 1:
        keyDestination = getCpf("Insira o cpf da conta destino: ")
    if transactionOption == 2:
        keyDestination = getNum("Insira o numero da conta destino: ")
    if transactionOption == 3:
        keyDestination = input("Insira a chave pix da conta destino: ")
    
    destinationAccount = searchAccountByKey(keyDestination)
        
    value = getFloat("insira o valor da transação: ")
    success = makeTransaction(loggedAccount, destinationAccount, value)
    if success:
        print(f"Transação efetuada para {destinationAccount.getHolder().getName()} com sucesso!")
    else:
        print(f"Não foi possível efetuar a transação.")
        
    
    
def registerKey(account: Account) -> bool:
    option = getOption(getNewKeyMenu(), [1,2,3,4])
    success = False
    if option == 1:
        success = account.addKey(account.getHolder().getCpf())
    if option == 2:
        success = account.addKey(account.getNum())
    if option == 3:
        success = account.addKey("0") #TODO -> função que gera uma key aleatória
    if option == 4:
        email = input("Digite seu email: ") #TODO -> função getEmail com padrão exigindo .com e @
        success = account.addKey(email)    
    if success:
        print("Chave pix registrada com sucesso!")
        return True
    return False