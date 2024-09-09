from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)

# def home(request):
#     return render(request, 'product_list.html')
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} {phone} {message}')
#     return render(request, 'contacts.html')