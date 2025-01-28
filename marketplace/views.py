from django.shortcuts import render

def index(request):
    return render(request, 'marketplace/index.html')

def about(request):
    return render(request, 'marketplace/about.html')

def sell(request):
    return render(request, 'marketplace/sell.html')

def buy(request):
    return render(request, 'marketplace/buy.html')