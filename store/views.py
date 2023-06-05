from django.shortcuts import render
import json

from store.models import Product


def cart_view(request):  # request - http packet
    return render(request, 'cart_page.html')


def sale_view(request):  # request - http packet
    return render(request, 'enpty_page.html')


def promo_view(request):  # request - http packet
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # Product(**data).save()
        Product.objects.create(**data)
    elif request.method == 'PATCH':
        data = json.loads(request.body.decode('utf-8'))
        if "id" in data:
            ch_product = Product.objects.get(pk=data['id'])
            ch_product.price = data['price']
            ch_product.title = data['title']
            ch_product.save()
    return render(request, 'enpty_page.html')
