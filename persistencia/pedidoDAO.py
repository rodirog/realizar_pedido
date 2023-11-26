from persistencia.abstractDAO import DAO
from entidade.pedido import Pedido
from entidade.produtor import Produtor


class PedidoDAO(DAO):
    def __init__(self):
        super().__init__('pedidos.pkl')

    def add(self, pedido: Pedido):
        if pedido is not None:
            id = pedido.id
            super().add(id, pedido)

    def get(self, id: int):
        return super().get(id)

    def update(self):
        return super().update()

    def getByProdutor(self, produtor: Produtor):
        pedidos = super().get_all()  # Use o método get_all da instância do DAO
        pedidos_filtrados = []
        for pedido in pedidos:
            if pedido.produtor.cpf == produtor.cpf:
                pedidos_filtrados.append(pedido)
        return pedidos_filtrados

    def get_all(self):
        pedidos = super().get_all()
        print("Pedidos no cache:")
        for pedido in pedidos:
            print(pedido.produtor.nome)  # ou outra informação relevante
        return pedidos