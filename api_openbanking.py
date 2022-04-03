import cProfile


class Openbanking:

    def consulta_api():

        import requests
        import json

        # url das API's de todos os bancos cadastrados no aplicativo.
        url = (
            'https://api.safra.com.br/open-banking/products-services/v1/business-financings',
            'https://opendata.api.bb.com.br/open-banking/products-services/v1/business-financings',
            'https://api.bradessco.com/bradesco/open-banking/products-services/v1/business-financings',
            'https://api.itau/open-banking/products-services/v1/business-financings',
            'https://openbanking.api.santander.com.br/open-banking/products-services/v1/business-financings'
        )

        lista_servicos = {}
        n_servicos = 0
        api = 0
        for x in url:
            # Em caso de falha na comunicação, função retorna vazio.
            try:
                # Requisição dos dados
                req = requests.get(url[api], timeout=10)
                if req.status_code == 200:
                    # API acessada com sucesso.
                    servico = req.json()
                    lista = servico['data']['brand']['companies'][0]

                    # Construção do dicionario de serviços, taxas e instiução que a função retornará.
                    instituicao = lista['name']
                    aux = 0
                    for i in lista['businessFinancings']:
                        if lista['businessFinancings'][aux]['interestRates'][0]['referentialRateIndexer'] == 'PRE_FIXADO':
                            lista_servicos[n_servicos] = [instituicao, [lista['businessFinancings'][aux]['type']], [
                                lista['businessFinancings'][aux]['interestRates'][0]['maximumRate']]]
                            n_servicos += 1
                        aux += 1
            except:
                pass
            api += 1
        return lista_servicos

    # Desenvolver def de consulta de dados de clientes (necessita credenciais do Banco Safra + autorização do cliente)
    # def info_cliente():


class Rotinas:

    # Função retorna resultados do layout de simulação.
    def simulador_juros(credito, entrada, periodo, juros):
        # simulador = [montante, parcela, total de juros]
        montante = credito * ((1+juros)**periodo)
        simulador = [montante, montante/periodo, montante - credito]

        return simulador

     # Função login
    def login(login, senha):
        import mysql.connector

        conexao = mysql.connector.connect(
            host='localhost', database='db_Cadastro', user='root', password='')

        if conexao.is_connected():
            db_info = conexao.get_server_info()
            cursor = conexao.cursor()
            cursor.execute("select ")

        # Desativa a conexão com a base de dados após uso.
        if conexao.is_connected():
            cursor.close()
            conexao.close()

        return(dados_cliente)
            
    # Função adiciona cadastro de novo usuário em base de dados
    def cadastro():
        import mysql.connector
        from mysql.connector import Error
        from datetime import datetime

        # Com os campos de entradas de dados já referenciados, atribuir diretamento os valores
        tbl_nome = input("Nome: ")
        tbl_cpf = input("CPF: ")
        tbl_senha = input("Senha: ")
        tbl_nasc = input("Data de nascimento: ")
        tbl_email = input("E-mail: ")
        tbl_telefone = input("Telefone: ")
        tbl_setor = input("Setor: ")
        tbl_autorizacao_openbanking = datetime.today().strftime('%d/%m/%Y')

        # Definição da query SQL para adicionar o novo cliente na base cadastral.
        # Junto com o cadastro será solicitado a autorizacao de consulta dos dados cliente no OpenBanking durante 6 meses.
        # A variável autorização_openbanking registrará a data do cadastro e servirá de flag para alertar o Safra o momento
        # que terá venciodo o periodo de autorização de uso dos dados do OpenBanking.
        declaracao = """INSERT INTO tbl_user (nome, cpf, senha, nasc, autorizacao_openbanking, email, telefone, setor) VALUES ("""
        dados = "'" + tbl_nome + "','" + tbl_cpf + "','" + tbl_senha + "','" + tbl_nasc + "','" + \
            str(tbl_autorizacao_openbanking) + "','" + \
            tbl_email + "','" + tbl_telefone + "','" + tbl_setor + "')"
        comando = declaracao + dados
        try:
            conexao = mysql.connector.connect(
                host='localhost', database='db_Cadastro', user='root', password='')

            inserir_cadastro = comando
            cursor = conexao.cursor()
            cursor.execute(inserir_cadastro)

            # Desativa a conexão com a base de dados após uso.
            conexao.commit()
            cursor.close()
        except Error as erro:
            print("Falha no processo de cadastro.")
