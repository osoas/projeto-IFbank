

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

def getMenuLogin() -> str:
    return """
========================================
            Como deseja logar
========================================
1. CPF titular
2. Número da conta
========================================
    """
def getMenuLogado() -> str:
    return """
========================================
          O que deseja fazer?
========================================
1. Ver informações
2. Realizar pix
3. Cadastrar pix
4. Contantos salvos
5. pédimea
5. Sair
========================================
    """
    
def getMenuTransacao() -> str:
    return """
========================================
     Qual tipo de chave irá inserir
========================================
1. CPF 
2. Número da conta
3. Chave aleatória --- TODO
========================================
    """

def printLine() -> None:
    print("=" * 40)