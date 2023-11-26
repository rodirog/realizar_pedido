from abc import ABC, abstractmethod


class Usuario:
    @abstractmethod
    def __init__(self, nome: str, cpf: str, telefone: int, municipio: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__municipio = municipio

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def telefone(self) -> int:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int):
        self.__telefone = telefone

    @property
    def municipio(self) -> str:
        return self.__municipio

    @municipio.setter
    def municipio(self, municipio: str):
        self.__municipio = municipio
