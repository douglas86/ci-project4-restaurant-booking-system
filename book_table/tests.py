from django.test import TestCase, Client
from model_bakery import baker

from .models import Customer


# Create your tests here.
class TestBookTable(TestCase):
    """
    Tests to be run:
    Test if the logged-in user is able to submit a form
    Test if the logged-out user is able to submit a form
    Test if you can access the book table page if not logged in
    """

    def setUp(self):
        """
        Special test case to set up the db for testing
        :return:
        """
        self.client = Client()
        self.create_user = self.client.post(
            "/accounts/signup/", {"username": "test", "password": "123456"}
        )
        self.customer = baker.make('Customer')

    def test_using_customer(self):
        """
        Test method using baked model
        :return:
        """
        self.assertIsInstance(self.customer, Customer)
