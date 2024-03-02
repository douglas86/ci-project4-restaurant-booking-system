from django.test import TestCase
from django.utils.http import base64

from menu import views


class TestTheme(TestCase, views.MenuView):
    """
    This test will test if the correct theme image is passed to template

    Tests:
    Test if the image exists
    Test if I pass a month if the correct image gets displayed
    """

    def convert_image(self, image_path):
        """
        Contert image to base64 string

        Parameters:
        image_path - this is the path of the image to be converted
        """

        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")

        return image_data

    def try_image(self, image):
        """
        Uses a try except block to see if the image is in existance
        Only pass the path of the file to this method

        Parameters:
        image - this parameter will just check if something is in existance
        """

        try:
            self.convert_image(image)
            return "file exists"
        except FileNotFoundError:
            raise FileNotFoundError

    def test_winter_image(self):
        """
        This will be to test if the winter image exists
        """

        print("Testing if winter image exists")

        self.try_image("static/images/menu/winter.jpg")
