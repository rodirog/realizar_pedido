from limite.telaPedido import TelaPedido
from entidade.pedido import Pedido
from entidade.produtor import Produtor
from entidade.itemPedido import ItemPedido
from persistencia.pedidoDAO import PedidoDAO
from controle.controladorProduto import ControladorProduto


class ControladorPedido():

    def __init__(self, controlador_item_pedido, controlador_produtor):
        #self.__controlador_sistema = controlador_sistema
        self.__tela_pedido = TelaPedido()
        self.__pedido_dao = PedidoDAO()
        self.__produtor = Produtor
        self.__controlador_item_pedido = controlador_item_pedido
        self.__controlador_produtor = controlador_produtor

    def pega_pedido_por_id(self, id):
        pedido = self.__pedido_dao.get(id)
        return pedido

    def selecionar_pedido(self):
        id = self.__tela_pedido.seleciona_pedido()
        return id

    def realizar_pedido(self):
        id = self.selecionar_pedido()
        pedido = self.__pedido_dao.get(id)
        dados_feiras = []
        dados_propriedade = []

        dados_itens = []
        for item in pedido.itens:
            dados_itens.append({"nome_produto": item.produto.nome,
                                "quantidade_produto": item.quantidade})

        preco_total = pedido.preco_total
        nome_produtor = pedido.produtor.nome

        feiras = pedido.produtor.feiras
        municipio_propriedade = pedido.produtor.municipio
        logradouro_propriedade = pedido.produtor.logradouro
        numero_propriedade = pedido.produtor.numero_logradouro
        endereco_propriedade = municipio_propriedade + "," + logradouro_propriedade + "," + numero_propriedade

        for feira in feiras:
            for dia_semana in feira.dias_semana:
                dados_feiras.append({"id": feira.id,
                                       "dia_semana": dia_semana,
                                       "municipio": feira.municipio,
                                       "logradouro": feira.logradouro,
                                       "numero_logradouro": feira.numero_logradouro})

        while True:
            local = self.__tela_pedido.selecionar_local(dados_feiras, endereco_propriedade)

            while local == 0:
                local = self.__tela_pedido.selecionar_local(dados_feiras, endereco_propriedade)

            if local != endereco_propriedade and local != None:
                local = ', '.join(map(str, local))
                pedido.feira = local

            revisou = self.__tela_pedido.mostrar_revisao_pedido(dados_itens, preco_total, local, nome_produtor)

            if revisou:
                pedido.situacao_pedido = "aguardando_pagamento"
                dados_pagamento = {"chave_pix": pedido.produtor.chave_pix,
                                   "tipo_chave": pedido.produtor.tipo_chave_pix,
                                   "nome_produtor": nome_produtor,
                                   "preco_total": preco_total}
                self.__tela_pedido.realizar_pagamento(dados_pagamento)
                self.__pedido_dao.update()
                break

    def incluir_pedido(self):
        try:
            dados_pedido = self.__tela_pedido.pegar_dados_pedido()
        except ValueError:
            self.__tela_pedido.mostrar_mensagem("Cadastro nao efetuado. \
                                                   Houve um erro na inserção dos dados!")
            self.__tela_pedido.close()
            return

        if dados_pedido:
            produtor = self.__controlador_produtor.pega_produtor_por_id(dados_pedido["id_produtor"])
            dados_pedido["produtor"] = produtor

            pedido = Pedido(dados_pedido["id_pedido"],
                          dados_pedido["preco_total_pedido"],
                          dados_pedido["produtor"])

            self.__pedido_dao.add(pedido)
            self.__tela_pedido.mostra_mensagem("Pedido incluso com sucesso!")

    def incluir_item(self):
        #self.lista_pedidos()
        id_pedido = self.__tela_pedido.seleciona_pedido()
        pedido = self.pega_pedido_por_id(id_pedido)
        dados_item = self.__controlador_item_pedido.incluir_item()

        item = ItemPedido(dados_item["id_item"],
                                 dados_item["produto_item"],
                                 dados_item["quantidade_item"])

        #self.__controlador_feira.feira_dao.add(feira)
        pedido.itens.append(item)
        self.__pedido_dao.update()
        self.__tela_pedido.mostra_mensagem("Item incluso com sucesso!")

    def lista_pedidos(self):

        if produtor is None:
            raise AttributeError("O produtor passado como parâmetro não é válido!")

        dados_pedidos = []
        try:
            if len(self.__dao_pedido.get_all()) == 0:
                raise KeyError
            else:
                for pedido in self.__dao_pedido.get_all():
                    if pedido.produtor == produtor:
                        dados_pedidos.append(
                            {
                                "produtor": pedido.produtor.nome,
                                "codigo": pedido.codigo,
                                "status": pedido.status,
                                "produtos": pedido.produtos,
                            }
                        )
                self.__tela_pedido.mostra_pedido(dados_pedidos)
        except KeyError:
            self.__tela_pedido.mostra_mensagem(
                "Ainda não há pedidos cadastrados!")

    def confirma_pagamento(self):
        # Solicite o código do pedido na tela de pedido
        codigo_pedido = self.__tela_pedido.tela_informa_codigo_pedido()

        # Recupere o pedido a partir do código
        pedido = self.__dao_pedido.get(codigo_pedido)

        if pedido is not None:
            # Altere o status do pedido para "aguardando entrega"
            pedido.status = "aguardando entrega"
            # Atualize o pedido no banco de dados (ou onde quer que esteja armazenado)
            self.__dao_pedido.update(pedido)
            self.__tela_pedido.mostra_mensagem(
                "Pagamento confirmado. Status do pedido alterado para 'aguardando entrega'.")
        else:
            self.__tela_pedido.mostra_mensagem("Pedido não encontrado. Verifique o código informado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        while True:
            opcao = self.__tela_pedido.tela_opcoes()
            if opcao == 1:
                #produtor = self.__controlador_sistema.controlador_produtor.pega_produtor_por_cpf(
                #    self.__tela_pedido.tela_login())
                self.incluir_pedido()

            elif opcao == 2:
                #produtor = self.__controlador_sistema.controlador_produtor.pega_produtor_por_cpf(
                #    self.__tela_pedido.tela_login())
                #self.lista_pedidos(produtor)
                pass
            elif opcao == 3:
                self.confirma_pagamento()
            elif opcao == 4:
                self.incluir_item()
            elif opcao == 5:
                self.realizar_pedido()
            elif opcao == 0:
                self.retornar()
            else:
                print("Opção inválida.")