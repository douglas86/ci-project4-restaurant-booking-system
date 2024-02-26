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

    def test_menu_type_slug(self):
        """
        Test if the menu_type is the correct menu that is passed in

        Test:
        Fail test - pass in an incorrect menu
        """

        # variables to gather the instances from MenuView
        breakfast_menu = views.MenuView.breakfast_meal(self)[0]
        lunch_menu = views.MenuView.lunch_meal(self)[0]
        supper_menu = views.MenuView.supper_meal(self)[0]

        # These 3 tests check if the correct menu_type is returned
        self.assertEqual(
            breakfast_menu.title(),
            "Breakfast Menu",
            msg="Breakfast Menu must be returned from this function",
        )

        self.assertEqual(
            lunch_menu.title(),
            "Lunch Menu",
            msg="Lunch Menu must be returned from this function",
        )

        self.assertEqual(
            supper_menu.title(),
            "Supper Menu",
            msg="Supper Menu must be returned from this function",
        )
