from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')