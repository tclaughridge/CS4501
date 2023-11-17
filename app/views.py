from django.shortcuts import render
from django.conf import settings
import json
import os

# Create your views here.

def getProviders(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'app/static/app/providers.json')

    with open(json_file_path, 'r') as file:
        data = json.load(file)
        data = sorted(data, key=lambda x: x['name'].lower())

    return render(request, 'app/index.html', {'data': data})


def filterProviders(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'app/static/app/providers.json')

    with open(json_file_path, 'r') as file:
        data = json.load(file)
        data = sorted(data, key=lambda x: x['name'].lower())

    # Create a list to store filter conditions, names, and values
    filter_conditions = []

    # Check if each filter parameter is in the request.GET dictionary

    # Location Filter
    if 'location' in request.GET:
        location = request.GET['location'].lower()
        filter_conditions.append({
            'name': 'Location',
            'value': location,
            'condition': lambda provider: location in provider['city'].lower() or location in provider['county'].lower() or location in provider['zip']
        })

    # Services Filter
    if 'service_type' in request.GET:
        selected_service_types = request.GET.getlist('service_type')
        filter_conditions.append({
            'name': 'Service Types',
            'value': ', '.join(selected_service_types),
            'condition': lambda provider: any(service_type in provider['services'] for service_type in selected_service_types)
        })

    # Health Plan filter
    if 'health_plan' in request.GET:
        selected_health_plans = request.GET.getlist('health_plan')
        filter_conditions.append({
            'name': 'Health Plans',
            'value': ', '.join(selected_health_plans),
            'condition': lambda provider: any(plan in provider['health_plan'] for plan in selected_health_plans)
        })

    
    # Languages Spoken filter
    if 'languages_spoken' in request.GET:
        selected_languages_spoken = request.GET.getlist('languages_spoken')
        filter_conditions.append({
            'name': 'Languages Spoken',
            'value': ', '.join(selected_languages_spoken),
            'condition': lambda provider: any(language in provider['languages_spoken'] for language in selected_languages_spoken)
        })


    # Apply filter conditions to the data
    filtered_data = data
    for condition in filter_conditions:
        filtered_data = list(filter(condition['condition'], filtered_data))

    return render(request, 'app/index.html', {'data': filtered_data, 'filter_conditions': filter_conditions})

