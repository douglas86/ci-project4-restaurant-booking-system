from threading import Thread

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView, FormView, CreateView

from .form import BookTableForm
from .models import Customer


# Create your views here.
class BookTableView(LoginRequiredMixin, TemplateView, FormView):
    template_name = 'book_table/table.html'
    form_class = BookTableForm

    def get_context_data(self, **kwargs):
        """
        This method is used to render data to the template context
        :param kwargs:
        :return:
        """

        return {'form': self.form_class()}


class BookTableCreateView(LoginRequiredMixin, CreateView, Thread):
    """
    This view is for posting data to the Customer Model
    """

    model = Customer
    template_name = 'book_table/table.html'
    form_class = BookTableForm
    success_message = "You have successfully booked your table"

    def form_valid(self, form):
        """
        This method is used to save the form to the Customer Model
        only if it is valid
        :param form:
        :return:
        """

        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        This method is used to redirect you to the table url
        when the form is submitted and successfully saved
        :return:
        """
        messages.success(self.request, self.success_message)
        return reverse('book_table:table')
