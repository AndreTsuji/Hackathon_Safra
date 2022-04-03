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
tbl_autorizacao_openbanking = datetime.today().strftime('%d/%m/%Y')

dados = "'" + tbl_nome + "','" + tbl_cpf + "','" + tbl_senha + "','" + tbl_nasc + "','" + str(tbl_autorizacao_openbanking) + "','" + tbl_email + "','" + tbl_telefone + "')"

declaracao = """INSERT INTO tbl_user (nome, cpf, senha, nasc, autorizacao_openbanking, email, telefone) VALUES ("""
comando = declaracao + dados
print(comando)