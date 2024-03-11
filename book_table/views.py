from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
class BookTable(LoginRequiredMixin, TemplateView):
    template_name = 'book_table/table.html'
