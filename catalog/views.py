from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "product_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context["product_list"]:
            product.active_version = product.versions.filter(is_current=True).first()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        #фун-ция по созданию продукта только зарег. пользователям
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse_lazy("catalog:product_update", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )

        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')
    return render(request, 'catalog/contacts.html')
