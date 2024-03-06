import base64
import os

from django.test import TestCase

from menu import views


def convert_to_base64(image):
    """
    Converts image to base64 string for testing or comparison
    """

    # opens and convert file to base64
    with open(image, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    return image_data


def check_correct_theme(month, image):
    """
    check if the correct theme image was returned
    """

    # variable for a file path
    file = f"static/images/menu/{image}"
    # variable to return the filepath of the image in views.MenuView
    displayed_file = views.images_to_be_displayed(month)

    # variables to convert image to base64 string
    image_based_on_month = convert_to_base64(displayed_file)
    image_passed = convert_to_base64(file)

    # check strings are equal
    if image_based_on_month == image_passed:
        return True
    else:
        return False


class TestTheme(TestCase, views.MenuView):
    """
    This test will test if the correct theme image is passed to template

    Tests:
    Test if the image exists
    Test if I pass a month if the correct image gets displayed
    """

    def file_exists(self, filename):
        """
        Check if the file is in existence
        """

        # variable for filepath
        file = f"static/images/menu/{filename}"
        # check is file exists using the variable above
        path = os.path.exists(file)

        # assertion to see if path variable is true
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

    def test_correct_file_returned(self):
        """
        Test if the correct file is returned
        """

        # assertion to check if the month is correct with the image returned
        self.assertTrue(
            check_correct_theme(1, "winter.jpg"),
            "The file and the month do not match",
        )
