from django.test import TestCase

from .models import ChefSpecial


class TestViews(TestCase):
    """
    Test if the correct data is returned from one of the menus
    """

    fixtures = ["chef_specials"]
    current_hour = 0

    def get_served(self):
        """
        Return the correct number based on current hour variable
        The number is the filter for the database
        :return:
        """

        if int(self.current_hour) >= 18:
            return 2  # filters all supper meals
        elif int(self.current_hour) >= 12:
            return 1  # filters all lunch meals
        elif int(self.current_hour) >= 8:
            return 0  # filters all breakfast meals
        else:
            return 3  # returns the default image

    def get_queryset(self):
        """
        Built in method to fetch data from a database
        """

        # calls method get_served to see what meals it needs to display
        served_meals = self.get_served()

        # ternary operator to see if variable served_meals is greater than 3
        meal = (
            ChefSpecial.objects.all().filter(served=served_meals)
            if served_meals < 3
            else "Not served"
        )

        return meal.values()

    def test_check_data_returned_breakfast_meals(self):
        """
        Test if the breakfast meal is returned correctly
        :return:
        """

        # change current hour variable
        self.current_hour = 8

        print("Testing Breakfast Meals")

        # validation check to iterate over queryset returned
        # making sure that all served meals have a value of 0
        for meal in self.get_queryset():
            self.assertEqual(meal["served"], 0)

    def test_check_data_returned_lunch_meals(self):
        """
        Test if the lunch meal is returned correctly
        :return:
        """

        # change current hour variable
        # this is when lunch meal is served from
        self.current_hour = 12

        print("Testing Lunch Meals")

        # validation check to iterate over queryset returned
        # making sure that all served meals have a value of 1
        for meal in self.get_queryset():
            self.assertEqual(meal["served"], 1)

    def test_check_data_returned_supper_meals(self):
        """
        Test if the Supper meal is returned correctly
        :return:
        """

        # change current hour variable
        # this is when supper meal is served from
        self.current_hour = 18

        print("Testing Supper Meals")

        # validation check to iterate over queryset returned
        # making sure that all served meals have a value of 2
        for meal in self.get_queryset():
            self.assertEqual(meal["served"], 2)
