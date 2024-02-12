import datetime

from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home/index.html'

    today = datetime.date.today()
    year = today.year

    def get_context_data(self, *args, **kwargs):
        return {'year': self.year}
