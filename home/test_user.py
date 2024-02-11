from django.test import TestCase, Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_user = self.client.post('/accounts/signup/', {'username': 'test', 'password': '123456'})

    def test_create_user(self):
        print("Creating new user")
        self.assertEqual(self.create_user.status_code, 200)

    def test_login_user(self):
        print("Logging in")
        self.assertEqual(self.create_user.status_code, 200)
