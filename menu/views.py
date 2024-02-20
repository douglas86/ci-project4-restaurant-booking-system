from django.views.generic import TemplateView


# Create your views here.
class MenuView(TemplateView):
    template_name = 'menu/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meals = ['breakfast', 'lunch', 'supper']
        # gets the url path which is a key of slug that was passed
        context['slug'] = self.kwargs['slug']

        print('context', context)

        # swi = switch(context)

        return {'meals': meals, 'context': context}


def switch(context):
    if context == 'breakfast':
        return breakfast()
    elif context == 'lunch':
        return lunch()
    elif context == 'supper':
        return supper()


def breakfast():
    menu = {'title': 'Breakfast Menu', 'name': 'This is breakfast',
            'ingredients': ['one', 'two', 'three'], 'price': 23}
    return menu


def lunch():
    print('lunch')


def supper():
    print('supper')
