from persistencia.abstractDAO import DAO
from entidade.produtor import Produtor


class ProdutorDAO(DAO):
    def __init__(self):
        super().__init__('produtores.pkl')

    def add(self, produtor: Produtor):
        if produtor is not None:  # \
            # and isinstance(produtor, Produtor) \
            # and isinstance(produtor.id, int):
            cpf = produtor.cpf
            super().add(cpf, produtor)

    def get(self, cpf: str):
        return super().get(cpf)

    def remove_by_cpf(self, cpf: str):
        for key, produtor in self._DAO__cache.items():
            if produtor.cpf == cpf:
                super().remove(key)
                return True
        return False

    def update(self):
        return super().update()

    def get_all(self):
        return super().get_all()