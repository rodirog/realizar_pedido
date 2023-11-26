#from entidade.unidadeMedidaEnum import UnidadeMedidaEnum
from service.produtoService import ProdutoService
from limite.telaProduto import ProdutoView
from persistencia.produtoDAO import ProdutoDAO
from entidade.produto import Produto


class ControladorProduto:
    def __init__(self):
        self.__produto_service = ProdutoService()
        self.__produto_view = ProdutoView()
        self.__produto_dao = ProdutoDAO()

    def pega_produto_por_id(self, id):
        #IMPORTANTE MUDAR ISSO DPS
        produto = self.__produto_dao.get(id)
        return produto

    def show_produto_view(self):
        opcoes = {
            1: self.cadastrar_produto,
            2: self.consultar_produto,
            3: self.alterar_produto,
            4: self.remover_produto,
            5: self.listar_produtos
        }
        while True:
            opcoes[self.__produto_view.mostra_opcoes()]()

    def cadastrar_produto(self):
        produto = self.__produto_view.cadastrar_produto()

        produto_novo = Produto()
        produto_novo.nome = produto['nome']
        produto_novo.preco_un = produto['preco_un']
        produto_novo.quantidade = produto['quantidade']
        produto_novo.unidade_medida = produto['unidade_medida']
        produto_novo.descricao = produto['descricao']
        produto_novo.preco_desconto = produto['preco_desconto']
        produto_novo.qtd_desconto = produto['qtd_desconto']
        produto_novo.id = produto['id']

        self.__produto_dao.add(produto_novo)
        #return produto

    def consultar_produto(self):
        return self.__produto_view.consultar_produto(self.__produto_service.consultar_produto())

    def listar_produtos(self):

        dados_produtos = []

        for produto in self.__produto_dao.get_all():
            dados_produtos.append({"id_produto": produto.id,
                                   "nome_produto": produto.nome,
                                   "descricao_produto": produto.descricao,
                                   "preco_desconto_produto": produto.preco_desconto,
                                   "preco_un_produto": produto.preco_un,
                                   "qtd_desconto_produto": produto.qtd_desconto,
                                   "quantidade_produto": produto.quantidade,
                                   "unidade_medida_produto": produto.unidade_medida})
        self.__produto_view.listar_produtos(dados_produtos)

    def alterar_produto(self):
        produto = self.__produto_view.alterar_produto()
        if isinstance(produto['produto_id'], int) \
                and isinstance(produto['nome'], str) \
                and isinstance(produto['descricao'], str) \
                and isinstance(produto['preco_un'], float) \
                and isinstance(produto['qtd_disponivel'], int) \
                and isinstance(produto['preco_desconto'], float) \
                and isinstance(produto['unidade_medida'], UnidadeMedidaEnum):
            return self.__produto_service.alterar_produto(
                produto['produto_id'],
                produto['nome'],
                produto['descricao'],
                produto['preco_un'],
                produto['qtd_disponivel'],
                produto['qtd_desconto'],
                produto['preco_desconto'],
                produto['unidade_medida']
            )

    def remover_produto(self):


        produto = self.__produto_view.remover_produto()

        return self.__produto_service.remover_produto(produto['produto_id'])

        #id_produto = self.__produto_view.remover_produto()
        #produto = self.__produto_dao.get(id_produto)

        #dados_produto = []
        #dados_produto.append({"id_produto": produto.id,
        #                       "nome_produto": produto.nome,
        #                       "descricao_produto": produto.descricao,
        #                       "preco_desconto_produto": produto.preco_desconto,
        #                       "preco_un_produto": produto.preco_un,
        #                       "qtd_desconto_produto": produto.qtd_desconto,
        #                       "quantidade_produto": produto.quantidade,
        #                       "unidade_medida_produto": produto.unidade_medida})
        #self.__produto_view.listar_produtos(dados_produto)
