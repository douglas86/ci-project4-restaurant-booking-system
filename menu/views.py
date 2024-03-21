from django.views.generic import TemplateView

from home.models import ChefSpecial
from menu.models import Menu

# variables to gather data from database
chef_specials_data = ChefSpecial.objects.all().values()
menu_data = Menu.objects.all().values()


class MenuView(TemplateView):
    """
    This view is responsible for rendering the menu from db to the template
    """

    # template to render
    template_name = 'menu/menu.html'
    # this is the url to know what menu to display
    slug = 'breakfast'
    # variable to filter data from model
    menu_type = 0
    # list to be returned once filtered correctly
    menu = []

    def change_menu_type(self):
        """
        This method is used to change the menu_type based on slug value
        :return:
        """

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

    def get_data(self):
        """
        This method is used to fetch menu and chef data from database
        :return:
        """

        # variable to iterate over menu_data
        # then it iterates over key, value pairs to filter out values based on served item
        menu_items = [i for i in menu_data for key, value in i.items() if key == 'served' and value == self.menu_type]
        # variable to iterate over chef_specials_data
        # then it iterates over key, value pairs to filter out values based on served item
        chef_items = [i for i in chef_specials_data for key, value in i.items() if
                      key == 'served' and value == self.menu_type]

        # combine the two lists into one
        self.menu = menu_items + chef_items

        return self.menu

    def get_queryset(self):
        """
        built in method used for gathering data for get_context_data
        :return:
        """

        # run method to change the variable self.menu_type
        self.change_menu_type()

        # return data to context
        return self.get_data()

    def get_context_data(self, **kwargs):
        """
        built in method used for rendering data to template
        :param kwargs:
        :return:
        """

        context = super(MenuView, self).get_context_data(**kwargs)
        # change self.slug to url path menu
        self.slug = self.kwargs['slug']

        # list for displaying menu tabs in template
        meals = ["breakfast", "starter", "lunch", "supper", "alcohol"]

        # update context dictionary with variables
        context['slug'] = self.slug
        context['menu'] = self.get_queryset()

        return {'meals': meals, 'context': context}
