from django.views.generic import TemplateView

from home.models import ChefSpecial
from menu.models import Menu

chef_specials = []
menu = []


class MenuView(TemplateView):
    """
    This view is responsible for rendering the menu from db to the template
    """

    template_name = 'menu/menu.html'
    slug = 'breakfast'
    menu_type = 0

    chef_specials = chef_specials
    menu = menu

    def change_menu_type(self):
        """
        This method is used to change the menu_type based on slug value
        :return:
        """

        pass

    def fetch(self):
        """
        This method is used to fetch data from the database
        :return:
        """

        self.chef_specials = ChefSpecial.objects.all().values()
        self.menu = Menu.objects.all().values()

        for i in self.chef_specials:
            chef_specials.append(i)

        for i in self.menu:
            menu.append(i)

    def get_data(self):
        """
        This method is used to fetch menu and chef data from database
        :return:
        """

        if self.chef_specials == [] or self.menu == []:
            self.fetch()

    def get_queryset(self):
        """
        built in method used for gathering data for get_context_data
        :return:
        """

        self.get_data()

        print(self.chef_specials)
        print(self.menu)

    def get_context_data(self, **kwargs):
        """
        built in method used for rendering data to template
        :param kwargs:
        :return:
        """

        context = super(MenuView, self).get_context_data(**kwargs)

        meals = ["breakfast", "starter", "lunch", "supper", "alcohol"]

        self.get_queryset()

        return {'meals': meals}

# class MenuView(TemplateView):
#     """
#     This view is responsible for reading and rendering to the templates
#     """
#
#     # template to send data to
#     template_name = 'menu/menu.html'
#
#     # this variable represents the url that I am on
#     slug = 'breakfast'
#     # this variable represents the menu from 0 to 4
#     menu_type = 0
#     # menu to return when all lists are appended
#     menu = []
#
#     def get_chef_special(self):
#         """
#         This method is responsible for gathering data from a Chef Special model
#         """
#
#         # use the menu_type as its filter
#         # only displays its values
#         chef_special = ChefSpecial.objects.filter(served=self.menu_type).values()
#
#         # loop around model and append to a menu list
#         for item in chef_special:
#             self.menu.append(item)
#
#     def get_menu(self):
#         """
#         This method is responsible for gathering data from a Menu model
#         """
#
#         # use the menu_type as its filter
#         # only displays its values
#         menu = Menu.objects.filter(served=self.menu_type).values()
#
#         # loop around model and append to a menu list
#         for item in menu:
#             self.menu.append(item)
#
#     def get_queryset(self):
#         """
#         Built in method used for fetching data from the database
#         """
#
#         # reset a menu list on start of method
#         self.menu = []
#
#         # run methods on its own separate threads
#         specials = threading.Thread(target=self.get_chef_special)
#         menu = threading.Thread(target=self.get_menu)
#
#         # gathers data from a model based on slug
#         if self.slug == 'breakfast':
#             self.menu_type = 0
#         elif self.slug == 'lunch':
#             self.menu_type = 1
#         elif self.slug == 'alcohol':
#             self.menu_type = 3
#         elif self.slug == 'starter':
#             self.menu_type = 4
#         else:
#             self.menu_type = 2
#
#         # start running thread
#         specials.start()
#         menu.start()
#
#         # finish running thread
#         specials.join()
#         menu.join()
#
#         return self.menu
#
#     def get_context_data(self, **kwargs):
#         """
#         Built in method used for rendering data to the template
#         """
#
#         # used to display tabs on template page
#         # for the different menu items
#         meals = ["breakfast", "starter", "lunch", "supper", "alcohol"]
#
#         # context variable for storing all kwargs
#         # this variable makes it easier to send to template
#         context = super(MenuView, self).get_context_data(**kwargs)
#         # variable for changing the slug based on url
#         self.slug = self.kwargs["slug"]
#
#         # store variables to context
#         context['slug'] = self.slug
#         context['menu'] = self.get_queryset()
#
#         return {"meals": meals, "context": context}
