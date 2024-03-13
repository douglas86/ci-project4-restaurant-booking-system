from django.test import TestCase, Client
from model_bakery import baker

from .form import BookTableForm
from .models import Customer
from .views import BookTableCreateView


# Create your tests here.
class TestBookTable(TestCase, BookTableCreateView):
    """
    Tests to be run:
    Test if the logged-in user is able to submit a form
    Test if the logged-out user is able to submit a form
    Test if you can access the book table page if not logged in
    """

    form_class = BookTableForm

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

    def test_form_valid(self):
        """
        Test method to save form only if logged-in user
        :return:
        """

        # self.client.login(username="test", password="123456")
        data = {"seats": 2, "time_slots": "2024-02-15T13:20:30+03:00"}
        f = BookTableForm(instance=self.customer, data=data)
        self.assertTrue(f.is_valid())
