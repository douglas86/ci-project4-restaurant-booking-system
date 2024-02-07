from django.views.generic import TemplateView


# Create your views here.
class MenuView(TemplateView):
    template_name = 'menu/menu.html'
