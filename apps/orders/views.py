from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from apps.users.models import CustomUser

from .models import Order


# Create your views here.
class SuccessView(TemplateView):
    template_name = "orders/success_created.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context


class OrderCreateView(CreateView):
    model = Order
    fields = ["name", "email", "product"]

    def get_success_url(self):
        return reverse_lazy("success_created")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.send_email()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context
