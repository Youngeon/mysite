from django.shortcuts import render
from django.http import Http404
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = '146a87f980237d3343ca5522e8ab816f'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    
    if(request.method == "POST"):# Проверяем запрос
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm() # Erase form 
    
    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        try:
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]
            }

            all_cities.append(city_info) 
        except:
            pass
    all_revcities = reversed(all_cities)
    context = {'all_info': all_revcities, 'form': form}
    return render(request, 'weather.html', context)