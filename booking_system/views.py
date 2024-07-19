import datetime

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView

from .forms import UsernameResetPasswordForm, ChangePasswordForm


class UsernamePasswordResetView(View):
    form_class = UsernameResetPasswordForm
    template_name = 'account/password_reset.html'

    # fetches current date of computer
    today = datetime.date.today()
    # fetches current hour based off the variable above
    current_hour = datetime.datetime.now().strftime("%H")
    # fetches current year based off the variable above
    year = today.year

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'year': self.year, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            temporary_password = form.save(request)
            return render(request, 'account/password_reset_done.html',
                          {'temporary_password': temporary_password})
        return render(request, self.template_name, {'form': form})


class ChangePasswordView(LoginRequiredMixin, FormView):
    form_class = ChangePasswordForm
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
