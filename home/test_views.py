from django.test import TestCase

from .models import ChefSpecial


class TestViews(TestCase):
    fixtures = ["chef_specials"]
    current_hour = 0

    def get_served(self):
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
        Gathers data from a database based on filter
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
        # change current hour variable
        self.current_hour = 8

        print("Breakfast Meals")

        for meal in self.get_queryset():
            self.assertEqual(meal["served"], 0)

        print("Breakfast Meals Passed")

    def test_check_data_returned_lunch_meals(self):
        # change current hour variable
        self.current_hour = 12

        print("Lunch Meals")

        for meal in self.get_queryset():
            self.assertEqual(meal["served"], 1)

        print("Lunch Meals Passed")

    def test_check_data_returned_supper_meals(self):
        # change current hour variable
        self.current_hour = 18

        print("Supper Meals")

        for meal in self.get_queryset():
            self.assertEqual(meal["served"], 2)

        print("Supper Meals Passed")
