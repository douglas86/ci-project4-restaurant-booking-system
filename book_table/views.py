from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView

from .form import BookTableForm


# Create your views here.
class BookTableView(LoginRequiredMixin, TemplateView, FormView):
    template_name = 'book_table/table.html'
    form_class = BookTableForm
    success_url = '/table/'

    def form_valid(self, form):
        """
        This method is called when the form data has been posted.
        :param form:
        :return:
        """

        form.send_email()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        This method is used to render data to the template context
        :param kwargs:
        :return:
        """

        return {'form': self.form_class()}
