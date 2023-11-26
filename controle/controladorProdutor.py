from persistencia.produtorDAO import ProdutorDAO
from limite.telaProdutor import TelaProdutor
from entidade.produtor import Produtor
from controle.controladorFeira import ControladorFeira
from entidade.feira import Feira


class ControladorProdutor():

    def __init__(self, controlador_sistema, controlador_feira):
        self.__produtor_dao = ProdutorDAO()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_feira = controlador_feira
        self.__tela_produtor = TelaProdutor()

    def pega_produtor_por_id(self, id: int):
        #IMPORTANTE MUDAR ISSO DPS
        id = str(id)
        produtor = self.__produtor_dao.get(id)
        return produtor

    def incluir_produtor(self):
        dados_produtor = self.__tela_produtor.pega_dados_produtor()
        produtor = self.pega_produtor_por_id(dados_produtor["cpf"])
        try:
            if produtor == None:
                produtor = Produtor(
                    dados_produtor["nome"], dados_produtor["cpf"],
                    dados_produtor["telefone"], dados_produtor["municipio"],
                    dados_produtor["certificacao"], dados_produtor["cnpj"],
                    dados_produtor["logradouro"], dados_produtor["numero_logradouro"],
                    dados_produtor["nome_fantasia"], dados_produtor["tipo_chave_pix"], dados_produtor["chave_pix"])
                self.__produtor_dao.add(produtor)
            else:
                raise KeyError
        except KeyError:
            self.__tela_produtor.mostra_mensagem(
                "Já existe um produtor vinculado a esse CPF")

    def incluir_feira(self):
        self.lista_produtores()
        cpf_produtor = self.__tela_produtor.seleciona_produtor()
        produtor = self.pega_produtor_por_id(cpf_produtor)
        dados_feira = self.__controlador_feira.incluir_feira()

        feira = Feira(dados_feira["dias_semana_feira"],
                                 dados_feira["id_feira"],
                                 dados_feira["municipio_feira"],
                                 dados_feira["logradouro_feira"],
                                 dados_feira["numero_logradouro_feira"])

        #self.__controlador_feira.feira_dao.add(feira)
        produtor.feiras.append(feira)
        self.__produtor_dao.update()
        self.__tela_produtor.mostra_mensagem("Feira inclusa com sucesso!")

    def lista_produtores(self):
        dados_produtores = []
        try:
            if len(self.__produtor_dao.get_all()) == 0:
                raise KeyError
            else:
                for produtor in self.__produtor_dao.get_all():
                    dados_produtores.append(
                        {"nome": produtor.nome, "cpf": produtor.cpf, "telefone": produtor.telefone,
                         "municipio": produtor.municipio, "certificacao": produtor.certificacao,
                         "cnpj": produtor.cnpj, "logradouro": produtor.logradouro,
                         "numero_logradouro": produtor.numero_logradouro, "nome_fantasia": produtor.nome_fantasia,
                         "tipo_chave_pix": produtor.tipo_chave_pix, "chave_pix": produtor.chave_pix,
                         "feiras": produtor.feiras})
                self.__tela_produtor.mostra_produtor(dados_produtores)
        except KeyError:
            self.__tela_produtor.mostra_mensagem(
                "Ainda não há produtores cadastrados!")

    def alterar_produtor(self):
        self.lista_produtores()
        cpf_produtor = self.__tela_produtor.seleciona_produtor()
        produtor = self.pega_produtor_por_cpf(cpf_produtor)

        try:
            if (produtor is not None):
                novos_dados_produtor = self.__tela_produtor.altera_dados_produtor(cpf_produtor)
                produtor.nome = novos_dados_produtor["nome"]
                produtor.telefone = novos_dados_produtor["telefone"]
                produtor.municipio = novos_dados_produtor["municipio"]
                produtor.certificacao = novos_dados_produtor["certificacao"]
                produtor.logradouro = novos_dados_produtor["logradouro"]
                produtor.numero_logradouro = novos_dados_produtor["numero_logradouro"]
                produtor.nome_fantasia = novos_dados_produtor["nome_fantasia"]
                produtor.tipo_chave_pix = novos_dados_produtor["tipo_chave_pix"]
                produtor.chave_pix = novos_dados_produtor["chave_pix"]
                self.__produtor_dao.update()
                self.lista_produtores()
            else:
                raise KeyError
        except KeyError:
            self.__tela_produtor.mostra_mensagem(
                "ATENÇÃO: Produtor não existente")

    def excluir_produtor(self):
        self.lista_produtores()
        cpf_produtor = self.__tela_produtor.seleciona_produtor()

        try:
            if self.__produtor_dao.remove_by_cpf(cpf_produtor):
                self.lista_produtores()
            else:
                raise KeyError
        except KeyError:
            self.__tela_produtores.mostra_mensagem(
                "ATENÇÃO: Produtor não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_produtor, 2: self.lista_produtores, 3: self.alterar_produtor,
                        4: self.excluir_produtor, 5: self.incluir_feira, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_produtor.tela_opcoes()]()