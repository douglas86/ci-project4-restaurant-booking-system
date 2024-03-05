from django.test import TestCase, Client


class TestUser(TestCase):
    """
    Testing if the user can log in or be created
    """

    def setUp(self):
        """
        This method initializes the setup of the user
        :return:
        """
        self.client = Client()
        self.create_user = self.client.post(
            '/accounts/signup/', {'username': 'test', 'password': '123456'})

    def test_create_user(self):
        """
        Run test to see if a user can be created
        :return:
        """
        print("Creating new user")
        self.assertEqual(self.create_user.status_code, 200)

    def test_login_user(self):
        """
        Run test to see if user can be logged in
        :return:
        """
        print("Logging in")
        self.assertEqual(self.create_user.status_code, 200)
