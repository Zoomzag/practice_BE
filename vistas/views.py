from django.shortcuts import render

def inicio(request):
    return render(request, 'Practica_class/index.html')

def about(request):
    return render(request, 'Practica_class/about.html')

def about(request):
    return render(request, 'Practica_class/contact.html')

def games(request):
    return render(request, 'Practica_class/games.html')

