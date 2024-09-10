from django.shortcuts import render
import pip._vendor.requests as requests

def home(request):

    city = request.GET.get('city', 'Kanpur')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d448c7118ab0ab5e8a41e06edc01a091'
    data = requests.get(url).json()

    payload = {'city':data['name'], 
               'weather': data['weather'][0]['main'], 
               'icon': data['weather'][0]['icon'],
               'kalvin_tempreture': data['main']['temp'], 
               'clacius_tempreture': int(data['main']['temp'] - 273), 
               'pressure':data['main']['pressure'], 
               'humidity':data['main']['humidity'],
               'description':data['weather'][0]['description']
               }
    
    context = {'data': payload}
    return render(request,'home.html', context)