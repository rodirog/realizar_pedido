#from entidade.unidadeMedidaEnum import UnidadeMedidaEnum


class Produto:
    def __init__(self):
        __id: int
        __nome: str
        __descricao: str
        __preco_un: float
        __quantidade: int
        __qtd_desconto: int
        __preco_desconto: float
        __unidade_medida: str

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: str) -> None:
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self.__descricao = descricao

    @property
    def preco_un(self) -> float:
        return self.__preco_un

    @preco_un.setter
    def preco_un(self, preco_un: float) -> None:
        self.__preco_un = preco_un

    @property
    def qtd_disponivel(self) -> int:
        return self.__qtd_disponivel

    @qtd_disponivel.setter
    def qtd_disponivel(self, qtd_disponivel: int) -> None:
        self.__qtd_disponivel = qtd_disponivel

    @property
    def qtd_desconto(self) -> int:
        return self.__qtd_desconto

    @qtd_desconto.setter
    def qtd_desconto(self, qtd_desconto: int) -> None:
        self.__qtd_desconto = qtd_desconto

    @property
    def preco_desconto(self) -> float:
        return self.__preco_desconto

    @preco_desconto.setter
    def preco_desconto(self, preco_desconto: float) -> None:
        self.__preco_desconto = preco_desconto

    @property
    def unidade_medida(self):
        return self.__unidade_medida

    @unidade_medida.setter
    def unidade_medida(self, unidade_medida) -> None:
        self.__unidade_medida = unidade_medida