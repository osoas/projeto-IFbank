from classes.personClass import Person
from firebase.config import db
class Account:
    def __init__(self, password: str, num: str, holderId: str, keys: list[str] = None, RealValue: float = 0, contacts: list[str] = []):
        self.__num = num
        self.__realValue = RealValue
        self.__holderId = holderId
        self.__password = password
        self.__keys = keys if keys is not None else [] 
        self.__isBlocked = False
        self.__contacts = contacts

    def getNum(self) -> str:
        return self.__num

    def getContacts(self) -> list[str]:
        return self.__contacts
    
    def getHolderId(self) -> Person:
        return self.__holderId

    def getPass(self) -> str:
        return self.__password    
    
    def getKey(self, index: int) -> str:
        return self.__keys[index]
    
    def getKeys(self) -> list[str]:
        return self.__keys
    
    def getRealValue(self) -> float:
        return self.__realValue
    
    def getStatus(self) -> bool:
        return self.__isBlocked
    
    def __setStatus(self, value: bool) -> None:
        
        self.__isBlocked = value
        
        
    def blockAccount(self) -> None:
        self.__setStatus(True) 
        account_ref = db.collection("accounts").document(self.getNum())
        account_ref.update({
            "isBlocked": True 
        })
    
    def addKey(self, key: str)  -> bool:
        if not key in self.getKeys():
            self.__keys.append(key)
            return True
        return False
    
    #TODO -> validação da senha está sendo feita com getPass, não pode haver um getPass público, por isso: fazer método de verificação de senha dentro da classe Account
    
    
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
    
    def attAccount(self) -> None:
        account_ref = db.collection("accounts").document(self.getNum()) 
        account_data = account_ref.get().to_dict() 
        
        if account_data:
            self.__realValue = account_data.get("realValue", self.__realValue)
            self.__keys = account_data.get("keys", self.__keys)
            self.__contacts = account_data.get("contacts", self.__contacts)
            self.__isBlocked = account_data.get("isBlocked", self.__isBlocked, 0)
            print(f"Conta {self.getNum()} atualizada com sucesso!")
        else:
            print(f"Conta {self.getNum()} não encontrada no Firebase.")
