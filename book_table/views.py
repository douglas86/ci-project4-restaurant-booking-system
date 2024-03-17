from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, CreateView

from .form import BookTableForm
from .models import Customer


# Create your views here.


class BookTableCreateView(LoginRequiredMixin, CreateView):
    """
    This view is used to write data to the database
    """

    # model to be used
    model = Customer
    # form to be used called from form.py
    form_class = BookTableForm
    # when form is valid send a success message
    success_message = "You have successfully booked your table"

    def get_queryset(self):
        """
        Built in method normally used to gather data from the database
        :return:
        """

        # counts how many records are in db based on user
        queryset = Customer.objects.filter(user=self.request.user).count()

        return queryset

    def get_success_url(self):
        """
        Built in method normally runs on form validation success
        :return:
        """

        # send a success message to template
        messages.success(self.request, self.success_message)
        return reverse('book_table:table')

    def form_valid(self, form):
        """
        Built in method normally used to validate the form
        :param form:
        :return:
        """

        # form validation check
        if self.get_queryset() <= 0:
            # save form only if there is no booking for the current day
            # based on logged-in user
            instance = form.save(commit=False)
            instance.user = self.request.user
        else:
            # return error message if there is already an entry in db
            self.success_message = 'You have already booked please choose anther day'
            messages.error(self.request, self.success_message)
            return redirect('book_table:table')
        return super().form_valid(form)


class BookTableView(LoginRequiredMixin, TemplateView, FormView):
    """
    This view is used to read and render data from database to template
    """

    # template to send data to
    template_name = 'book_table/table.html'
    # form to be used called from form.py
    form_class = BookTableForm

    def get_queryset(self):
        """
        Built in method used to fetch data from a database
        :return:
        """

        pass

    def get_context_data(self, **kwargs):
        """
        Built in method used to render data to template
        :param kwargs:
        :return:
        """

        return {'form': self.form_class()}
