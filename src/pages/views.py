from django.shortcuts import render
import requests

def index(request):
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    context = {
        'users': users.json()
    }
    return render(request, "index.html", context)
