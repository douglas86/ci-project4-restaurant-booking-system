import datetime

from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    """
    Home page view
    """
    template_name = 'home/index.html'

    # variables to gather current year of Laptop
    today = datetime.date.today()
    year = today.year

    def get_context_data(self, *args, **kwargs):
        """
        Passes the current year to the template context
        :param args:
        :param kwargs:
        :return:
        """
        return {'year': self.year}
