from firebase_admin import firestore
from functions.functionsMenu import getNewKeyMenu
from functions.functionsGet import getOption, getCpf, getFloat, getNum, getEmail
from functions.functionsMenu import getTransactionMenu, getSaveContactMenu
from functions.searches import searchAccountByKey, searchAccountByCpf, searchAccountByNum
from functions.generates import generatePix
from classes.accountClass import Account
import firebase_admin
from firebase.config import db

def viewInfo(account: Account) -> str:
    
    accountRef = db.collection("accounts")    
    account_query = accountRef.where("num", "==", account.getNum()).get()
    
    if not account_query:
        print(f"Conta com o número {account.getNum()} não encontrada.")
        return "Conta não encontrada."
    
    accountData = account_query[0].to_dict()

    holderRef = db.collection("users").document(accountData['holderId'])
    holderData = holderRef.get().to_dict()

    if not holderData:
        print("Titular da conta não encontrado.")
        return "Titular da conta não encontrado."

    return f"""
{"=" * 40}
Titular: {holderData['name']}
Idade: {holderData['age']}
CPF: {holderData['cpf']}
{"=" * 40}
Número: {accountData['num']} 
Saldo em real: {accountData['realValue']}
Chaves pix: {accountData['keys']}
{"=" * 40}
"""


   
def makeTransaction(senderAccount: Account, destinationAccount: Account, value: float) -> bool:
    senderRef = db.collection("accounts").document(senderAccount.getNum())
    receiverRef = db.collection("accounts").document(destinationAccount.getNum())

    senderData = senderRef.get().to_dict()
    senderRealValue = senderData.get('realValue', 0)

    if senderRealValue >= value:
        senderRef.update({
            "realValue": senderRealValue - value
        })

        receiverData = receiverRef.get().to_dict()
        receiverRealValue = receiverData.get('realValue', 0)
        receiverRef.update({
            "realValue": receiverRealValue + value
        })

        return True
    return False
def transaction(loggedAccount: Account) -> None:
    transactionOption = getOption(getTransactionMenu(), [1, 2, 3])
    keyDestination = None

    if transactionOption == 1:
        keyDestination = getCpf("Insira o CPF da conta destino: ")
    elif transactionOption == 2:
        keyDestination = getNum("Insira o número da conta destino: ")
    elif transactionOption == 3:
        keyDestination = input("Insira a chave Pix da conta destino: ")

    destinationAccount = searchAccountByKey(keyDestination)

    if not destinationAccount:
        print("Conta destino não encontrada!")
        return

    value = getFloat("Insira o valor da transação: ")
    success = makeTransaction(loggedAccount, destinationAccount, value)

    if success:
        name = db.collection("users").document(destinationAccount.getHolderId()).get().to_dict()["name"]
        print(f"Transação efetuada para {name} com sucesso!")

        save = getOption(getSaveContactMenu(), [1, 2])
        if save == 1:
            account_ref = db.collection("accounts").document(loggedAccount.getNum())
            account_data = account_ref.get().to_dict()

            if "contacts" not in account_data:
                account_data["contacts"] = []  

            if destinationAccount.getNum() not in account_data["contacts"]:
                account_data["contacts"].append(destinationAccount.getNum())  
                account_ref.update({"contacts": account_data["contacts"]})
                loggedAccount.attAccount()
                print("Conta destino adicionada aos contatos.")
            else:
                print("Conta destino já está nos contatos.")
    else:
        print("Não foi possível efetuar a transação.")


        
def registerKey(account: Account) -> bool:
    option = getOption(getNewKeyMenu(), [1, 2, 3, 4])
    success = False

    if option == 1:
        success = account.addKey(account.getHolderId())
    elif option == 2:
        success = account.addKey(account.getNum())
    elif option == 3:
        success = account.addKey(generatePix()) 
    elif option == 4:
        email = getEmail("Digite seu email: ") 
        success = account.addKey(email)

    if success:
        accountRef = db.collection("accounts").document(account.getNum())
        accountRef.update({
            "keys": account.getKeys()
        })
        print("Chave pix registrada com sucesso!")
        return True
    
    print("Falha ao registrar chave pix")
    return False


def makeDeposit(account: Account, value: float) -> bool:
    if value <= 0:
        print("O valor do depósito deve ser maior que zero.")
        return False
    
    accountRef = db.collection("accounts").document(account.getNum())
    currentRealValue = accountRef.get().to_dict().get('realValue', 0)

    accountRef.update({
        "realValue": currentRealValue + value
    })

    print(f"Depósito de R${value:.2f} realizado com sucesso!")
    return True



def viewContacts(account: Account) -> None:
    contacts = account.getContacts()
    
    if not contacts:
        print("Você ainda não possui contatos.")
        return

    contact_options = []
    contact_mapping = {}

    print("\n========================================")
    print("    Escolha um contato para transação:")
    print("========================================")

    for idx, contact_num in enumerate(contacts, start=1):
        contactAccount = searchAccountByNum(contact_num)
        if not contactAccount:
            continue
        
        contactHolder = db.collection("users").document(contactAccount.getHolderId())
        name = contactHolder.get().to_dict()["name"]
        contact_options.append(f"{idx}. {name}")
        contact_mapping[idx] = contactAccount

    if not contact_options:
        print("Nenhum contato salvo.")
        return

    print("\n".join(contact_options))
    print("========================================")

    choice = getOption("", contact_mapping)
    destinationAccount = contact_mapping[choice]
    value = getFloat("Insira o valor da transação: ")
    success = makeTransaction(account, destinationAccount, value)
    if success:
        name = db.collection("users").document(destinationAccount.getHolderId()).get().to_dict()["name"]
        print(f"pix efetuado para {name} com sucesso")