from django.shortcuts import render
from django.conf import settings
import json
import os

# Create your views here.

def getProviders(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'app/static/app/providers.json')

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    if 'search' in request.GET:
        q = request.GET
        print(q)
        if 'fff' in request.GET['SERCHTEST1']:
            print("HERE")
        
        return render(request, 'app/search.html', {'data': data})
    return render(request, 'app/index.html', {'data': data})

def searchProviders(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'app/static/app/providers.json')
    with open(json_file_path, 'r') as file:
        data = json.load(file)


    if 'search' in request.GET:
        return render(request, 'app/search.html', {'data': data})
    
    return render(request, 'app/search.html', {'data': data})
