from django.views.generic import TemplateView


class MenuView(TemplateView):
    """
    This view is responsible for rendering the menu from db to the template
    """

    template_name = 'menu/menu.html'
    slug = 'breakfast'

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
