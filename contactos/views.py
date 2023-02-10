from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    vista = "Contactos"
    return render(request, 'index.html', 
                context = {'vista' : vista})