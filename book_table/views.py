from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .form import BookTableForm


# Create your views here.
class BookTable(LoginRequiredMixin, TemplateView):
    template_name = 'book_table/table.html'
    form_class = BookTableForm

    def get_context_data(self, **kwargs):
        return {'form': self.form_class()}
