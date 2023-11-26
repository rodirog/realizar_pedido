from limite.telaSistema import TelaSistema
from controle.controladorProdutor import ControladorProdutor
from controle.controladorFeira import ControladorFeira
from controle.controladorProduto import ControladorProduto
from controle.controladorPedido import ControladorPedido
from controle.controladorItemPedido import ControladorItemPedido

class ControladorSistema:

    def __init__(self):
        self.__controlador_feira = ControladorFeira()
        self.__controlador_produto = ControladorProduto()
        self.__controlador_item_pedido = ControladorItemPedido()
        self.__controlador_produtor = ControladorProdutor(self, self.__controlador_feira)
        self.__controlador_pedido = ControladorPedido(self.__controlador_item_pedido,
                                                      self.__controlador_produtor)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_produtor(self):
        return self.__controlador_produtor

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_produtores(self):
        self.__controlador_produtor.abre_tela()

    def cadastra_produtos(self):
        self.__controlador_produto.show_produto_view()

    def cadastro_pedidos(self):
        self.__controlador_pedido.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {3: self.cadastro_pedidos, 2: self.cadastra_produtos, 1: self.cadastra_produtores, 0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()