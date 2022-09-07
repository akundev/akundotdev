from django.views.generic import TemplateView

from .models import CustomUser


class AboutTemplateView(TemplateView):
    template_name = "users/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context
