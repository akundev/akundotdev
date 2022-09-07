from django.urls import path

from .views import ToolDetailView, ToolListView

urlpatterns = [
    path("", ToolListView.as_view(), name="tools_list"),
    path("<slug:slug>/", ToolDetailView.as_view(), name="tool_detail"),
]
