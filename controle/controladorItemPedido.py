from controle.controladorProduto import ControladorProduto
from limite.telaItemPedido import TelaItemPedido


class ControladorItemPedido():
    def __init__(self):
        self.__tela_item_pedido = TelaItemPedido()
        self.__controlador_produto = ControladorProduto()

    def iniciar(self):
        self.mostrar_tela_opcoes()

    def mostrar_tela_opcoes(self):
        opcoes = {1: self.incluir_item,
                  2: self.listar_itens}

        while True:
            opcao = self.__tela_item_pedido.tela_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()

    def incluir_item(self):
        #ja_existe = False
        self.__controlador_produto.listar_produtos()
        try:
            dados_item = self.__tela_item_pedido.pegar_dados_item()
        except ValueError:
            self.__tela_item.mostrar_mensagem("Cadastro nao efetuado. \
                                                Houve um erro na inserção dos dados!")
            self.__tela_feira.close()
            return

        if dados_item:

            produto = self.__controlador_produto.pega_produto_por_id(dados_item["id_produto_item"])
            dados_item["produto_item"] = produto

            #for feira in self.__feira_dao.get_all():

            #    if dados_feira["id_feira"] == feira.id:
            #        self.__tela_feira.mostrar_mensagem("Uma feira com este id já existe!")
            #        ja_existe = True

            #if not ja_existe:

            return dados_item
                #feira = Feira(dados_feira["dias_semana_feira"],
                #                         dados_feira["id_feira"],
                #                         dados_feira["municipio_feira"],
                #                         dados_feira["logradouro_feira"],
                #                         dados_feira["numero_logradouro_feira"])

                #self.__feira_dao.add(feira)
                #self.__tela_feira.mostrar_mensagem("Feira inclusa com sucesso!")

    def listar_feiras(self):
        dados_feiras = []
        feiras = self.__feira_dao.get_all()

        for feira in feiras:
            dados_feiras.append({"id_feira": feira.id,
                                   "dias_semana_feira": feira.dias_semana,
                                   "municipio_feira": feira.municipio,
                                   "logradouro_feira": feira.logradouro,
                                   "numero_logradouro_feira": feira.numero_logradouro})

        self.__tela_feira.listar_feiras(dados_feiras)