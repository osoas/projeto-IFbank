from classes.accountClass import Account

def viewInfo(account: Account) -> str:
    
    return f"""
{"=" * 40}
Titular: {account.getHolder().getName()}
Idade: {account.getHolder().getAge()}
CPF: {account.getHolder().getCpf()}
{"=" * 40}
Número: {account.getNum()} 
saldo em real: {account.getRealValue()}
{"=" * 40}
"""
   
   
def makeTransaction(senderAccount: Account, destinationAccount: Account, value: float) -> bool:
    removed = senderAccount.take(value)
    if removed:        
        received = destinationAccount.receive(value)
        if not received:
            senderAccount.receive(value)
       
    return removed and received
    