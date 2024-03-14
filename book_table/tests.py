from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory


class TestBookTableCreate(TestCase):
    """
    Tests:
    - Test if I can access the protected page if I am a user
    - Test if I can access the protected page if I am an Anonymous user
    - Test if I can post a form if I am a user
    - Test if I can post a form if I am an Anonymous user
    """

    def setUp(self):
        """
        Set up the test cases for users
        :return:
        """

        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', email='test@gmail.com', password='123456')

    def test_protected_page_user(self):
        """
        Test if I can access the protected if I am a user of the site
        :return:
        """

        pass

    def test_protected_page_anonymous(self):
        """
        Test if I can access the protected if I am an Anonymous user
        :return:
        """

        pass

    def test_posting_form_user(self):
        """
        Test if I can post a form if I am a logged-in user
        :return:
        """

        pass

    def test_posting_form_anonymous(self):
        """
        Test if I can post a form if I am an Anonymous user
        :return:
        """

        pass

    # def test_details(self):
    #     request = self.factory.get('/table/')
    #     # request.user = self.user
    #     request.user = AnonymousUser()
    #     # data = {'seats': 1, "time_slots": "2024-02-15T13:20:30+03:00"}
    #     # response = BookTableCreateView(form=data)
    #     response = BookTableCreateView.as_view()(request)
    #     self.assertEqual(response.status_code, 200)

# Create your tests here.
# class TestBookTable(TestCase, BookTableCreateView):
#     """
#     Tests to be run:
#     Test if the logged-in user is able to submit a form
#     Test if the logged-out user is able to submit a form
#     Test if you can access the book table page if not logged in
#     """
#
#     form_class = BookTableForm
#     url = '/table'
#
#     def setUp(self):
#         """
#         Special test case to set up the db for testing
#         :return:
#         """
#         self.client = Client()
#         self.create_user = self.client.post(
#             "/accounts/signup/", {"username": "test", "password": "123456"}
#         )
#         self.customer = baker.make('Customer')
#
#     def test_using_customer(self):
#         """
#         Test method using baked model
#         :return:
#         """
#         self.assertIsInstance(self.customer, Customer)
#
#     def test_form_valid(self):
#         """
#         Test method to save form only if logged-in user
#         :return:
#         """
#
#         # self.client.login(username="test", password="123456")
#         data = {"seats": 2, "time_slots": "2024-02-15T13:20:30+03:00"}
#         f = BookTableForm(instance=self.customer, data=data)
#         self.assertTrue(f.is_valid())
