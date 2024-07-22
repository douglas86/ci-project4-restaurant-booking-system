import datetime

from django.views.generic import TemplateView


# Create your views here.
class AboutView(TemplateView):
    """
    About view to render about a restaurant to template
    """

    template_name = 'about/about.html'

    today = datetime.date.today()
    current_hour = datetime.datetime.now().strftime("%H")
    year = today.year

    def get_context_data(self, **kwargs):
        """
        built in method used to render data to template
        :param kwargs:
        :return:
        """

        return {"year": self.year}
