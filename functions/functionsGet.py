import re

def getOption(txt: str, validOptions: list[int]) -> int:
    while True:
        print(txt)
        try:
            option = int(input())
            if option in validOptions:
                return option
            else:
                print("Essa opção não existe.")
        except ValueError:
            print("Valor incorreto. Digite um número válido.")

def getAge(txt: str) -> int:
    while True:
        try:
            num = int(input(txt))
            if num >= 18:
                return num
            else:
                print("Apenas maiores de 18 anos são aceitos.")
        except ValueError:
            print("Valor incorreto. Digite uma idade válida.")
            
def getFloat(txt: str) -> float:
    while True:
        try:
            valor = float(input(txt))
            return valor
        except ValueError:
            print("Valor incorreto. Digite um valor válido.")






def getCpf(txt: str) -> str:
    while True:
        cpf = input(txt)
        if re.match(r"^\d{11}$", cpf):
            return cpf
        else:
            print("cpf incorreto. Digite um cpf válido")
     

def getNum(txt: str) -> str:
    while True:
        Num = input(txt)
        if re.match(r"^\d{9}$",Num):
            return Num
        else:
            print("o Numero de verificaçao incorreto.Digite um numero valido")


def getpassword(txt: str) -> str:
    while True:
        password = input(txt)
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%?&]{4}$', password):
            return password
        else:
            print(
                "Sua senha deve conter:\n"
                "  * Exatamente 11 caracteres\n"
                "  * Pelo menos uma letra MAIÚSCULA\n"
                "  * Pelo menos um número\n"
                "  * Pelo menos um caractere especial (!@#$%?&)\n"
            )


    


