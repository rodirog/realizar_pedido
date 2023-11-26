import PySimpleGUI as sg


class TelaPedido():
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
            [sg.Text('-------- Pedidos ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Pedido', "RD1", key='1')],
            [sg.Radio('Listar Pedidos', "RD1", key='2')],
            [sg.Radio('Confirmar Pagamento', "RD1", key='3')],
            [sg.Radio('Incluir item', "RD1", key='4')],
            [sg.Radio('Realizar Pedido', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Pedidos').Layout(layout)

    def selecionar_local(self, dados_feiras, endereco_propriedade):
        sg.ChangeLookAndFeel('Green')
        feira_layout = []

        radio_key = endereco_propriedade

        propriedade_info = [

            [sg.Text(f"Na propriedade", font=("Helvetica", 16), size=(25, 1))],
            [sg.Text(f"Endereço: {endereco_propriedade}", size=(40,1))],
            [sg.Radio(f'Selecionar', 'RD1', key=radio_key)],
        ]

        propriedade_layout = propriedade_info

        feira_layout.append([sg.Text(f"Em uma feira", font=("Helvetica", 16), size=(15, 1))])

        for feira in dados_feiras:
            feira_id = feira["id"]
            feira_dia_semana = feira["dia_semana"]
            feira_municipio = feira["municipio"]
            feira_logradouro = feira["logradouro"]
            feira_numero_logradouro = feira["numero_logradouro"]

            radio_key = f'feira_{feira_id} feira_{feira_dia_semana}'

            feira_info = [
                [sg.Text(f"Dia da semana: {feira_dia_semana}")],
                [sg.Text(f"Município: {feira_municipio}")],
                [sg.Text(f"Logradouro: {feira_logradouro}")],
                [sg.Text(f"Número: {feira_numero_logradouro}")],
                [sg.Radio(f'Selecionar', 'RD1', key=radio_key)],
                [sg.HorizontalSeparator()],
            ]

            feira_layout.extend(feira_info)

        column_layout_feiras = sg.Column(feira_layout, size=(400, 300), scrollable=True)
        column_layout_propriedade = sg.Column(propriedade_layout, size=(300, 200))

        layout = [
            [sg.Text(f"Como deseja retirar seu pedido?", font=("Helvetica", 16), size=(30, 1))],
            [column_layout_feiras, column_layout_propriedade],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]

        self.__window = sg.Window('Realizar pedido').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event in (None, 'Voltar'):
                self.__window.Close()
                return 0
                #break

            if event == 'Confirmar':

                for feira in dados_feiras:
                    radio_key = f'feira_{feira["id"]} feira_{feira["dia_semana"]}'
                    if values[radio_key]:
                        self.__window.Close()
                        return feira["dia_semana"], feira["municipio"], feira["logradouro"], feira["numero_logradouro"]

                radio_key = endereco_propriedade
                if values[radio_key]:
                    self.__window.Close()
                    return endereco_propriedade

                else:
                    self.__window.Close()
                    self.mostra_mensagem("Voce nao selecionou uma opcao")
                    return 0
                    #sg.popup_error("Please select an option")


    def mostrar_revisao_pedido(self, dados_itens, preco_total, local, nome_produtor):
        sg.ChangeLookAndFeel('Green')
        itens_layout = []

        dados_retirada_info = [

            [sg.Text(f"Endereço", font=("Helvetica", 16), size=(15, 1))],
            [sg.Text(f"{local}")],
            [sg.Text(f"Nome do produtor", font=("Helvetica", 16), size=(15, 1))],
            [sg.Text(f"{nome_produtor}")]
        ]

        dados_retirada_layout = dados_retirada_info

        itens_layout.append([sg.Text(f"Itens", font=("Helvetica", 16), size=(15, 1))])

        for item in dados_itens:
            nome_produto = item["nome_produto"]
            quantidade_produto = item["quantidade_produto"]

            item_info = [
                [sg.Text(f"Nome do produto: {nome_produto}")],
                [sg.Text(f"Quantidade: {quantidade_produto}")],
                [sg.HorizontalSeparator()],
            ]

            itens_layout.extend(item_info)

        valor_total_info = [

            [sg.Text(f"Valor total", font=("Helvetica", 16), size=(15, 1))],
            [sg.Text(f"R$ {preco_total}")],
        ]

        valor_total_layout = valor_total_info

        column_layout_dados_retirada = sg.Column(dados_retirada_layout, size=(400, 300))
        column_layout_itens = sg.Column(itens_layout, size=(200, 200), scrollable=True)
        column_layout_valor_total = sg.Column(valor_total_layout, size=(200, 200))

        layout = [
            [sg.Text(f"Confirme os dados do pedido", font=("Helvetica", 16), size=(30, 1))],
            [column_layout_itens, column_layout_valor_total, column_layout_dados_retirada],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]

        self.__window = sg.Window('Realizar pedido').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event in (None, 'Voltar'):
                self.__window.Close()
                return False
                break

            if event == 'Confirmar':
                self.__window.Close()
                return True

    def realizar_pagamento(self, dados_pagamento):
        sg.ChangeLookAndFeel('Green')

        dados_pagamento_info = [
            [sg.Text(f"Dados do pagamento", font=("Helvetica", 16), size=(20, 1))],
            [sg.Text(f"CHAVE PIX", font=("Helvetica", 11), size=(20, 1))],
            [sg.Text(f"{dados_pagamento['chave_pix']}")],
            [sg.Text(f"TIPO", font=("Helvetica", 11), size=(20, 1))],
            [sg.Text(f"{dados_pagamento['tipo_chave']}")],
            [sg.Text(f"NOME PRODUTOR", font=("Helvetica", 11), size=(20, 1))],
            [sg.Text(f"{dados_pagamento['nome_produtor']}")],
            [sg.Text(f"VALOR", font=("Helvetica", 11), size=(20, 1))],
            [sg.Text(f"R$ {str(dados_pagamento['preco_total'])}")]
        ]

        dados_pagamento_layout = dados_pagamento_info

        column_layout_dados_pagamento = sg.Column(dados_pagamento_layout, size=(400, 300))

        layout = [
            [sg.Text(f"Realize o pagamento", font=("Helvetica", 16), size=(30, 1))],
            [column_layout_dados_pagamento],
            [sg.Text(f"*Realize o pagamento e aguarde a confirmação do pedido", font=("Helvetica", 8), size=(60, 1))],
            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Realizar pedido').Layout(layout)

        while True:
            event, values = self.__window.Read()

            #if event in (None, 'Voltar'):
            #    self.__window.Close()
            #    break

            if event == 'Confirmar':
                self.__window.Close()
                self.mostra_mensagem("Pedido realizado. Espere a confirmação do produtor")
                return True
            else:
                self.mostra_mensagem("Pedido realizado. Espere a confirmação do produtor")
                break

    def pegar_dados_pedido(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text("Cadastre o pedido", font=("Helvica", 16), size=(15, 1))],
            [sg.Text("*Id", size=(15, 1)), sg.InputText(key="it_id", size=(6, 1))],
            [sg.Text("*Preço total", size=(15, 1)), sg.InputText(key="it_preco_total")],
            [sg.Text("*Id do produtor", size=(15, 1)), sg.InputText(key="it_id_produtor")],
            [sg.HorizontalSeparator()],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gerenciemento de pedidos').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            self.close()
            return
        id = int(values['it_id'])
        preco_total = float(values['it_preco_total'])
        id_produtor = int(values['it_id_produtor'])

        self.close()
        return {"id_pedido": id, "preco_total_pedido": preco_total,
                "id_produtor": id_produtor}

    def mostra_pedido(self, dados_pedido):
        string_todos_pedidos = ""
        for dado in dados_pedido:
            string_todos_pedidos = string_todos_pedidos + "CODIGO DO PEDIDO: " + dado["codigo"] + '\n'
            string_todos_pedidos = string_todos_pedidos + "NOME DO PRODUTOR: " + dado["produtor"] + '\n'
            string_todos_pedidos = string_todos_pedidos + "PRODUTOS: " + dado["produtos"] + '\n'
            string_todos_pedidos = string_todos_pedidos + "STATUS: " + (dado["status"]) + '\n\n'

        sg.Popup('-------- LISTA DE PEDIDOS ----------', string_todos_pedidos)

    def seleciona_pedido(self):
        sg.ChangeLookAndFeel('Green')
        layout = [
            [sg.Text('-------- SELECIONAR PEDIDO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o codigo do pedido que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona pedido').Layout(layout)

        button, values = self.open()
        id = int(values['codigo'])
        self.close()
        return id

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def tela_login(self):
        login = input("CPF do produtor: ")
        return login

    def tela_informa_codigo_pedido(self):
        return input("Digite o código do pedido: ")  # Solicita o código do pedido ao usuário