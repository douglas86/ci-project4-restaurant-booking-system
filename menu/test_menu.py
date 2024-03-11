from django.test import TestCase

from . import views


class TestMenu(TestCase, views.MenuView):
    """
    Test the menu functionality of my site
    """

    fixtures = ['home/fixtures/chef_specials.json', 'menu/fixtures/menu.json']

    def start_gathering_data(self):
        """
        Starts to gather data from a database
        :return:
        """

        pass

    def test_breakfast(self):
        """
        Tests:
        - a Breakfast menu returned
        - with a special menu

        :return:
        """

        pass

    def test_lunch(self):
        pass

    def test_supper(self):
        pass

    def test_starter(self):
        pass

    def test_alcohol(self):
        pass

# class TestMenu(TestCase, views.MenuView):
#     """
#     This test method is going to be used to test if I am getting data from db
#
#     Tests:
#     Test if data comes from ChefSpecial database
#     Test if the correct menu comes through when slug is passed in
#     Test if menu_type is equal to slug
#     """
#
#     fixtures = ["home/fixtures/chef_specials.json"]
#     slug = views.MenuView.slug
#
#     def test_decide_on_breakfast_menu(self):
#         """
#         Test if the breakfast menu is returned simulating Slug
#         """
#
#         meal = views.MenuView.decide_on_meal(self)
#
#         self.assertEqual(
#             meal[0],
#             "Breakfast Menu",
#             msg="Test if the correct slug is passed and the correct meal is returned",
#         )
#
#     def test_decide_on_lunch_menu(self):
#         """
#         Test if the lunch menu is returned simulating slug change
#         """
#         self.slug = "lunch"
#         meal = views.MenuView.decide_on_meal(self)
#
#         self.assertEqual(meal[0], "Lunch Menu", msg="Test if Lunch menu is returned")
#
#     def test_decide_on_supper_menu(self):
#         """
#         Test if the supper menu is returned simulating slug change
#         """
#
#         self.slug = "supper"
#         meal = views.MenuView.decide_on_meal(self)
#
#         self.assertEqual(
#             meal[0],
#             "Supper Menu",
#             msg="Test if Supper Menu is returned based on slug change",
#         )
#
#     def test_menu_type_breakfast(self):
#         """
#         Test if the menu_type returned is the breakfast_menu
#         """
#
#         menu = views.breakfast_meal()[0]
#
#         self.assertEqual(
#             menu.title(), "Breakfast Menu", msg="Breakfast menu get returned"
#         )
#
#     def test_menu_type_lunch(self):
#         """
#         Test if the menu_type returned is the lunch_menu
#         """
#
#         menu = views.lunch_meal()[0]
#
#         self.assertEqual(menu.title(), "Lunch Menu", msg="Lunch menu gets returned")
#
#     def test_menu_type_supper(self):
#         """
#         Test if the menu_type returned is the supper_menu
#         """
#
#         menu = views.supper_meal()[0]
#
#         self.assertEqual(menu.title(), "Supper Menu", msg="Supper menu gets returned")
