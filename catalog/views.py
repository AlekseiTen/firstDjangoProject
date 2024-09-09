from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)


def products_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"products": product}
    return render(request, 'products_detail.html', context)
