import datetime
from django.views.generic import TemplateView

from home.models import ChefSpecial


# Create your views here.
class MenuView(TemplateView):
    """
    View used for the Menu Page
    """
    template_name = 'menu/menu.html'

    # variables used for the current time
    today = datetime.date.today()  # gets current date of laptop
    current_hour = datetime.datetime.now().strftime(
        '%H')  # gets the current hour only

    def combine_menus(self, specials, additional_meals):
        lists = []

        # had to create two for loops as both of them
        # were of different data types

        # iterates over specails model from database
        # appends it to lists above
        for v in specials.values():
            dict = {}
            dict['title'] = v['title']
            dict['ingredients'] = v['ingredients']
            lists.append(dict)

        # iterate over additional_meals from a created dictionary
        # appends it to lists above
        for meals in additional_meals:
            for key, value in meals.items():
                dict = {}
                dict[key] = value
                lists.append(dict)

        return lists

    def breakfast_meal(self):
        """
        Display information for the Breakfast Menu
        """
        menu_type = "Breakfast Menu"
        specials = ChefSpecial.objects.filter(served=0)
        breakfast_menu = [
            {
                "title": "Fluffy Pancakes",
                "ingredients": [
                    "whole milk",
                    "large egg",
                    "vegatable oil",
                    "homemade pancake mix",
                    "sugar"
                ]
            },
            {
                "title": "Focaccia French Toast",
                "ingredients": [
                    "large eggs",
                    "whole eggs",
                    "pure vanilla extracts",
                    "ground cinnamon",
                    "slices of focaccia",
                    "unsalted butter",
                ]
            }
        ]
        return menu_type, self.combine_menus(specials, breakfast_menu)

    def lunch_meal(self):
        """
        Display information for the Lunch Menu
        """
        menu_type = "Lunch Menu"
        specials = ChefSpecial.objects.filter(served=1)
        lunch_menu = [
            {
                "title": "First title",
                "ingredients": ["one", "two", "three"]
            },
            {
                "title": "Second title",
                "ingredients": ["four", "five", "six"]
            }
        ]
        return menu_type, self.combine_menus(specials, lunch_menu)

    def supper_meal(self):
        """
        Display information for the Supper Menu
        """
        menu_type = "Supper Menu"
        specials = ChefSpecial.objects.filter(served=2)
        supper_menu = [
            {
                "title": "First title",
                "ingredients": ["one", "two", "three"]
            },
            {
                "title": "Second title",
                "ingredients": ["four", "five", "six"]
            }
        ]
        return menu_type, self.combine_menus(specials, supper_menu)

    def decide_on_meal(self):
        """
        dicide on the correct meal to display based on current hour
        """
        if int(self.current_hour) >= 18:
            return self.supper_meal()  # filters all supper meals
        elif int(self.current_hour) >= 12:
            return self.lunch_meal()  # filters all lunch meals
        elif int(self.current_hour) >= 8:
            return self.breakfast_meal()  # filters all breakfast meals
        else:
            return 3  # returns the default image

    def __getitem__(self, items):
        """
        Special method used to iterate over lists, dictionaries and tuples
        """
        return items

    def get_queryset(self):
        """
        Special Django method used to gather data
        """
        menu_type = self.__getitem__(self.decide_on_meal())[0]
        menu_items = self.__getitem__(self.decide_on_meal())[1]
        return menu_type, menu_items

    def get_context_data(self, **kwargs):
        """
        Special Django method used to send data to template for display
        """
        context = super().get_context_data(**kwargs)
        # variable used for dropdown list when on mobile
        # and tabs when on tablet
        meals = ['breakfast', 'lunch', 'supper']

        # updated context with name of menu type and its items
        context['menu_type'] = self.get_queryset()[0]
        context['menu_items'] = self.get_queryset()[1]

        return {
            'meals': meals, 'context': context
        }
