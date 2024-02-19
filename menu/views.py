from django.views.generic import TemplateView


# Create your views here.
class MenuView(TemplateView):
    template_name = 'menu/menu.html'

    def get_context_data(self, **kwargs):
        meals = ['breakfast', 'lunch', 'supper']
        context = self.kwargs['slug']

        switch(context)

        return {'meals': meals, 'context': context}


def switch(context):
    if context == 'breakfast':
        return breakfast()
    elif context == 'lunch':
        return lunch()
    elif context == 'supper':
        return supper()


def breakfast():
    print('breakfast')


def lunch():
    print('lunch')


def supper():
    print('supper')
