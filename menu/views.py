import threading

from django.views.generic import TemplateView

from home.models import ChefSpecial
from menu.models import Menu


class MenuView(TemplateView):
    """
    View used for the menu page
    This will be my first implementation of multithreading operations
    """

    template_name = 'menu/menu.html'

    # this variable represents the url that I am on
    slug = 'breakfast'
    # this variable represents the menu from 0 to 4
    menu_type = 0
    # menu to return when all lists are appended
    menu = []

    def get_chef_special(self):
        """
        This method is used to get the chef special model from the database
        :return:
        """

        chef_special = ChefSpecial.objects.filter(served=self.menu_type).values()

        # loop around model and append to a menu list
        for item in chef_special:
            self.menu.append(item)

    def get_menu(self):
        """
        This method is used to get the menu model from the database
        :return:
        """

        menu = Menu.objects.filter(served=self.menu_type).values()

        # loop around model and append to a menu list
        for item in menu:
            self.menu.append(item)

    def get_queryset(self):
        """
        This is a built-in Django method used to gather
        data from the database for get_context_data
        :return:
        """

        # reset menu
        self.menu = []

        # run methods on its own separate threads
        specials = threading.Thread(target=self.get_chef_special)
        menu = threading.Thread(target=self.get_menu)

        # gathers data from a model based on slug
        if self.slug == 'breakfast':
            self.menu_type = 0
        elif self.slug == 'lunch':
            self.menu_type = 1
        elif self.slug == 'alcohol':
            self.menu_type = 3
        elif self.slug == 'starter':
            self.menu_type = 4
        else:
            self.menu_type = 2

        # start running thread
        specials.start()
        menu.start()

        # finish running thread
        specials.join()
        menu.join()

        return self.menu

    def get_context_data(self, **kwargs):
        """
        This is a built-in Django method used to send data to the template for rendering
        :param kwargs:
        :return:
        """

        # used for tabs on menu page
        meals = ["breakfast", "starter", "lunch", "supper", "alcohol"]

        context = super(MenuView, self).get_context_data(**kwargs)
        self.slug = self.kwargs["slug"]

        # store variables to context
        context['slug'] = self.slug
        context['menu'] = self.get_queryset()

        return {"meals": meals, "context": context}
