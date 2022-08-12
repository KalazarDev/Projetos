
# API (v3) 26b70d65cf33405492bbb8b17e5fb8b9
# https://api.themoviedb.org/3/movie/550?api_key=26b70d65cf33405492bbb8b17e5fb8b9
# API (V4) eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNmI3MGQ2NWNmMzM0MDU0OTJiYmI4YjE3ZTVmYjhiOSIsInN1YiI6IjYyY2YzZTcwYjM5ZTM1MDA0ZTI0MGFjNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GzzvXy5iDaZk0sdxE1BcHuMhwcN0ypHJ_vqNOg7WnRA
from itertools import count
from urllib.request import urlopen
import requests
import json

url = 'https://api.themoviedb.org/3/discover/movie?api_key='
url_add = '&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate'
api_key = '26b70d65cf33405492bbb8b17e5fb8b9'
request = requests.get(url + api_key + url_add)
todos = json.loads(request.content)



for i in range(0, len(todos['results'])):
    print(f'Filme {i+1}: {todos["results"][i]["original_title"]}  Nota: {todos["results"][i]["vote_average"]}')
