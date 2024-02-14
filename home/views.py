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
    current_hour = datetime.datetime.now().strftime('%H')
    year = today.year

    # name of the restaurant
    name = "culinary Haven"

    def get_served(self):
        """
        Logic to return current meal
        :return:
        """
        if int(self.current_hour) >= 18:
            return 2  # filters all supper meals
        elif int(self.current_hour) >= 12:
            return 1  # filters all lunch meals
        elif int(self.current_hour) >= 8:
            return 0  # filters all breakfast meals
        else:
            return 3  # returns the default image

    def get_queryset(self):
        """
        Gathers data from a database based on filter
        """
        served_meals = self.get_served()
        print('s', served_meals)
        meal = ChefSpecial.objects.all().filter(served=served_meals) if served_meals < 3 else "Not served"
        return meal

    def get_context_data(self, *args, **kwargs):
        """
        Passes the current year to the template context
        :param args:
        :param kwargs:
        :return:
        """
        return {'year': self.year, "name": self.name, "meals": self.get_queryset()}
