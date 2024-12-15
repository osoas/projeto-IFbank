from classConta import Conta

def verInfos(conta: Conta) -> str:
    
    return f"""
{"=" * 40}
Titular: {conta.getTitular().getNome()}
Idade: {conta.getTitular().getIdade()}
CPF: {conta.getTitular().getCpf()}
{"=" * 40}
Número: {conta.getNum()} 
saldo em real: {conta.getSaldoReal()}
{"=" * 40}
"""
   
   
def efetuarTransacao(contaRemetente: Conta, contaDestino: Conta, valor: float) -> bool:
    removeu = contaRemetente.tirar(valor)
    if removeu:        
        recebeu = contaDestino.receber(valor)
        #TODO -> se a pessoa removeu o dinheiro e a outra não recebeu, retorne o dinheiro para a conta do remetente
    return removeu and recebeu
    