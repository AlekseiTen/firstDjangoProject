from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path("product/create", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path('contacts/', contacts, name='contacts')
]