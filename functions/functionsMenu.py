

def getMenu() -> str:
    return """
========================================
            Bem-vindo ao IFbank
========================================
1. Criar Conta
2. Logar
0. Finalizar
========================================
"""

def getLoginMenu() -> str:
    return """
========================================
            Como deseja logar
========================================
1. CPF titular
2. Número da conta
========================================
    """
def getLoggedMenu() -> str:
    return """
========================================
          O que deseja fazer?
========================================
1. Ver informações
2. Realizar pix
3. Cadastrar pix
4. Contatos salvos
5. pédimea
6. Sair
7. Realizar depósito
========================================
    """
    
def getTransactionMenu() -> str:
    return """
========================================
     Qual tipo de chave irá inserir
========================================
1. CPF 
2. Número da conta
3. Outro
========================================
    """

def getNewKeyMenu() -> str:
    return """
========================================
    Escolha um chave para adicionar
========================================
1. CPF 
2. Número da conta
3. Chave aleatória --- TODO
4. Email
========================================
    """

def printLine() -> None:
    print("=" * 40)
