from django.urls import path

from .views import AboutTemplateView

urlpatterns = [path("", AboutTemplateView.as_view(), name="about")]
