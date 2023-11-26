from abc import abstractmethod
from entidade.usuario import Usuario


class Produtor(Usuario):
    abstractmethod

    def __init__(self, nome: str, cpf: str, telefone: int, municipio: str,
                 certificacao: str, cnpj: str, logradouro: str, numero_logradouro: int,
                 nome_fantasia: str, tipo_chave_pix: str, chave_pix: str):
        super().__init__(nome, cpf, telefone, municipio)
        self.__certificacao = certificacao
        self.__cnpj= cnpj
        self.__logradouro = logradouro
        self.__numero_logradouro = numero_logradouro
        self.__nome_fantasia = nome_fantasia
        self.__tipo_chave_pix = tipo_chave_pix
        self.__chave_pix = chave_pix
        self.__catalogo = []
        self.__feiras = []
        self.__id = None

    @property
    def id(self):
        return self.__id

    @property
    def certificacao(self):
        return self.__certificacao

    @certificacao.setter
    def certificacao(self, certificacao):
        self.__certificacao = certificacao

    @property
    def feiras(self):
        return self.__feiras

    @feiras.setter
    def feiras(self, feiras):
        self.__feiras = feiras

    @property
    def catalogo(self):
        return self.__catalogo

    @catalogo.setter
    def catalogo(self, catalogo):
        self.__catalogo = catalogo

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    @property
    def numero_logradouro(self):
        return self.__numero_logradouro

    @numero_logradouro.setter
    def numero_logradouro(self, numero_logradouro):
        self.__numero_logradouro = numero_logradouro

    @property
    def nome_fantasia(self):
        return self.__nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    @property
    def tipo_chave_pix(self):
        return self.__tipo_chave_pix

    @tipo_chave_pix.setter
    def tipo_chave_pix(self, tipo_chave_pix):
        self.__tipo_chave_pix = tipo_chave_pix

    @property
    def chave_pix(self):
        return self.__chave_pix

    @chave_pix.setter
    def chave_pix(self, chave_pix):
        self.__chave_pix = chave_pix