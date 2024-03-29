from datetime import date

from utils.helper import date_para_str, str_para_date


class Cliente:
    contador: int = 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__email: str = email
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> str:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def data_nascimento(self: object) -> str:
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self: object) -> str:
        return date_para_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return f'Código: {self.codigo} \n' \
               f'Nome: {self.nome} \n' \
               f'Data de nascimento: {self.data_nascimento} \n' \
               f'Cadastro: {self.data_cadastro}'
