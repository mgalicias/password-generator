from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def welcome(request):
    return render(request,"generator/home.html")


def password(request):

    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    #length = int( request.form.get('length') )
    length = int( request.GET.get('length') )

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIUJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    
    if request.GET.get('special'):
        characters.extend("!@#$%^&*()-=_+/<>~")
    
    password = ""   

    for x in range(length):
        password += random.choice(characters)


    return render( request ,"generator/generate-password.html" , { 'password' : password  } )
