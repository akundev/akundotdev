from django.views.generic import DetailView, ListView


from .models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "shop/products_list.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "shop/product_detail.html"
