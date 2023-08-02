import requests
from django.http import JsonResponse
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

def get_weather_data(request):
    location = request.GET.get('location')
    print(location)
    api_key = '272206d9d71640779bf63731230108'  

    try:
        
        api_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
        print("API URL:", api_url)

        
        response = requests.get(api_url)
        print("API Response Status Code:", response.status_code)

        
        if response.status_code == 200:
            weather_data = response.json()
            data = {
                'condition': weather_data['current']['condition']['text'],
                'location': weather_data['location']['name'],
                'temperature': weather_data['current']['temp_c'],
                'humidity': weather_data['current']['humidity'],
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Error fetching weather data'}, status=500)
    except Exception as e:
        print("Exception:", e)
        return JsonResponse({'error': str(e)}, status=500)