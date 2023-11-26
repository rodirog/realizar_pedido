import PySimpleGUI as sg

class TelaItemPedido:

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        opcao = None
        button, values = self.open()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('Gerenciamento de itens', font=("Helvica", 22))],
            [sg.Text('Escolha sua opção', font=("Helvica", 13))],
            [sg.Radio('Incluir item', "RD1", key='1')],
            [sg.Radio('Listar itens', "RD1", key='2')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Gerenciamento de feiras').Layout(layout)

    def pegar_dados_item(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text("Cadastre o item", font=("Helvica", 16), size=(15, 1))],
            [sg.Text("*Id", size=(15, 1)), sg.InputText(key="it_id", size=(6, 1))],
            [sg.Text("*Id_produto", size=(15, 1)), sg.InputText(key="it_id_produto")],
            [sg.Text("*Quantidade", size=(15, 1)), sg.InputText(key="it_quantidade")],
            [sg.HorizontalSeparator()],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gerenciamento de itens').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            self.close()
            return

        id = int(values['it_id'])
        id_produto = int(values['it_id_produto'])
        quantidade = int(values['it_quantidade'])

        self.close()
        return {"id_item": id, "id_produto_item": id_produto,
                "quantidade_item": quantidade}

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)