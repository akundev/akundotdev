from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


from .models import Order


# Create your views here.
class SuccessView(TemplateView):
    template_name = "orders/success_created.html"


class OrderCreateView(CreateView):
    model = Order
    fields = ["name", "email", "product"]

    def get_success_url(self):
        return reverse_lazy("success_created")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.send_email()
        return response
