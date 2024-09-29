from django.shortcuts import render

def login(request):
    return render(request, 'users_interface/login.html')
