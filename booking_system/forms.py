from django import forms
from django.contrib.auth.models import User


class UsernameResetPasswordForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)

    def save(self, request):
        username = self.cleaned_data['username']

        try:
            user = User.objects.get(username=username)
            temporary_password = User.objects.make_random_password()
            user.set_password(temporary_password)
            user.save()
            return temporary_password
        except User.DoesNotExist:
            raise forms.ValidationError('Username does not exist')


class ChangePasswordForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', max_length=150)
    temporary_password = forms.CharField(widget=forms.PasswordInput)

    def save(self, request):
        temporary_password = self.cleaned_data['temporary_password']
        user = request.POST['username']
        new_password = self.cleaned_data['password']

        if user.check_password(temporary_password):
            user.set_password(new_password)
            user.save()
            return new_password
        else:
            raise forms.ValidationError('Temporary password is incorrect.')
