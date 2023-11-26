import pickle
from persistencia.abstractDAO import DAO
from entidade.consumidor import Consumidor


class ConsumidorDAO(DAO):
    def __init__(self):
        super().__init__("consumidores.pkl")

    def add(self, consumidor: Consumidor):
        if consumidor is not None and isinstance(consumidor, Consumidor):
            cpf = consumidor.cpf
            super().add(cpf, consumidor)

    # def get(self, cpf):
    #  try:
    #    for consumidor in self.get_all():
    #       if consumidor.cpf == cpf:
    #           return consumidor
    # except KeyError:
    #      pass
    #   return None

    def get(self, cpf: str):
        return super().get(cpf)

    def get_all(self):
        return super().get_all()

    def remove_by_cpf(self, cpf: str):
        for key, consumidor in self._DAO__cache.items():
            if consumidor.cpf == cpf:
                super().remove(key)
                return True
        return False

    def update(self):
        return super().update()
