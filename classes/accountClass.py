from classes.personClass import Person
from functions.generates import generateNum

class Account:
    def __init__(self, holder: Person, password: str, RealValue: float = 0, num: str = generateNum(), keys: list[str] = None):
        self.__num = num
        self.__realValue = RealValue
        self.__holder = holder
        self.__password = password
        self.__keys = keys if keys is not None else [] 

    def getNum(self) -> str:
        return self.__num
    
    def getHolder(self) -> Person:
        return self.__holder

    def getPass(self) -> str:
        return self.__password    
    
    def getKey(self, index: int) -> str:
        return self.__keys[index]
    
    def getKeys(self) -> list[str]:
        return self.__keys
    
    def addKey(self, key: str)  -> bool:
        if not key in self.getKeys():
            self.__keys.append(key)
            return True
        return False
    #TODO -> validação da senha está sendo feita com getPass, não pode haver um getPass público, por isso, fazer método de verificação de senha dentro da classe Account
    
    def getRealValue(self) -> float:
        return self.__realValue
    
    def __setRealValue(self, newValue: float) -> None:
        self.__realValue = newValue

    def take(self, value: float) -> bool:
        realValue = self.getRealValue()
        if realValue - value >=  0:
            self.__setRealValue(realValue - value)
            return True
        return False
    
    def receive(self, value: float) -> bool:
        self.__setRealValue(self.getRealValue() + value)
        return True
    
    #método para adicionar dinheiro nas contas para testar funcionalidades 
    def peDeMeia(self) -> None:
        self.__setRealValue(self.getRealValue() + 200)
            
