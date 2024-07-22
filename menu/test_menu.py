from django.test import TestCase

from . import views


class TestMenu(TestCase, views.MenuView):
    """
    Test if the correct menu is returned from a menu model
    :param model: The menu model
    :param MenuView: The main menu view for fetching methods for testing
    """

    fixtures = ['home/fixtures/chef_specials.json', 'menu/fixtures/menu.json']

    def change_slug(self, new_slug_value, menu_type):
        """
        This method is used to simulate the change of slug and menu_type value
        :param new_slug_value:
        :param menu_type:
        :return:
        """

        self.slug = new_slug_value
        self.menu_type = menu_type

    def fetch_data(self, data):
        """
        This method is used to fetch and return data from the menu model
        :param data:
        :return:
        """

        for item in data:
            for key, value in item.items():
                if key == 'served':
                    self.assertEqual(value, self.menu_type)

    def test_breakfast(self):
        """
        Testing if the breakfast menu is returned correctly
        :return:
        """

        print('Testing breakfast')

        self.change_slug('breakfast', 0)
        data = self.get_data()
        self.fetch_data(data)

    def test_lunch(self):
        """
        Testing if the lunch menu is returned correctly
        :return:
        """

        print('Testing lunch')

        self.change_slug('lunch', 1)
        data = self.get_data()
        self.fetch_data(data)

    def test_supper(self):
        """
        Testing if the supper menu is returned correctly
        :return:
        """

        print('Testing supper')

        self.change_slug('supper', 2)
        data = self.get_data()
        self.fetch_data(data)

    def test_alcohol(self):
        """
        Testing if the alcohol menu is returned correctly
        :return:
        """

        print('Testing alcohol')

        self.change_slug('alcohol', 3)
        data = self.get_data()
        self.fetch_data(data)

    def test_starter(self):
        """
        Testing if the starter menu is returned correctly
        :return:
        """

        print('Testing starter')

        self.change_slug('starter', 4)
        data = self.get_data()
        self.fetch_data(data)
