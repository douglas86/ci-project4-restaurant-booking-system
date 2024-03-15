from django.test import TestCase

from . import views


class TestMenu(TestCase, views.MenuView):
    """
    Test if the correct menu is returned from a menu model
    :param model: The menu model
    :param MenuView: The main menu view for fetching methods for testing
    """

    # populate database
    fixtures = ['home/fixtures/chef_specials.json', 'menu/fixtures/menu.json']

    def start_gathering_data(self):
        """
        Starts to gather data from the database
        :return:
        """

        # fetch methods from MenuView for testing
        # this will also populate the menu list in MenuView class
        self.get_chef_special()
        self.get_menu()

        # once the menu view has been populated, it will then return it
        return self.menu

    def check_menu_data(self):
        """
        This will be a for loop that will return True or False
        based on if the served value is correct
        :return:
        """

        # this will reset the menu list from MenuView
        #  before the logic runs below
        self.menu = []

        # iterate over a menu list from views
        for items in self.start_gathering_data():
            # iterate over items data for key value pairs
            for key, value in items.items():
                # only check a key of served
                if key == 'served':
                    # check if value and menu_type are equal
                    if self.menu_type == value:
                        return True
                    else:
                        return False

    def test_breakfast(self):
        """
        Testing if a breakfast menu is correct
        :return:
        """

        print('Testing breakfast menu')

        # simulate changing of slug for a breakfast menu
        self.slug = 'breakfast'
        # this is the variable to be filtered in a database
        self.menu_type = 0

        # assertion to validate if correct menu
        self.assertEqual(self.check_menu_data(), True)

    def test_lunch(self):
        """
        Testing if the lunch menu is correct
        :return:
        """

        print('Testing lunch menu')

        # simulate changing of slug for a lunch menu
        self.slug = 'lunch'
        # this is the variable to be filtered in a database
        self.menu_type = 1

        # assertion to validate if correct menu
        self.assertEqual(self.check_menu_data(), True)

    def test_supper(self):
        """
        Testing if the supper menu is correct
        :return:
        """

        print('Testing supper menu')

        # simulate changing of slug for a supper menu
        self.slug = 'supper'
        # this is the variable to be filtered in a database
        self.menu_type = 2

        # assertion to validate if correct menu
        self.assertEqual(self.check_menu_data(), True)

    def test_starter(self):
        """
        Testing if the starter menu is correct
        :return:
        """

        print('Testing starter menu')

        # simulate changing of slug for a starter menu
        self.slug = 'starter'
        # this is the variable to be filtered in a database
        self.menu_type = 3

        # assertion to validate if correct menu
        self.assertEqual(self.check_menu_data(), True)

    def test_alcohol(self):
        """
        Testing if the alcohol menu is correct
        :return:
        """

        print('Testing alcohol menu')

        # simulate changing of slug for an alcohol menu
        self.slug = 'alcohol'
        # this is the variable to be filtered in a database
        self.menu_type = 4

        # assertion to validate if correct menu
        self.assertEqual(self.check_menu_data(), True)
