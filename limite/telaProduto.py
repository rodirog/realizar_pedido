import PySimpleGUI as sg


class ProdutoView:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def __close(self):
        self.__window.Close()

    def __open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_opcoes(self):
        self.init_opcoes()
        button, values = self.__open()
        if values["1"]:
            opcao = 1
        if values["2"]:
            opcao = 2
        if values["3"]:
            opcao = 3
        if values["4"]:
            opcao = 4
        if values["5"]:
            opcao = 5
        self.__close()
        return opcao

    def init_opcoes(self):
        layout = [
            [sg.Text("CRUD Produto", font=("Helvica", 20))],
            [sg.Text("Escolha sua opção", font=("Helvica", 15))],
            [sg.Radio("Cadastrar Produto ", "RD1", key='1')],
            [sg.Radio("Consultar Produto", "RD1", key='2')],
            [sg.Radio("Alterar Produto", "RD1", key='3')],
            [sg.Radio("Remover Produto", "RD1", key='4')],
            [sg.Radio("Listar Produtos", "RD1", key='5')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("OpenFoods").Layout(layout)

    def cadastrar_produto(self):
        layout = [
            [sg.Text("Cadastrar Produto", font=("Helvica", 20))],
            [sg.Text("ID:", size=(25, 1)), sg.InputText("", key='id')],
            [sg.Text("Nome:", size=(25, 1)), sg.InputText("", key='nome')],
            [sg.Text("Descricao:", size=(25, 1)), sg.InputText("", key='descricao')],
            [sg.Text("Preço Unitário:", size=(25, 1)), sg.InputText("", key='preco_un')],
            [sg.Text("Quantidade Disponível:", size=(25, 1)), sg.InputText("", key='quantidade')],
            [sg.Text("Unidade de Medida:", size=(25, 1)), sg.InputText("", key='unidade_medida')],
            [sg.Text("Preço Desconto:", size=(25, 1)), sg.InputText("", key='preco_desconto')],
            [sg.Text("Qtd desconto:", size=(25, 1)), sg.InputText("", key='qtd_desconto')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]

        self.__window = sg.Window("OpenFoods").Layout(layout)
        button, values = self.__open()

        id = int(values['id'])
        quantidade = values['quantidade']
        qtd_desconto = values['qtd_desconto']
        nome = values['nome']
        preco_desconto = values['preco_desconto']
        descricao = values['descricao']
        preco_un = values['preco_un']
        unidade_medida = values['unidade_medida']

        self.__close()

        return {
            "id": id,
            "nome": nome,
            "descricao": descricao,
            "preco_un": preco_un,
            "quantidade": quantidade,
            "preco_desconto": preco_desconto,
            "qtd_desconto": qtd_desconto,
            "unidade_medida": unidade_medida
        }

    def consultar_produto(self, catalogo_produtos: dict):
        teste = ""

        for produto in catalogo_produtos:
            teste += "Nome: " + produto['nome'] + "\n"
            teste += "Descrição: " + produto['descricao'] + "\n"
            teste += "Preço Unitário: " + produto['preco_un'] + "\n"
            teste += "Quantidade disponível: " + produto['qtd_disponivel'] + "\n"
            teste += "Unidade de Medida: " + produto['unidade_medida'] + "\n"

        sg.Popup("Catálogo de Produtos", teste)

    def alterar_produto(self):
        layout = [
            [sg.Text("Alterar Produto", font=("Helvetica", 20))],
            [sg.Text("Digite o ID do produto que deseja alterar", font=("Helvetica", 15))],
            [sg.Text("ID:", size=(25, 1)), sg.InputText("", key='produto_id')],
            [sg.Text("Nome:", size=(25, 1)), sg.InputText("", key='nome')],
            [sg.Text("Preço Unitário:", size=(25, 1)), sg.InputText("", key='preco_un')],
            [sg.Text("Quantidade Disponível:", size=(25, 1)), sg.InputText("", key='qtd_disponivel')],
            [sg.Text("Unidade de Medida:", size=(25, 1)), sg.InputText("", key='unidade_medida')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]

        self.__window = sg.Window("OpenFoods").Layout(layout)
        button, values = self.__open()

        produto_id = values['produto_id']
        nome = values['nome']
        preco_un = values['preco_un']
        qtd_disponivel = values['qtd_disponivel']
        unidade_medida = values['unidade_medida']

        self.__close()

        return {
            "produto_id": produto_id,
            "nome": nome,
            "preco_un": preco_un,
            "qtd_disponivel": qtd_disponivel,
            "unidade_medida": unidade_medida
        }

    def listar_produtos(self, dados_produtos):
        string_todos_produtos = ""
        for dado in dados_produtos:
            string_todos_produtos = string_todos_produtos + "ID: " + str(dado["id_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "NOME: " + dado["nome_produto"] + '\n'
            string_todos_produtos = string_todos_produtos + "DESCRICAO: " + dado["descricao_produto"] + '\n'
            string_todos_produtos = string_todos_produtos + "QUANTIDADE: " + str(dado["quantidade_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "PREÇO: " + str(dado["preco_un_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "PREÇO DECONTO: " + str(dado["preco_desconto_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "QTD DESCONTO: " + str(
                dado["qtd_desconto_produto"]) + '\n'
            string_todos_produtos = string_todos_produtos + "UNIDADE DE MEDIDA: " + str(dado["unidade_medida_produto"]) + '\n\n'


        sg.Popup('-------- LISTA DE PRODUTOS ----------', string_todos_produtos)

    def remover_produto(self):
        layout = [
            [sg.Text("Remover Produto", font=("Helvetica", 20))],
            [sg.Text("Digite o ID do produto que deseja remover", font=("Helvetica", 15))],
            [sg.Text("ID:", size=(25, 1)), sg.InputText("", key='produto_id')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]

        self.__window = sg.Window("OpenFoods").Layout(layout)
        button, values = self.__open()

        produto_id = values['produto_id']


        self.__close()

        return produto_id
