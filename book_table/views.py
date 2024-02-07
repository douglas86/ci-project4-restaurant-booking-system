from django.views.generic import TemplateView


# Create your views here.
class BookTable(TemplateView):
    template_name = 'book_table/table.html'
