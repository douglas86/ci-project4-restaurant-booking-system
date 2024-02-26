from django.core.management import call_command
from django.test import TestCase

from home.models import ChefSpecial
from . import views


class TestMenu(TestCase, views.MenuView):
    """
    This test method is going to be used to test if I am getting data from db

    Tests:
    Test if data comes from ChefSpecial database
    Test if the correct menu comes through when slug is passed in
    Test if menu_type is equal to slug
    """

    fixtures = ["home/fixtures/chef_specials.json"]
    slug = views.MenuView.slug

    def test_decide_on_breakfast_menu(self):
        """
        Test if the breakfast menu is returned simulating self.slug
        """

        meal = views.MenuView.decide_on_meal(self)

        self.assertEqual(
            meal[0],
            "Breakfast Menu",
            msg="Test if the correct slug is passed and the correct meal is returned",
        )

    def test_decide_on_lunch_menu(self):
        """
        Test if the lunch menu is returned simulating self.slug change
        """
        self.slug = "lunch"
        meal = views.MenuView.decide_on_meal(self)

        self.assertEqual(meal[0], "Lunch Menu", msg="Test if Lunch menu is returned")

    def test_decide_on_supper_menu(self):
        """
        Test if the supper menu is returned simulating self.slug change
        """

        self.slug = "supper"
        meal = views.MenuView.decide_on_meal(self)

        self.assertEqual(
            meal[0],
            "Supper Menu",
            msg="Test if Supper Menu is returned based on slug change",
        )

    def test_menu_type_breakfast(self):
        """
        Test if the menu_type returned is the breakfast_menu
        """

        menu = views.MenuView.breakfast_meal(self)[0]

        self.assertEqual(
            menu.title(), "Breakfast Menu", msg="Breakfast menu get returned"
        )

    def test_menu_type_lunch(self):
        """
        Test if the menu_type returned is the lunch_menu
        """

        menu = views.MenuView.lunch_meal(self)[0]

        self.assertEqual(menu.title(), "Lunch Menu", msg="Lunch menu gets returned")

    def test_menu_type_supper(self):
        """
        Test if the menu_type returned is the supper_menu
        """

        menu = views.MenuView.supper_meal(self)[0]

        self.assertEqual(menu.title(), "Supper Menu", msg="Supper menu gets returned")
