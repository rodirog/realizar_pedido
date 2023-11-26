from abc import abstractmethod
from entidade.usuario import Usuario


class Consumidor(Usuario):
    abstractmethod

    def __init__(self, nome: str, cpf: str, telefone: int, municipio: str):
        super().__init__(nome, cpf, telefone, municipio)
        self.__id = None

    @property
    def id(self) -> int:
        return self.__id
