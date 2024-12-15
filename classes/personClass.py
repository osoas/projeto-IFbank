class Person:
    def __init__(self, name: str, age: int, cpf: str):
        self.__cpf = cpf
        self.__name = name
        self.__age = age
        
    def getCpf(self) -> str:
        return self.__cpf

    def getName(self) -> str:
        return self.__name
    
    def getAge(self) -> int:
        return self.__age
    

