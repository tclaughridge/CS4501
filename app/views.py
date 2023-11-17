from django.shortcuts import render
from django.conf import settings
import json
import os

# Create your views here.

def getProviders(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'app/static/app/providers.json')

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    return render(request, 'app/index.html', {'data': data})
