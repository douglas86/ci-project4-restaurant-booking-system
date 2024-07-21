from django.urls import reverse


def action_url(request):
    return {
        'action_url': reverse('submit_form')
    }
