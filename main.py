from api_openbanking import Openbanking
from api_openbanking import Rotinas

openbanking = Openbanking
rotinas = Rotinas
status = False

# cadastro = rotinas.cadastro()
dados_cliente = rotinas.login('joao.paulo@gmail.com', 'senha123', status)
print(status)
# catalogo_credito = openbanking.consulta_api()
#print (catalogo_credito)

#simulador_juros = rotinas.simulador_juros()
