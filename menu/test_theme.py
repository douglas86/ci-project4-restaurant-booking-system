import os
from django.test import TestCase

from menu import views


class TestTheme(TestCase, views.MenuView):
    """
    This test will test if the correct theme image is passed to template

    Tests:
    Test if the image exists
    Test if I pass a month if the correct image gets displayed
    """

    def file_exists(self, filename):
        """
        Check if the file is in existance
        """

        # varaible for filepath
        file = f"static/images/menu/{filename}"
        # check is file exists using the varaible above
        path = os.path.exists(file)

        # assertion to see if path varaible is true
        # if not true it will return the f string
        self.assertTrue(path, f"The file {filename} does not exist")

    def test_file_exists(self):
        """
        Test if file exists
        """

        # pass file to file_exists method to see if the file exists
        self.file_exists("winter.jpg")
        self.file_exists("autumn.jpg")
        self.file_exists("summer.jpeg")
        self.file_exists("spring.jpg")
