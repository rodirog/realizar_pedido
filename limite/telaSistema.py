import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        print(msg)

    def init_components(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('Open Foods', font=("Helvica", 25))],
            [sg.Text('Coma saudável e sustentável!', font=("Helvica", 15))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Produtores', "RD1", key='1')],
            [sg.Radio('Produtos', "RD1", key='2')],
            [sg.Radio('Pedido', "RD1", key='3')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Open Foods').Layout(layout)