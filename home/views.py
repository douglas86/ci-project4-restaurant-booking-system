import datetime

from django.views.generic import TemplateView

from .models import ChefSpecial


# Create your views here.
class HomePageView(TemplateView):
    """
    Home page view
    """

    template_name = "home/index.html"
    model = ChefSpecial

    today = datetime.date.today()  # gets current data of laptop
    current_hour = datetime.datetime.now().strftime("%H")  # gets the current hour only
    year = today.year  # gets the current year

    # name of the restaurant
    name = "culinary Haven"

    def get_served(self):
        """
        Logic to return current meal served
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
        # calls method get_served to see what meals it needs to display
        served_meals = self.get_served()
        # ternary operator to see if variable served_meals is greater than 3
        meal = (
            ChefSpecial.objects.all().filter(served=served_meals)
            if served_meals < 3
            else "Not served"
        )

        return meal

    def get_context_data(self, *args, **kwargs):
        """
        Passes data to the template variable
        :param args:
        :param kwargs:
        :return:
        """
        return {"year": self.year, "name": self.name, "meals": self.get_queryset()}
