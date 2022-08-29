import requests

cep = '01306040'
link = f'https://viacep.com.br/ws/{cep}/json/'
requisicao = requests.get(link)

dic_requisicao = requisicao.json()

uf=dic_requisicao['uf']
cidade = dic_requisicao['localidade']

print(uf, cidade)