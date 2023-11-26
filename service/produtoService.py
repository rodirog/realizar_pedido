from entidade.produto import Produto
from persistencia.produtoDAO import ProdutoDAO
#from entidade.unidadeMedidaEnum import UnidadeMedidaEnum


class ProdutoService:
    def __init__(self):
        self.__produtos = ProdutoDAO()

    def cadastrar_produto(self, nome: str, preco_un: float, quantidade: int, unidade_medida,
                          descricao, preco_desconto, qtd_desconto, id) -> Produto:
        produto = Produto()
        produto.nome = nome
        produto.preco_un = preco_un
        produto.quantidade = quantidade
        produto.unidade_medida = unidade_medida
        produto.descricao = descricao
        produto.preco_desconto = preco_desconto
        produto.qtd_desconto = qtd_desconto
        produto.id = id

        self.__produtos.add(produto)
        return produto

    def consultar_produto(self):
        catalogo_produtos = list()

        for produto in self.__produtos.get_all():
            catalogo_produtos.append({
                "nome": produto.nome,
                "descricao": produto.descricao,
                "preco_un": produto.preco_un,
                "qtd_disponivel": produto.qtd_disponivel,
                "unidade_medida": produto.unidade_medida
            })

        return catalogo_produtos

    def alterar_produto(self,
                        produto_id: int,
                        nome: str,
                        descricao: str,
                        preco_un: float,
                        qtd_disponivel: int,
                        qtd_desconto: int,
                        preco_desconto: float,
                        unidade_medida):
        for produto in self.__produtos.get_all():
            if produto.id == produto_id:
                produto.nome = nome
                produto.descricao = descricao
                produto.preco_un = preco_un
                produto.qtd_disponivel = qtd_disponivel
                produto.qtd_desconto = qtd_desconto
                produto.preco_desconto = preco_desconto
                produto.unidade_medida = unidade_medida
                return True
        return False

    def remover_produto(self, produto_id: int):
        self.__produtos.remove(self.__produtos.get(produto_id))