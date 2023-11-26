from persistencia.abstractDAO import DAO
from entidade.produto import Produto


class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto: Produto):
        super().add(produto.id, produto)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)