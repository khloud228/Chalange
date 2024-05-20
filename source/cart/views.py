from django.shortcuts import render, HttpResponse
from source.services import Cart


def testCart(request):
    cart = Cart(request)
    print(cart.cart)
    return HttpResponse('console!')
