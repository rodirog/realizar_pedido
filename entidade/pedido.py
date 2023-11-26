from entidade.produtor import Produtor
import random
import string

# from entidade.consumidor import Consumidor

class Pedido:
    def __init__(self, id:int, preco_total: float, produtor: Produtor):
        self.__produtor = produtor
        #self.__consumidor = consumidor
        self.__id = id
        self.__produtor = produtor
        self.__situacao_pedido = None
        self.__itens = []
        self.__preco_total = preco_total
        self.__feira = None

    @property
    def produtor(self):
        return self.__produtor

    @produtor.setter
    def produtor(self, produtor: Produtor):
        if (isinstance(produtor, Produtor)):
            self.__produtor = produtor

    #@property
    #def consumidor(self):
    #    return self.__consumidor

    #@consumidor.setter
    #def consumidor(self, consumidor: Consumidor):
    #    if (isinstance(consumidor, Consumidor)):
    #        self.__consumidor = consumidor

    @property
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, itens: []):
        self.__itens = itens

    @property
    def feira(self):
        return self.__feira

    @feira.setter
    def feira(self, feira):
        self.__feira = feira

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def situacao_pedido(self):
        return self.__situacao_pedido

    @situacao_pedido.setter
    def situacao_pedido(self, situacao_pedido: str):
        self.__situacao_pedido = situacao_pedido

    @property
    def preco_total(self):
        return self.__preco_total

    @preco_total.setter
    def preco_total(self, preco_total):
        self.__preco_total = preco_total
