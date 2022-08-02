# to handle  data retrieval
import urllib3
from urllib3 import request
# to handle certificate verification
import certifi
# to manage json data
import json
# for pandas dataframes
import pandas as pd
# uncomment below if installation needed (not necessary in Colab)
#!pip install certifi
from pandas.io.json import json_normalize
import requests

url = 'https://api-cotacao-b3.labdo.it/api/empresa'


query = {'nm_empresa':'45', 'cd_acao_rdz':'180'}
response = requests.get(url, params=query)
print(response.json())