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
