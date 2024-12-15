from classes.accountClass import Account
from globalsVar import persons, accounts

def searchAccountByCpf(cpf: str) -> Account | None:
    for person in persons:
        if cpf == person.getCpf():
            for account in accounts:
                if account.getHolder() == person:
                    return account        
    return None

def searchAccountByNum(num: str) -> Account | None:
    for account in accounts:
        if num == account.getNum():
            return account
    return None