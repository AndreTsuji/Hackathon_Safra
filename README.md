# Hackathon_Safra
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

Desenvolvimento de um app (marca desvinculada do banco safra) focado no microempreendedor e pequenas empresas que compare os cenários de aquisição de crédito na principais instituições financeiras do país e apresente para o usuário as melhores opções de crédito com as menores taxas do mercado.


![login_page](https://user-images.githubusercontent.com/95044193/161455093-40a72c77-b6ac-4c97-8518-665cb3023173.png)
![simulate_page](https://user-images.githubusercontent.com/95044193/161454623-948b5ede-d1a4-4c68-a6ae-30940e307bbf.png)
![calc_page](https://user-images.githubusercontent.com/95044193/161454506-bbd658a4-2bc6-4c4b-a6cc-b10ca7dab123.png)
  
## Porque o projeto é útil

Para ter acesso à facilidade proporcionada pelo app em encontrar as melhores ofertas de crédito, o usuário deve aceitar o termo de compartilhamentos de dados bancários do OpenBanking. O Safra então terá acesso aos dados de clientes das mais variadas instituições financeiras do país, permitindo por exemplo:
- obter insumos para automatização das análises de risco;
- aumentar o portfólio de clientes e nichos de mercado (Estudos de prospecção);
- mapeamento de mercado mais assertivo (segmento e setores de mercado, qualidade de atendimento, taxas…);
- oferta de produtos e serviços personalizados de acordo com o perfil e histórico do cliente;
- valorização do Cliente baseado em seus dados compartilhados;
- fortalecer as áreas de negócio e tomadas de decisão para o Banco Safra.

## Funcionalidades

A [api_openbanking.py](api_openbanking.py) consiste em um arquivo python com as seguintes classes/ funções:

Openbanking.consulta_api() -> responsável pela coleta e tratamento dos dados abertos de serviços de empréstimos e financiamentos disponibilizados pelas instituições financeiras participantes do OpenBanking

Openbanking.menor_taxa(lista_servicos) -> lista das ofertas de crédito listadas da menor para a maior taxa

Openbanking.Filtro_servico(Tipo_servico) -> lista das ofertas de crédito filtradas por tipo de serviço

Rotinas.simulador_juros(credito, entrada, periodo, juros) -> simulação de crédito de acordo com valor, entrada e número de parcelas desejadas

Rotinas.login(login, senha, status) -> login do app

Rotinas.cadastro() -> cadastro de novos usuários

## Técnicas e Tecnologias utilizadas

* Python
* SQL
* Orientação a objeto

## Contribuidores

Barbara Bernardi/
Cleyson Teixeira/
Daniel Rezende/
Gabriel P. Assis/
Gallileu Genesis/
Leo Carvalho


## Desenvolvedores:
André Tsuji/
Gabriel Veronezzi
