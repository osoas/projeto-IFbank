class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade
        
    def getCpf(self) -> str:
        return self.__cpf

    def getNome(self) -> str:
        return self.__nome
    
    def getIdade(self) -> int:
        return self.__idade
    

