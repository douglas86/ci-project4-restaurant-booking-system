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
    slug = "breakfast"

    def test_chefspecial_database(
        self,
    ):
        """
        This will test if there is data in the database
        from chef_specials model
        """
        chef_model = ChefSpecial.objects.all()
        count_model_entries = chef_model.count()
        self.assertTrue(count_model_entries > 0, msg="The model has got entries")

    def test_correct_slug_menu(
        self,
    ):
        pass

    def test_menu_type_slug(
        self,
    ):
        pass
