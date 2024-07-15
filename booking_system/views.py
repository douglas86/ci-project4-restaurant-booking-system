from django.shortcuts import render
from django.views import View

from .forms import UsernameResetPasswordForm


class UsernamePasswordResetView(View):
    form_class = UsernameResetPasswordForm
    template_name = 'account/password_reset.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            temporary_password = form.save(request)
            return render(request, 'account/password_reset_done.html', {'temporary_password': temporary_password})
        return render(request, self.template_name, {'form': form})
