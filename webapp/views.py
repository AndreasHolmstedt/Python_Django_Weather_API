from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import City
from .forms import CityForm

import requests

def index(request):

    key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID=fd517109eb32166ea6c3f9ce98aeae19&units=metric'


    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("../webapp")

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        call = requests.get(url.format(city)).json()

        if call[u'cod'] == 200:
            weather_report = {
                'city_name': city,
                'temp': round(call['main']['temp']),
                'icon': call['weather'][0]['icon'],
                'desc': call['weather'][0]['description'],
            }
            weather_data.append(weather_report)

    context  = {'weather_data': weather_data, 'form': form }
    return render(request, 'webapp/home.html', context)
