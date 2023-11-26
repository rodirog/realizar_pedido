import PySimpleGUI as sg


class TelaProdutor():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- PRODUTORES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Produtor', "RD1", key='1')],
            [sg.Radio('Listar Produtores', "RD1", key='2')],
            [sg.Radio('Alterar Produtor', "RD1", key='3')],
            [sg.Radio('Excluir Produtor', "RD1", key='4')],
            [sg.Radio('Incluir Feira', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Produtores').Layout(layout)

    def pega_dados_produtor(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- DADOS PRODUTOR ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Text('Município:', size=(15, 1)), sg.InputText('', key='municipio')],
            [sg.Text('Certificação:', size=(15, 1)), sg.InputText('', key='certificacao')],
            [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
            [sg.Text('Logradouro:', size=(15, 1)), sg.InputText('', key='logradouro')],
            [sg.Text('Numero do logradouro:', size=(15, 1)), sg.InputText('', key='numero_logradouro')],
            [sg.Text('Nome fantasia:', size=(15, 1)), sg.InputText('', key='nome_fantasia')],
            [sg.Text('Tipo chave pix:', size=(15, 1)), sg.InputText('', key='tipo_chave_pix')],
            [sg.Text('Chave pix:', size=(15, 1)), sg.InputText('', key='chave_pix')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de produtores').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        telefone = values['telefone']
        municipio = values['municipio']
        certificacao = values['certificacao']
        cnpj = values['cnpj']
        logradouro = values['logradouro']
        numero_logradouro = values['numero_logradouro']
        nome_fantasia = values['nome_fantasia']
        tipo_chave_pix = values['tipo_chave_pix']
        chave_pix = values['chave_pix']

        self.close()
        return {"nome": nome, "cpf": cpf, "telefone": telefone, "municipio": municipio,
                "certificacao": certificacao, "cnpj": cnpj, "logradouro": logradouro,
                "numero_logradouro": numero_logradouro, "nome_fantasia": nome_fantasia,
                "tipo_chave_pix": tipo_chave_pix, "chave_pix": chave_pix}

    def mostra_produtor(self, dados_produtor):
        string_todos_produtores = ""
        for dado in dados_produtor:
            string_todos_produtores = string_todos_produtores + "NOME DO PRODUTOR: " + dado["nome"] + '\n'
            string_todos_produtores = string_todos_produtores + "CPF DO PRODUTOR: " + dado["cpf"] + '\n'
            string_todos_produtores = string_todos_produtores + "FONE DO PRODUTOR: " + str(dado["telefone"]) + '\n'
            string_todos_produtores = string_todos_produtores + "MUNICÍPIO DO PRODUTOR: " + (dado["municipio"]) + '\n'
            string_todos_produtores = string_todos_produtores + "CERTIFICAÇÃO DO PRODUTOR: " + (
            dado["certificacao"]) + '\n'
            string_todos_produtores = string_todos_produtores + "CNPJ DO PRODUTOR: " + (dado["cnpj"]) + '\n'
            string_todos_produtores = string_todos_produtores + "LOGRADOURO: " + (dado["logradouro"]) + '\n'
            string_todos_produtores = string_todos_produtores + "NUMERO DO LOGRADOURO: " + (
            dado["numero_logradouro"]) + '\n'
            string_todos_produtores = string_todos_produtores + "NOME FANTASIA: " + (dado["nome_fantasia"]) + '\n'
            string_todos_produtores = string_todos_produtores + "TIPO CHAVE PIX: " + (dado["tipo_chave_pix"]) + '\n'
            string_todos_produtores = string_todos_produtores + "CHAVE PIX: " + (dado["chave_pix"]) + '\n'
            for feira in dado["feiras"]:
                string_todos_produtores = string_todos_produtores + "FEIRA: " + (str(feira.id)) + '\n\n'

        sg.Popup('-------- LISTA DE PRODUTORES ----------', string_todos_produtores)

    def seleciona_produtor(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- SELECIONAR PRODUTOR ----------', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do produtor que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona produtor').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def altera_dados_produtor(self, cpf):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- DADOS PRODUTOR ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.Text(cpf)],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Text('Município:', size=(15, 1)), sg.InputText('', key='municipio')],
            [sg.Text('Certificação:', size=(15, 1)), sg.InputText('', key='certificacao')],
            [sg.Text('Logradouro:', size=(15, 1)), sg.InputText('', key='logradouro')],
            [sg.Text('Numero do logradouro:', size=(15, 1)), sg.InputText('', key='numero_logradouro')],
            [sg.Text('Nome fantasia:', size=(15, 1)), sg.InputText('', key='nome_fantasia')],
            [sg.Text('Tipo chave pix:', size=(15, 1)), sg.InputText('', key='tipo_chave_pix')],
            [sg.Text('Chave pix:', size=(15, 1)), sg.InputText('', key='chave_pix')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Produtores').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        municipio = values['municipio']
        certificacao = values['certificacao']
        logradouro = values['logradouro']
        numero_logradouro = values['numero_logradouro']
        nome_fantasia = values['nome_fantasia']
        tipo_chave_pix = values['tipo_chave_pix']
        chave_pix = values['chave_pix']

        self.close()
        return {"nome": nome, "telefone": telefone, "municipio": municipio, "certificacao": certificacao,
                "logradouro": logradouro, "numero_logradouro": numero_logradouro,
                "nome_fantasia": nome_fantasia, "tipo_chave_pix": tipo_chave_pix, "chave_pix": chave_pix}

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values