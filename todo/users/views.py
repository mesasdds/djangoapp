from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request) 
    return redirect('/accounts/login')  


