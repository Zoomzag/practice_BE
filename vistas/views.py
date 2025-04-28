from django.shortcuts import render

def inicio(request):
    return render(request, 'Practica_class/index.html')

def about(request):
    return render(request, 'Practica_class/about.html')

def about(request):
    return render(request, 'Practica_class/contact.html')

def games(request):
    return render(request, 'Practica_class/games.html')

def sign_in(request):
    return render(request, 'Practica_class/sign_in.html')

def sign_up(request):
    return render(request, 'Practica_class/sign_up.html')

