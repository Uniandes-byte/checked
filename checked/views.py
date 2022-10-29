from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def team(request):
    return render(request, 'team.html')