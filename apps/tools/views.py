from django.views.generic import DetailView, ListView

from apps.users.models import CustomUser

from .models import Tool

# Create your views here.


class ToolListView(ListView):
    model = Tool
    context_object_name = "tools"
    template_name = "tools/tools_list.html"
    queryset = Tool.objects.all()[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context


class ToolDetailView(DetailView):
    model = Tool
    context_object_name = "tool"
    template_name = "tools/tool_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context
