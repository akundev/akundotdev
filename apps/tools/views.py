from django.views.generic import DetailView, ListView


from .models import Tool

# Create your views here.


class ToolListView(ListView):
    model = Tool
    context_object_name = "tools"
    template_name = "tools/tools_list.html"
    queryset = Tool.objects.all()[:5]


class ToolDetailView(DetailView):
    model = Tool
    context_object_name = "tool"
    template_name = "tools/tool_detail.html"
