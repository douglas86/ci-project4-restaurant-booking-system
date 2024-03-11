from django.test import TestCase

from . import views


class TestMenu(TestCase, views.MenuView):
    """
    Test the menu functionality of my site
    """

    # populate database
    fixtures = ['home/fixtures/chef_specials.json', 'menu/fixtures/menu.json']

    def start_gathering_data(self):
        """
        Starts to gather data from the database
        :return:
        """

        self.get_chef_special()
        self.get_menu()

        return self.menu

    def check_menu_data(self):
        """
        This will be a for loop that will return True or False
        based on if the served value is correct
        :return:
        """

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
        Tests:
        - a Breakfast menu returned
        - with a special menu

        :return:
        """

        print('Testing breakfast menu')

        self.slug = 'breakfast'
        self.menu_type = 0

        self.assertEqual(self.check_menu_data(), True)

    def test_lunch(self):
        """
        Tests:
        - a Lunch menu returned
        - with a special menu

        :return:
        """

        print('Testing lunch menu')

        self.slug = 'lunch'
        self.menu_type = 1

        self.assertEqual(self.check_menu_data(), True)

    def test_supper(self):
        """
        Tests:
        - a Supper menu returned
        - with a special menu

        :return:
        """

        print('Testing supper menu')

        self.slug = 'supper'
        self.menu_type = 2

        self.assertEqual(self.check_menu_data(), True)

    def test_starter(self):
        """
        Tests:
        - a Supper menu returned
        - with a special menu

        :return:
        """

        print('Testing starter menu')

        self.slug = 'starter'
        self.menu_type = 3

        self.assertEqual(self.check_menu_data(), True)

    def test_alcohol(self):
        """
        Tests:
        - a Supper menu returned
        - with a special menu

        :return:
        """

        print('Testing alcohol menu')

        self.slug = 'alcohol'
        self.menu_type = 4

        self.assertEqual(self.check_menu_data(), True)
