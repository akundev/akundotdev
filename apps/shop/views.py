from django.views.generic import DetailView, ListView

from apps.users.models import CustomUser

from .models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "shop/products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "shop/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context
