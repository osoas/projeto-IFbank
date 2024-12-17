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
        num = input(txt)
        if re.match(r"^\d{9}$",num):
            return num
        else:
            print("o número inserido não atende os padrões. Digite um numero de exatamente 9 digitos")


def getpassword(txt: str) -> str:
    while True:
        password = input(txt)
        if re.match(r'^?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%?&]{9}$', password):
            return password
        else:
            print(
                "Sua senha deve conter:\n"
                "  * Exatamente 9 caracteres\n"
                "  * Pelo menos uma letra MAIÚSCULA\n"
                "  * Pelo menos um número\n"
                "  * Pelo menos um caractere especial (!@#$%?&)\n"
            )



    


