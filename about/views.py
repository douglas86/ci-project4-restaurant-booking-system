import datetime

from django.views.generic import TemplateView


# Create your views here.
class AboutView(TemplateView):
    """
    About view to render about a restaurant to template
    """

    # template to be rendered
    template_name = 'about/about.html'

    # fetches current date of computer
    today = datetime.date.today()
    # fetches current hour based off the variable above
    current_hour = datetime.datetime.now().strftime("%H")
    # fetches current year based off the variable above
    year = today.year

    def get_context_data(self, **kwargs):
        """
        built in method used to render data to template
        :param kwargs:
        :return:
        """

        return {"year": self.year}
