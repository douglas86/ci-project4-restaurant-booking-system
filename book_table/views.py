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
    # this will only send paginate_by number to template at once
    paginate_by = 5

    def get_queryset(self):
        """
        Built in method used to fetch data from a database
        :return:
        """

        customer = Customer.objects.filter(user=self.request.user).values()
        data = []
        data_items = {}

        # iterate over Customer model
        for key, value in customer[0].items():
            # convert model into a usable format
            # only convert items in a model that have a datatime attribute
            try:
                data_items[key] = value.strftime('%d %B %Y %H:%M')
            # if no datatime attribute leave item as is
            except AttributeError:
                data_items[key] = value

        # push data_items to data list
        data.append(data_items)

        return data

    def get_context_data(self, **kwargs):
        """
        Built in method used to render data to template
        :param kwargs:
        :return:
        """

        # context variable for storing all kwargs
        # this variable makes it easier to send to template
        context = super(BookTableView, self).get_context_data(**kwargs)

        context['customer'] = self.get_queryset()

        return {'form': self.form_class(), 'context': context}
