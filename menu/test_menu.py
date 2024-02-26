from django.core.management import call_command
from django.test import TestCase

from home.models import ChefSpecial


class TestMenu(TestCase):
    """
    This test method is going to be used to test if I am getting data from db

    Tests:
    Test if data comes from ChefSpecial database
    Test if the correct menu comes through when slug is passed in
    Test if menu_type is equal to slug
    """

    fixtures = ["home/fixtures/chef_specials.json"]

    def __getItem__(self, items):
        """
        Special method to iterate over list, dictionaries and tuples
        """
        return items

    def filter_menu(self, served, passing_menu):
        """
        This will return True or False

        Returns True if the correct menu was returned
        Returns False if the incorrect menu was returned

        Parameters:
        served - this is a parameter from 0 to 2
        passing_menu - this is variable from 0 to 2, for if the correct value is returned

        0 - being breakfast menu
        1 - being lunch menu
        2 - being supper menu
        """

        chef_model = ChefSpecial.objects.filter(served=served)

        for i in range(len(self.__getItem__(chef_model).values())):
            menu_served = int(self.__getItem__(chef_model).values()[i]["served"])

            if passing_menu == 0 and menu_served == 0:
                return True
            elif passing_menu == 1 and menu_served == 1:
                return True
            elif passing_menu == 2 and menu_served == 2:
                return True
            else:
                return False

    def test_chefspecial_database(self):
        """
        This will test if there is data in the database
        from chef_specials model
        """
        chef_model = ChefSpecial.objects.all()
        count_model_entries = chef_model.count()
        self.assertTrue(count_model_entries > 0, msg="The model has got entries")

    def test_correct_slug_menu(self):
        """
        Testing to see if the correct menu is being returned

        Parameters to be passed to the filter_menu method
        The first parameter is the menu that you want from the database from 0 to 2
        The second parameter is to make sure that the filter function is working correctly value from 0 to 2

        0 - being breakfast menu
        1 - being lunch menu
        2 - being supper menu
        """
        self.assertTrue(
            self.filter_menu(0, 1), msg="The database is not returning the correct menu"
        )

    def test_menu_type_slug(self):
        pass
