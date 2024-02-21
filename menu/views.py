import datetime
from django.views.generic import TemplateView

from home.models import ChefSpecial


# Create your views here.
class MenuView(TemplateView):
    """
    This is the view for the Menu to be displayed
    """
    template_name = 'menu/menu.html'

    today = datetime.date.today()  # gets current data of laptop
    current_hour = datetime.datetime.now().strftime(
        '%H')  # gets the current hour only

    def breakfast_meal(self):
        return ChefSpecial.objects.filter(served=0)

    def lunch_meal(self):
        return ChefSpecial.objects.filter(served=1)

    def supper_meal(self):
        return ChefSpecial.objects.filter(served=2)

    def decide_on_meal(self):
        if int(self.current_hour) >= 18:
            return self.supper_meal()  # filters all supper meals
        elif int(self.current_hour) >= 12:
            return self.lunch_meal()  # filters all lunch meals
        elif int(self.current_hour) >= 8:
            return self.breakfast_meal()  # filters all breakfast meals
        else:
            return 3  # returns the default image

    def get_queryset(self):
        return self.decide_on_meal()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meals = ['breakfast', 'lunch', 'supper']
        # gets the url path which is a key of slug that was passed
        context['slug'] = self.kwargs['slug']

        print('context', self.get_queryset())

        # swi = switch(context)

        return {'meals': meals, 'context': context, 'queryset': self.get_queryset()}


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
