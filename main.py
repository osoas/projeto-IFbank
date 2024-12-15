from funcoesMenu import getMenu, getMenuLogado, printLine, getMenuTransacao
from funcoesGet import getOption, getFloat, getCpf
from funcoes import criar_conta, realizar_login
from funcoesLogado import efetuarTransacao, verInfos
from buscas import buscar_conta_por_cpf, buscar_conta_por_num

from classConta import Conta
from classPessoa import Pessoa

# Variáveis globais
from globais import contas, pessoas
contaLogada = False

#TODO -> criar class transação
#TODO -> cada transação deve ser uma instancia da class Transação
#TODO -> guardar o histórico de transações

osoas = Pessoa("osoas", 23, "123")
roni = Pessoa("roni", 50, "999")
pessoas.append(osoas)
pessoas.append(roni)


contas.append(Conta(osoas, "123"))
contas.append(Conta(roni, "123"))


def main() -> None:
    global contaLogada
    
    while True:
        option = getOption(getMenu(), [1, 2, 0])

        if option == 1:
            criar_conta()
            input()
    
        if option == 2:
            contaLogada = realizar_login()
            input()
            break
            
        if option == 0:
            printLine()
            print("Obrigado por usar o IFbank!")
            return

    while True:
        option = getOption(getMenuLogado(), [1, 2, 3, 4, 5, 6])
        if option == 1:
            print(verInfos(contaLogada))
            input()
        
        if option == 2:
            #TODO -> salvar os contatos 
            optionTransacao = getOption(getMenuTransacao(), [1, 2, 3])
            contaDestino = False     
            
            if optionTransacao == 1:
                cpfDestino = getCpf("Insira o cpf da conta destino: ")
                contaDestino = buscar_conta_por_cpf(cpfDestino)
            if optionTransacao == 2:
                numDestino = input("Insira o numero da conta destino: ")
                contaDestino = buscar_conta_por_num(numDestino)
                
            valor = getFloat("insira o valor da transação: ")
            efetuarTransacao(contaLogada, contaDestino, valor)
        if option == 3:
            #TODO -> cadastro de chave pix nova
            return
        if option == 4:
            #TODO -> ver os contatos salvos para efetuar pix rápidamente
            return
        if option == 5:
            contaLogada.peDeMeia()    
        
        if option == 6:
            contaLogada = False
            main()
            
        # 1 ver infos 
        # 2 realizar transação 
        # 3 cadastrar pix TODO
        # 4 contatos salvos TODO
        # 5 pé de meia
        # 6 sair da conta
        
        
        

main()
