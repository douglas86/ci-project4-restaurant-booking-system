from django.views.generic import TemplateView


# Create your views here.
class MenuView(TemplateView):
    template_name = 'menu/menu.html'

    def get_context_data(self, **kwargs):
        meals = ['Breakfast', 'Lunch', 'Supper']

        return {'meals': meals}
