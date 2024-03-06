import datetime

from django.utils.http import base64
from django.views.generic import TemplateView

from home.models import ChefSpecial
from menu.models import Menu


# Create your views here.
def images_to_be_displayed(month):
    """
    This function will determine what image needs to be displayed

    Parameters:
    month - this is an integer that is passed in based on the current month
    """

    # Winter - December, January, February
    if month >= 12:
        return "static/images/menu/winter.jpg"
    # Autumn - September, October, November
    elif month >= 9:
        return "static/images/menu/autumn.jpg"
    # Summer - June, July, August
    elif month >= 6:
        return "static/images/menu/summer.jpeg"
    # Spring - March, April, May
    elif month >= 3:
        return "static/images/menu/spring.jpg"
    # this section is for January and February months
    else:
        return "static/images/menu/winter.jpg"


def combine_menus(specials=None, additional_meals=None):
    """
    This will combine specails and additional_meals into one list
    """

    # get returned when the arrays have been combined for easy iteration
    # in template
    if additional_meals is None:
        additional_meals = []
    if specials is None:
        specials = []
    lists = []

    # had to create two for loops as both of them
    # were of different data types

    # iterates over a specails model from database
    # appends it to lists above
    # if I don't have a specails I can pass it an open list
    if specials:
        for v in specials.values():
            dic = {"title": v["title"], "ingredients": ", ".join(v["ingredients"])}
            lists.append(dic)

    # iterates over additional_meals from a menu model
    if additional_meals:
        for k in additional_meals.values():
            dic = {"title": k["title"], "description": k["description"]}
            lists.append(dic)

    return lists


def breakfast_meal():
    """
    Display information for the Breakfast Menu
    """

    menu_type = "Breakfast Menu"
    specials = ChefSpecial.objects.filter(served=0)
    breakfast_menu = Menu.objects.filter(menu_type=0)

    return (
        menu_type,
        combine_menus(specials, breakfast_menu),
    )


def starter_menu():
    """
    This menu will display at the top of the lunch and supper menu only
    """

    menu_type = "Starter Menu"
    starter = Menu.objects.filter(menu_type=4)

    return menu_type, combine_menus([], starter)


def lunch_meal():
    """
    Display information for the Lunch Menu
    """

    menu_type = "Lunch Menu"
    specials = ChefSpecial.objects.filter(served=1)
    lunch_menu = Menu.objects.filter(menu_type=1)

    # display starter menu on main menu for lunch
    starter = starter_menu()

    return menu_type, combine_menus(specials, lunch_menu), starter


def supper_meal():
    """
    Display information for the Supper Menu
    """

    menu_type = "Supper Menu"
    specials = ChefSpecial.objects.filter(served=2)
    supper_menu = Menu.objects.filter(menu_type=2)

    # display starter menu on main menu for supper
    starter = starter_menu()

    return menu_type, combine_menus(specials, supper_menu), starter


def alcohol():
    """
    Displays information for the alcohol menu
    """

    menu_type = "Alcohol Menu"
    alcohol_menu = Menu.objects.filter(menu_type=3)

    return menu_type, combine_menus([], alcohol_menu)


class MenuView(TemplateView):
    """
    View used for the Menu Page
    """

    # template that gets displayed when view is loaded
    template_name = "menu/menu.html"

    # variables used for the current time
    today = datetime.date.today()  # gets current date of laptop
    current_hour = datetime.datetime.now().strftime("%H")  # gets the current hour only

    # slug to determine on what menu to display based on url
    # this variable is set in get_context_data method
    slug = "breakfast"

    def __getitem__(self, items):
        """
        Special method used to iterate over lists, dictionaries and tuples
        """

        return items

    def decide_on_meal(self):
        """
        decision to be made on what menu gets displayed
        based on an url path
        """

        if self.slug == "breakfast":
            return breakfast_meal()
        elif self.slug == "lunch":
            return lunch_meal()
        elif self.slug == "alcohol":
            return alcohol()
        else:
            return supper_meal()

    def determining_month_of_year(self):
        """
        This method determines the month of the year
        Once that is determined it will pass it to the method
        images_to_be_displayed
        """

        # variable to determine the current month
        # this method returns the current month as an integer
        month = self.today.month

        # spring - March, April, May
        # Summer - June, July, August
        # Autumn - September, October, November
        # Winter - December, January, February

        return images_to_be_displayed(month)

    def themes(self):
        """
        This method will return the current theme to get_context_data
        """

        # variable for a returning image path
        image_path = self.determining_month_of_year()

        # logic for reading in the file from the image_path variable
        # and returning it as a base64 string
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")

        return image_data

    def get_queryset(self):
        """
        Special Django method used to gather data from a database
        """

        # gets menu_type and menu_items from decide_on_meal method
        menu_type = self.__getitem__(self.decide_on_meal())[0]
        menu_items = self.__getitem__(self.decide_on_meal())[1]

        # check if there is a starter menu included if not
        # return starter_menu as an empty list
        try:
            starter = self.__getitem__(self.decide_on_meal())[2]
        except IndexError:
            starter = []

        return menu_type, menu_items, starter

    def get_context_data(self, **kwargs):
        """
        Special Django method used to send data to template for display
        """

        context = super().get_context_data(**kwargs)
        # variable used for dropdown list when on mobile
        # and tabs when on tablet
        meals = ["breakfast", "lunch", "supper", "alcohol"]
        # changes self.slug to an url path
        self.slug = self.kwargs["slug"]

        # updated context with name of a menu type and its items
        context["menu_type"] = self.get_queryset()[0]
        context["menu_items"] = self.get_queryset()[1]
        context["starter_menu"] = self.get_queryset()[2]

        return {"meals": meals, "context": context, "theme": self.themes()}
