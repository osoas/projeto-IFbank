from classPessoa import Pessoa
from gerarNum import gerarNum

class Conta:
    def __init__(self, titular: Pessoa, senha: str, saldoReal: float = 0, num: str = gerarNum()):
        self.__num = num
        self.__saldoReal = saldoReal
        self.__titular = titular
        self.__senha = senha

    def getNum(self) -> str:
        return self.__num
    
    def getTitular(self) -> Pessoa:
        return self.__titular

    def getSenha(self) -> str:
        return self.__senha    
    
    def getSaldoReal(self) -> float:
        return self.__saldoReal
    
    def __setSaldoReal(self, newValor: float) -> None:
        self.__saldoReal = newValor

    def tirar(self, valor: float) -> bool:
        saldoReal = self.getSaldoReal()
        if saldoReal - valor >=  0:
            self.__setSaldoReal(saldoReal - valor)
            return True
        return False
    
    def receber(self, valor: float) -> bool:
        self.__setSaldoReal(self.getSaldoReal() + valor)
        return True
    
    #método para adicionar dinheiro nas contas para testar funcionalidades 
    def peDeMeia(self) -> None:
        self.__setSaldoReal(self.getSaldoReal() + 200)
            
