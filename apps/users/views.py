from django.views.generic import TemplateView


class AboutTemplateView(TemplateView):
    template_name = "users/about.html"
