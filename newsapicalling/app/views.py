from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    url = "https://newsapi.org/v2/everything?q=keyword&apiKey=c49eac1bf9f144a8ba5418fc6aa8fffd"
    response = requests.get(url)
    # data = json.loads(response.text)
    data = response.json().get("totalResults")
    datas = response.json().get("articles")
    print(f'Total users: {response.json().get("articles")}')
    return render(request, 'index.html', {"data": data,'datas':datas})
 
#  https://newsapi.org/v2/everything?q=tesla&from=2023-09-14&sortBy=publishedAt&apiKey=API_KEY c49eac1bf9f144a8ba5418fc6aa8fffd