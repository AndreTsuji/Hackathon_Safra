def consulta_api(banco):

    import requests
    import json

    # Definição da url da API do banco selecionado
    if banco == 'safra':
        url = 'https://api.safra.com.br/open-banking/products-services/v1/business-financings'
    elif banco == 'bb':
        url = 'https://opendata.api.bb.com.br/open-banking/products-services/v1/business-financings'
    elif banco == 'bradesco':
        url = 'https://api.bradessco.com/bradesco/open-banking/products-services/v1/business-financings'
    elif banco == 'itau':
        url = 'https://api.itau/open-banking/products-services/v1/business-financings'
    elif banco == 'santander':
        url = 'https://openbanking.api.santander.com.br/open-banking/products-services/v1/business-financings'
    else:
        url = 'https://api.safra.com.br/open-banking/products-services/v1/business-financings'

    # Requisição dos dados
    req = requests.get(url, timeout=3)
    servico = req.json()
    lista = servico['data']['brand']['companies'][0]

    # Construção do dicionario de serviços, taxas e instiução que a função retornará.
    lista_servicos = {}
    instituicao = lista['name']
    aux = 0
    for i in lista['businessFinancings']:
        if lista['businessFinancings'][aux]['interestRates'][0]['referentialRateIndexer'] == 'PRE_FIXADO':
            lista_servicos[lista['businessFinancings'][aux]['type']] = [
                lista['businessFinancings'][aux]['interestRates'][0]['maximumRate'], instituicao]
        aux += 1
    return lista_servicos
