from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.


# Development API key
api_key = 'DEMO_KEY'


def index(request):

    response = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=' + api_key)

    if response.status_code == 200:
        data = response.json()
        return render(request, 'blog/index.html', {'data': data})
    else:
        return HttpResponse("Error")
