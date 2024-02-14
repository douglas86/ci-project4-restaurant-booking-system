import datetime

from django.views.generic import TemplateView

from .models import ChefSpecial


# Create your views here.
class HomePageView(TemplateView):
    """
    Home page view
    """
    template_name = 'home/index.html'
    model = ChefSpecial

    # variables to gather current year of Laptop
    today = datetime.date.today()
    year = today.year

    # name of the restaurant
    name = "culinary Haven"

    def get_context_data(self, *args, **kwargs):
        """
        Passes the current year to the template context
        :param args:
        :param kwargs:
        :return:
        """
        return {'year': self.year, "name": self.name}
