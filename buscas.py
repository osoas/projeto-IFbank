from classConta import Conta
from globais import pessoas, contas

def buscar_conta_por_cpf(cpf: str) -> Conta | None:
    for pessoa in pessoas:
        if cpf == pessoa.getCpf():
            for conta in contas:
                if conta.getTitular() == pessoa:
                    return conta
    return None

def buscar_conta_por_num(num: str) -> Conta | None:
    for conta in contas:
        if num == conta.getNum():
            return conta
    return None