import PySimpleGUI as sg


class TelaConsumidor():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
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
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- CONSUMIDORES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Se cadastre como consumidor', "RD1", key='1')],
            [sg.Radio('Alterar meus dados', "RD1", key='2')],
            [sg.Radio('Listar consumidores', "RD1", key='3')],
            [sg.Radio('Excluir minha conta', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('OPEN FOODS').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def dados_cadastro_consumidor(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- DADOS CONSUMIDOR ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Telefone:', size=(15, 1)),
             sg.InputText('', key='telefone')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Municipio:', size=(15, 1)),
             sg.InputText('', key='municipio')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('OPEN FOODS ').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        cpf = values['cpf']
        municipio = values['municipio']

        self.close()
        return {"nome": nome, "telefone": telefone, "cpf": cpf, "municipio": municipio}

    def altera_dados_consumidor(self, cpf):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- DADOS CONSUMIDOR ----------', font=("Helvica", 25))],
            [sg.Text('CPF:', size=(15, 1)), sg.Text(cpf)],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Text('Municipio:', size=(15, 1)), sg.InputText('', key='municipio')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('OPEN FOODS ').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        municipio = values['municipio']

        self.close()
        return {"nome": nome, "telefone": telefone, "municipio": municipio}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def mostra_consumidor(self, dados_consumidor):
        string_todos_consumidores = ""
        for dado in dados_consumidor:
            string_todos_consumidores = string_todos_consumidores + \
                                        "Nome: " + dado["nome"] + '\n'
            string_todos_consumidores = string_todos_consumidores + \
                                        "Numero Telefone: " + str(dado["telefone"]) + '\n'
            string_todos_consumidores = string_todos_consumidores + \
                                        "Municipio: " + str(dado["municipio"]) + '\n'
            string_todos_consumidores = string_todos_consumidores + \
                                        "CPF: " + str(dado["cpf"]) + '\n\n'

        sg.Popup('-------- LISTA DE CONSUMIDORES ----------',
                 string_todos_consumidores)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_consumidor(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- SELECIONAR CONSUMIDOR ----------',
                     font=("Helvica", 25))],
            [sg.Text('Digite o CPF do consumidor que deseja selecionar:',
                     font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona consumidor').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
