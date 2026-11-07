
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def help_page(request):
    return render(request, 'help.html')


def support_page(request):
    return render(request, 'support.html')


def cart(request):
    return render(request, 'cart.html')


def bestseller(request):
    return render(request, 'bestseller.html')


def contact(request):
    return render(request, 'contact.html')


def shop(request):
    return render(request, 'shop.html')


def single(request):
    return render(request, 'single.html')


def checkout(request):
    return render(request, 'checkout.html')


def page_not_found(request):
    return render(request, '404.html', status=404)
