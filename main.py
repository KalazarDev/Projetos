# to handle  data retrieval
import urllib3
from urllib3 import request
# to manage json data
import json
import requests

url = 'https://api-cotacao-b3.labdo.it/api/empresa'


# query = {'nm_empresa':'45', 'cd_acao_rdz':'180'}
response = requests.get(url)
response_dict = response.json()
response_a = response.text
for c in response_a:
    print(response_a[c]['cd_acao_rdz'])   


#print(f'{response_dict[c]["cd_acao"]}\n{response_dict[c]["tx_cnpj"]}\n{response_dict[c]["segmento"]}\n{response_dict[c]["setor_economico"]}')


