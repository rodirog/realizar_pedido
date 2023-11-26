from limite.telaConsumidor import TelaConsumidor
from entidade.consumidor import Consumidor
from persistencia.consumidorDAO import ConsumidorDAO


class ControladorConsumidores:
    def __init__(self, controlador_sistema):
        self.__consumidor_dao = ConsumidorDAO()
        # self.__consumidores = []
        #self.__ultimo_id = 0
        self.__tela_consumidor = TelaConsumidor()
        self.__controlador_sistema = controlador_sistema

    def pega_consumidor_por_cpf(self, cpf: str):
        consumidor = self.__consumidor_dao.get(cpf)
        return consumidor


    def incluir_consumidor(self):
        dados_consumidor = self.__tela_consumidor.dados_cadastro_consumidor()
        #self.__ultimo_id += 1
        cpf = dados_consumidor["cpf"]
        consumidor_existente = self.__consumidor_dao.get(cpf)
        if consumidor_existente is not None:
            self.__tela_consumidor.mostra_mensagem(
                "CPF já cadastrado. Não é possível cadastrar novamente."
            )
            return
        consumidor = Consumidor(
            nome=dados_consumidor["nome"],
            telefone=dados_consumidor["telefone"],
            cpf=dados_consumidor["cpf"],
            municipio=dados_consumidor["municipio"],
        )
        self.__consumidor_dao.add(consumidor)

    def alterar_consumidor(self):  # ver se vai funcionar
        self.lista_consumidores()
        cpf_consumidor = self.__tela_consumidor.seleciona_consumidor()
        consumidor = self.pega_consumidor_por_cpf(cpf_consumidor)

        if consumidor is not None:
            novos_dados_consumidor = self.__tela_consumidor.altera_dados_consumidor(
                cpf_consumidor
            )
            consumidor.nome = novos_dados_consumidor["nome"]
            consumidor.telefone = novos_dados_consumidor["telefone"]
            consumidor.municipio = novos_dados_consumidor["municipio"]
            self.__consumidor_dao.update()
            self.lista_consumidores()
        else:
            self.__tela_consumidor.mostra_mensagem("ATENÇÃO: Consumidor não existente")

    def lista_consumidores(self):
        dados_consumidores = []
        for consumidor in self.__consumidor_dao.get_all():
            dados_consumidores.append(
                {
                    "nome": consumidor.nome,
                    "telefone": consumidor.telefone,
                    "cpf": consumidor.cpf,
                    "municipio": consumidor.municipio,
                }
            )
        self.__tela_consumidor.mostra_consumidor(dados_consumidores)

    def excluir_consumidor(self):
        self.lista_consumidores()
        cpf_consumidor = self.__tela_consumidor.seleciona_consumidor()

        if self.__consumidor_dao.remove_by_cpf(cpf_consumidor):
            self.lista_consumidores()
        else:
            self.__tela_consumidor.mostra_mensagem("ATENÇÃO: Consumidor não existe")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_consumidor,
            2: self.alterar_consumidor,
            3: self.lista_consumidores,
            4: self.excluir_consumidor,
            0: self.retornar,
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_consumidor.tela_opcoes()]()
