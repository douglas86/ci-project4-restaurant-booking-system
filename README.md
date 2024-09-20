![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## [Introduction](#table-of-content)

This is Part of my Fourth Project at Code Institute.

This is a simple Restaurant Booking System, were I can book tables based on a date and time
I am also able to see the Restaurant's Menu and Chef's specials.

![heading-image.png](static/images/docs/introduction/heading-image.png)

[Live link can be found here](https://ci-booking-system-5abd35239ade.herokuapp.com/)

---

# Table of Content

- [Planning](#planning)
    - [Wireframes](#wireframes)
    - [Ux-design](#ux-design)
    - [Colour Pallet](#colour-pallet)
    - [User Stories using MOSCOW Prioritization techniques](#user-stories-using-moscow-prioritization-techniques)
    - [How to start this project locally](#how-to-start-this-project-locally)
    - [How this project was deployed to Heroku](#how-this-project-was-deployed-to-heroku)
    - [Technology Used](#technology-used)
    - [neat and clean code](#neat-and-clean-code)
- [Features](#features)
    - [Features that have been included in this project](#features-that-have-been-included-in-this-project)
        - [hamburger image on smaller devices](#hamburger-image-on-smaller-devices)
        - [Authentication](#authentication)
        - [Description of the restaurant](#description-of-the-restaurant)
        - [scrolling left and right arrows for carousel](#scrolling-left-and-right-arrows-for-carousel)
        - [table booking with booking history and next booking](#table-booking-with-booking-history-and-next-booking)
        - [deleting table records](#deleting-table-records)
    - [Future features to be added at a later stage](#future-features-to-be-added-at-a-later-stage)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
        - [Testing responsiveness of the menu page](#testing-responsiveness-of-the-menu-page)
        - [Testing the responsiveness of the about page](#testing-the-responsiveness-of-the-about-page)
        - [Testing if I can navigate to table page](#testing-if-i-can-navigate-to-table-page)
        - [Testing of updating records](#testing-of-updating-records)
        - [Testing model form for booking a table](#testing-model-form-for-booking-a-table)
            - [Html validation testing](#html-validation-testing)
            - [Css validation testing](#css-validation-testing)
            - [Wave testing for accessibility](#wave-testing-for-accessibility)
            - [lighthouse testing](#lighthouse-testing)
    - [Automated Testing](#automated-testing)
        - [Authentication](#authentication-1)
        - [Homepage](#homepage-2)
        - [Test if correct menu gets returned based on slug](#test-if-correct-menu-gets-returned-based-on-slug)
        - [Test form invalid on Booking a table page](#test-form-invalid-on-booking-a-table-page)
        - [Test form valid on Booking a table page](#test-form-valid-on-booking-a-table-page)
        - [Test protected pages against anonymous user](#test-protected-pages-against-anonymous-user)
        - [Test protected pages against users that are logged in or not](#test-protected-pages-against-users-that-are-logged-in-or-not)
- [Bugs](#bugs)
    - [The text is not aligned correctly to the Authentication Icon](#the-text-is-not-aligned-correctly-to-the-authentication-icon)
    - [Labels are not correctly sitting next to the Icons](#labels-are-not-correctly-sitting-next-to-the-icons)
    - [Problem with Hamburger Menu](#problem-with-hamburger-menu)
    - [Hamburger menu jumps as I try and open and close menu](#hamburger-menu-jumps-as-i-try-and-open-and-close-menu)
    - [Operational error in database as trying to run auto test](#operational-error-in-database-as-trying-to-run-auto-test)
    - [Carousel image not being aligned correctly](#carousel-image-not-being-aligned-correctly)
    - [Favicon icon not displaying](#favicon-icon-not-displaying)
    - [Heroku auto refreshing unnecessarily](#heroku-auto-refreshing-unnecessarily)
    - [Navbar not at top of screen](#navbar-not-at-top-of-screen)
    - [Performance issues in page loading](#performance-issues-in-page-loading)
    - [Too many connections to database at once](#too-many-connections-to-database-at-once)
    - [styling of homepage](#styling-of-homepage)
    - [carousel arrows](#carousel-arrows)
    - [copyright text not showing in footer](#copyright-text-not-showing-in-footer)
    - [copyright text overlapping with developer content](#copyright-text-overlapping-with-developer-content)
    - [next booking not being displayed](#next-booking-not-being-displayed)
    - [not recognizing daylight savings mode](#not-recognizing-daylight-savings-mode)
    - [table over lapping on smaller devices](#table-over-lapping-on-smaller-devices)
    - [TypeError in console](#typeerror-in-console)
    - [Am I Responsive does not display image](#am-i-responsive-does-not-display-image)
- [Credits](#credits)

---

## [Planning](#table-of-content)

These Wireframes and UX Designs were designed on Figma

### [Wireframes](#planning)

#### Homepage

![wireframe-homepage.png](static/images/docs/planning/wireframe-homepage.png)

- The message box in the middle is for where the carousel will go

#### Menu Page

![wireframe-menu-page.png](static/images/docs/planning/wireframe-menu-page.png)

- The box in the middle is to represent the menu
- breakfast, lunch, supper, alcohol or starter menu

#### About Page

![wireframe-about.png](static/images/docs/planning/wireframe-about.png)

- The box in the middle is where I will place a section about our humble beginnings

#### Book a table Page

![wireframe-book-table.png](static/images/docs/planning/wireframe-book-table.png)

- The big box in the middle is for all booking history
- The top box on the left-hand side is for the last booking
- The one under that is for vouchers
- The voucher system has been taken out of the equation for now

### [Ux-design](#planning)

#### Home Page

![ux-homepage.png](static/images/docs/planning/ux-homepage.png)

#### Menu Page

![ux-menu-page.png](static/images/docs/planning/ux-menu-page.png)

#### Book Table Page

![ux-book-table.png](static/images/docs/planning/ux-book-table.png)

#### About Page

![ux-about.png](static/images/docs/planning/ux-about.png)

### ERD diagram

![ERD_diagram.png](static/images/docs/planning/ERD_diagram.png)

- I have taken the voucher model out
- as of now it became an unnecessary feature

### [Colour Pallet](#planning)

![color-pallet.png](static/images/docs/planning/color-pallet.png)

Click [here](https://coolors.co/9f7e69-d2bba0-f2efc7-f7ffe0-ffeee2) to see where I got this color pallet from

How I came by this color Pallet:

I went onto Google and googled: What would be a nice color theme for an exclusive restaurant

- See
  results [here](https://www.google.com/search?client=firefox-b-d&q=what+would+be+a+nice+color+theme+for+an+exclusive+restaurant&dlnr=1&sei=bazIZcmsAvKxhbIP18mBkAE)
- I had thought that a nice light gray would've worked well as some of the colors used with my UX design was already a
  grayish color

### [User Stories using MOSCOW Prioritization techniques](#planning)

This Project was done in incremental stages, trying my best to follow the agile methods.

Header

![Screenshot from 2024-02-04 14-57-56.png](static/images/docs/moscow-header.png)

kanban board

![kanban-board.png](static/images/docs/planning/kanban-board.png)

Explanation of the columns on the board:

- Backlog: this is where the issues start from when they are created
- Ready: these issues are ready to be picked up so work can be conducted
- In Progress: This is what is busy being worked on
- In review: This is the stage were the testing gets done
- Done: for all completed issues

Milestones

This project was done in incremental stages, building it page by page.
As such, the milestone percentage will change slightly in each iteration.

![milestones.png](static/images/docs/planning/milestones.png)

This is when I am 46% done, but only the header issue was added

![milestones-header-46.png](static/images/docs/planning/milestones-header-46.png)

Footer

- The footer had only three issues in it, so I only labeled them as Must-have
- There was also an issue that I created for Documentation

![moscow-footer.png](static/images/docs/planning/moscow-footer.png)

- Once the footer had been completed, 84% was done.

![milestone-footer.png](static/images/docs/planning/milestone-footer.png)

Homepage

- There were only four issues added for this section
- As I didn't plan on doing a lot of work here

![moscow-homepage.png](static/images/docs/planning/moscow-homepage.png)

- The milestone was taken after the homepage was done
- When the Menu Page and About Page were added as issues

![milestone-homepage.png](static/images/docs/planning/milestone-homepage.png)

Menu Page

- I created 10 sticky notes to decide on what I wanted for the issues
- Once I knew what I wanted, then created the issues for the kanban board,
- Sorting them out into Moscow priorities sticking with 60% Must-have
- I have also created an issue for the documentation
- Which I will do after all required issues are done

Sticky notes on Figma to plan what sort of issues I am wanting to solve

![moscow-menu-planning.png](static/images/docs/planning/moscow-menu-planning.png)

Once the Issues were created, I gave them their labels using MOSCOW priorities

![moscow-menu-create-issues.png](static/images/docs/planning/moscow-menu-create-issues.png)

After all, planning is in place the milestone section shows percentage done

![moscow-menu-milestone.png](static/images/docs/planning/moscow-menu-milestone.png)

About Page

- Screenshot of the issues board using moscow priorities

![moscow-about-issues.png](static/images/docs/planning/moscow-about-issues.png)

- The kanban board in action

![kanban-about.png](static/images/docs/planning/kanban-about.png)

- When the last section was added, this is the milestone thus far

![milestones-about.png](static/images/docs/planning/milestones-about.png)

Table booking Page

- Screenshot of the kanban board when busy on the bookings page

![kanban-table-booking.png](static/images/docs/planning/kanban-table-booking.png)

- Screenshot of the Milestone project board

![milestones-table-booking.png](static/images/docs/planning/milestones-table-booking.png)

### [How to start this project locally](#planning)

- when using ssh
- git clone git@github.com: douglas86/ci-project4-restaurant-booking-system.git
- when using http
- git clone https://github.com/douglas86/ci-project4-restaurant-booking-system.git
- make sure to have a look at the runtime.txt file to see what version of python I am using
- then create a virtual environment with that python version
- to see if a virtual environment has been created, the words venv in brackets will appear in the terminal
- as I am using pycharm, the virtual environment will start automatically when I start my IDE
- then install all the packages needed for this project using the following command
- pip install -r requirements.txt
- to start the Django server, run the following command
- create an env.py file this is used to store all environment variables
- create the variable needs for this project see the image below
- placing the name of the variables in the empty quotation marks
- make sure to set DJANGO_DEBUG = True
- django secret keys should never be committed to GitHub
- so if you need one, follow the following link
- [generate a new secret key](https://www.makeuseof.com/django-secret-key-generate-new/#:~:text=You%20can%20accidentally%20make%20your,are%20still%20learning%20about%20GitHub.)
- Then go to [elephantSQL](https://www.elephantsql.com/)
- And create a new database instance to make sure that the version of PostgresSQL is greater than 12
- Once created, then copy and paste the url in the env.py for the DATABASE_URL string
- once that is done, then you can run the command below to run the server
- python manage.py runserver
- you can use ctrl + click on the server name that should open up a web browser at the correct port

env.py

![env.png](static/images/docs/env.png)

### [How this project was deployed to Heroku](#planning)

- head over to [Heroku Dashboard](https://dashboard.heroku.com/apps)
- create a new app and add all the environment variables to your config vars
- make sure to add DISABLE_COLLECT STATIC with the value of 1
- if this variable is not used, Heroku will spit out an error
- change DJANGO_DEBUG with the value of False
- make sure that there is a runtime.txt file
- this will tell Heroku what version of python to use
- make sure that requirements.txt is updated
- make sure to see if Heroku hasn't automatically added a build pack for PostgresSQL
- if it has deleted it as this project is using elephantSQL instead
- connect GitHub and the repo to Heroku and build the project

### [Technology Used](#planning)

- HTML/CSS - HTML templating and CSS styling
- Python—logic used in this project
- JavaScript—Used for Models and other front end logic
- Django - Python Framework for developing this project
- PostgresSQL - using elephantSQL for database
- Heroku - cloud deployment
- GitHub - version control
- Pycharm - IDE for development

### [neat and clean code](#planning)

- Code always needs to be kept neat and tidy
- As such, I have tried my best to organize my code readably

order of imports

- standard libraries
- third-party libraries
- django imports
- local imports
- imported based on logic: like try/except or if statements

[reference](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#:~:text=Put%20imports%20in%20these%20groups,import%20objects%20in%20each%20section.)

order of methods in classes

- magic methods: def __magic_method__(self)
- public methods: def public_method(self)
- class method: class within class
- private methods: def private_methods(self): helper functions
- get_queryset: this is used for gathering data for get_context_data
- get_context_data: this is for rendering data to a template file

order of classes within files:

- follow CRUD operations for views
- follow alphabetical order for all other files

order in test files:

- setUp method
- helper functions: in alphabetical order, then grouped together by relevance
- tests: in alphabetical order

[reference](https://stackoverflow.com/questions/10289461/what-is-a-good-way-to-order-methods-in-a-python-class)

---

## [Features](#table-of-content)

### [Features that have been included in this project](#features)

#### [hamburger image on smaller devices](#features)

When screen gets minimised all content gets reduced to hamburger menu

![header-hamburger-menu.png](static/images/docs/features/header-hamburger-menu.png)

- This has since been changed to the three horizontal lines
- as it made for better UX design

#### [Authentication](#features)

When the user is not logged in, this image will be displayed

![header-logout-image.png](static/images/docs/features/header-logout-image.png)

When the user is logged in, a welcome message will be displayed with a different image

![header-login-image.png](static/images/docs/features/header-login-image.png)

#### [Description of the restaurant](#features)

- Created a description about the restaurant
- With its very beginnings

![description.png](static/images/docs/features/description.png)

#### [scrolling left and right arrows for carousel](#features)

- There is an arrow that you can use to scroll left and right
- I have tried to blend it in to the rest of the site

![scrolling_left_right_arrows_carousel.png](static/images/docs/features/scrolling_left_right_arrows_carousel.png)

- The design layout has changed slightly since this image
- I have added it as a card, giving it better styling

#### [table booking with booking history and next booking](#features)

- You can only book a table if you are logged in
- The icon in the header will not be displayed if you are logged out
- There is a section to show all history of your bookings
- I have left out pagination, as I will be implementing it at a later date
- Displaying all history bookings as a table
- I have also added it to display your next booking
- But at this time it will only display the last booking that you have booked for
- I have not added the logic needed to work out the next booking
- as if you had a few bookings after the current date
- it will just display the last one
- As I believe at this stage, it will be a performance issue, as async has not been worked out properly yet

- What it looks like on mobile devices

![table-mobile.png](static/images/docs/features/table-mobile.png)

- What it looks like on desktop devices

![table-desktop.png](static/images/docs/features/table-desktop.png)

#### [deleting table records](#features)

- Once the Delete button is clicked
- a modal will pop up for deleting the record from the database

![delete_button.png](static/images/docs/bugs/delete_button.png)

![delete_modal.png](static/images/docs/bugs/delete_modal.png)

#### [reset password based on username](#features)

- when you want to reset your password, enter your username

![reset-password.png](static/images/docs/features/reset-password.png)

- If the username is correct, it will take you to a page for a temporary password

![reset-password-done.png](static/images/docs/features/reset-password-done.png)

- There is a link on that page that takes you to the change password page
- Which you can only access if you log in with the temp password

![change_password.png](static/images/docs/features/change_password.png)

- As a future feature, I would like to authenticate by email
- As it will be more secure

### [Future features to be added at a later stage](#features)

- I would like to add a dashboard for the admin logged-in user
- I have already included a role in the database for this feature
- Search based on Foreign Key in an admin panel:
    - I would like to search based on a foreign key in the admin panel
    - for some reason, I can't seem to search using the search_filed as it does not work on foreign keys
- I am wanting to implement async/await for fetching data
- As a future feature, I would like to add email for reset password

---

## [Testing](#table-of-content)

- This is generally the cycle that I tried to follow for testing

![testing-lifecycle.png](static/images/docs/testing/testing-lifecycle.png)

### [Manual Testing](#testing)

| Title                                   | Pass |
|-----------------------------------------|------|
| Header                                  | Yes  |
| Homepage                                | Yes  |
| Testing responsive of the menu page     | Yes  |
| Testing responsive of the about page    | Yes  |
| Testing of updating records             | Yes  |
| Testing if I can navigate to table page | Yes  |
| Testing model form for booking a table  | Yes  |
| HTML Validation testing                 | Yes  |
| CSS Validation testings                 | Yes  |
| Wave testing for accessibility          | Yes  |
| Lighthouse testing                      | Yes  |

#### Header

I have tested the responsive design of the header
There is a collapsable hamburger menu on devices smaller than laptop

This is what it looks like on a laptop and larger

![header-desktop.png](static/images/docs/testing/header-desktop.png)

When the navbar becomes smaller than laptop, this is what it will look like

![header-mobile.png](static/images/docs/testing/header-mobile.png)

- The hamburger-menu has changed to the three horizontal lines

When the hamburger icon menu is open

![header-ham-open.png](static/images/docs/testing/header-ham-open.png)

Testing with HTML validator

![header-html-validator.png](static/images/docs/testing/header-html-validator.png)

The results can be
found [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-booking-system-5abd35239ade.herokuapp.com%2F)

Testing with a CSS validator

![header-css-validator.png](static/images/docs/testing/header-css-validator.png)

The results can be
found [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-booking-system-5abd35239ade.herokuapp.com%2F)

This testing was conducted on Lighthouse with Desktop in mind

![testing-header.png](static/images/docs/testing/testing-header.png)

This testing was conducted on Lighthouse with Mobile in mind

![testing-header2.png](static/images/docs/testing/testing-header2.png)

#### Homepage

- When do I have added data for the Carousel?
- You are only allowed to add three entries per meal
- For instance, you are only allowed three breakfasts, three lunches and three suppers
- The carousel will auto choose which one based on the time of day
- I have allowed for four entries, based on the fact that if you need to update one of them

If all data is correct, it will show this in the admin panel

![manual-homepage-db-pass.png](static/images/docs/testing/manual-homepage-db-pass.png)

If you are trying to enter more than three entries for breakfast

![manual-homepage-db-fail.png](static/images/docs/testing/manual-homepage-db-fail.png)

- Was testing to see if I could get the correct meals from the database
- Just by changing the filter variable
- When you enter what type of meal you want, it is done as a choice based on three numbers
- Zero being breakfast, one being lunched and 2 being supper
- There is also a number three that means that if it doesn't correspond to any number that will then run

![manual-homepage-meal.png](static/images/docs/testing/manual-homepage-meal.png)

- Tested responsiveness of the carousel
- I don't test for anything below 400 pixels

Responsive on Mobile devices

![manual-homepage-responsive-mobile.png](static/images/docs/testing/manual-homepage-responsive-mobile.png)

Responsive on Tablet devices

![manual-homepage-responsive-tablet.png](static/images/docs/testing/manual-homepage-responsive-tablet.png)

Responsive on Laptop devices

![manual-homepage-responsive-laptop.png](static/images/docs/testing/manual-homepage-responsive-laptop.png)

- This design has changed to a card since it was taken

#### [Testing responsiveness of the menu page](#manual-testing)

- Testing to see how responsive the menu page is
- on different screen sizes

Responsive design on laptop

![menu_page_laptop.png](static/images/docs/testing/manual_testing/menu_page_laptop.png)

Responsive design on tablet

![menu_page_tablet.png](static/images/docs/testing/manual_testing/menu_page_tablet.png)

Responsive design on mobile

![menu_page_mobile.png](static/images/docs/testing/manual_testing/menu_page_mobile.png)

- I have changed the background color for the headings

#### [Testing the responsiveness of the about page](#manual-testing)

- This testing section was to test it to see how the about page
- is going to look at different screen sizes

Responsive design on mobile

![about_responsive_mobile.png](static/images/docs/testing/manual_testing/about_responsive_mobile.png)

Responsive design on Tablet

![about_responsive_tablet.png](static/images/docs/testing/manual_testing/about_responsive_tablet.png)

Responsive design on Laptop

![about_responsive_laptop.png](static/images/docs/testing/manual_testing/about_responsive_laptop.png)

#### [Testing of updating records](#manual-testing)

- When the update button is clicked
- The modal will popup using form validation
- I have not yet been able to pre-populate the form using JavaScript
- That will be added as a future feature
- However, the update does work
- You have to update both fields at the sametime
- Clicking the "X" or the Cancel button will exit the modal
- When submit is clicked, it will send it to a database for updating
- which will send you a message to say it has been updated

![update_records_1.png](static/images/docs/testing/manual_testing/update_records_1.png)

![update_records_2.png](static/images/docs/testing/manual_testing/update_records_2.png)

![update_records_3.png](static/images/docs/testing/manual_testing/update_records_3.png)

#### [Testing if I can navigate to table page](#manual-testing)

- when I am logged out and I try to log in to the table page
- it redirects me to sign in page

- manually entering the address in address bar

![tabel_address_bar.png](static/images/docs/testing/manual_testing/tabel_address_bar.png)

- when hit enters the address bar

![table_protected_page.png](static/images/docs/testing/manual_testing/table_protected_page.png)

#### [Testing model form for booking a table](#manual-testing)

- The number of seats only allows you to select from 1 to 10
- The validation of the timeslots only allows you to select from 1 hour of present time
- As a logged-in user, you are only allowed to book once a day, to eliminate double booking on the same day
- The modal is also fully responsive
- I have not been able to work out daylight savings mode

Modal form

![modal_table_booking_form.png](static/images/docs/testing/manual_testing/modal_table_booking_form.png)

Modal booking message

![modal_table_booking_message.png](static/images/docs/testing/manual_testing/modal_table_booking_message.png)

Modal testing of incorrect time slot

![modal_table_booking_test.png](static/images/docs/testing/manual_testing/modal_table_booking_test.png)

#### [Html validation testing](#manual-testing)

- I tested this on HTML Validator
- Using the Heroku link of my live site
- As the validator won't work when copying and pasting code
- This link was tested on the about page
- But all the pages are only giving info warnings

![html-validator-link.png](static/images/docs/testing/manual_testing/html-validator-link.png)

![html-validator-results.png](static/images/docs/testing/manual_testing/html-validator-results.png)

#### [Css validation testing](#manual-testing)

- The only errors that CSS picked up were with bootstrap
- There were no other errors with my CSS code

![css-validation.png](static/images/docs/testing/manual_testing/css-validation.png)

#### [Wave testing for accessibility](#manual-testing)

- With the wave validator, there seems to be just two contrast issues on all pages
- This is a small issue with the contrast of the developer section in footer

![wave-validator-about.png](static/images/docs/testing/manual_testing/wave-validator-about.png)

![footer.png](static/images/docs/testing/manual_testing/footer.png)

#### [lighthouse testing](#manual-testing)

- this lighthouse testing was done in incognito mode
- As some of my extensions were messing with the results

home page on mobile

![home_mobile.png](static/images/docs/testing/lighthouse/home_mobile.png)

home page on desktop

![home_desktop.png](static/images/docs/testing/lighthouse/home_desktop.png)

menu page on mobile

![menu_mobile.png](static/images/docs/testing/lighthouse/menu_mobile.png)

menu page on desktop

![menu_desktop.png](static/images/docs/testing/lighthouse/menu_desktop.png)

table booking page on mobile

![table_mobile.png](static/images/docs/testing/lighthouse/table_mobile.png)

table booking page on desktop

![table_desktop.png](static/images/docs/testing/lighthouse/table_desktop.png)

about page on mobile

![about_mobile.png](static/images/docs/testing/lighthouse/about_mobile.png)

about page on desktop

![about_desktop.png](static/images/docs/testing/lighthouse/about_desktop.png)

### [Automated Testing](#testing)

The following command can be used to run tests in Parallel
Auto means that it will only run tests on threads that are available
python manage.py test --parallel auto

If you are just wanting to test conventionally

| Title                                                        | Pass |
|--------------------------------------------------------------|------|
| Authentication                                               | Yes  |
| Homepage                                                     | Yes  |
| Test if correct menu gets returned based on slug             | Yes  |
| Test form invalid on Booking a table page                    | Yes  |
| Test form valid on Booking a table page                      | Yes  |
| Test protected pages against anonymous user                  | Yes  |
| Test protected pages against users that are logged in or not | Yes  |

#### [Authentication](#automated-testing)

What was tested in this scenario:

- I wanted to test it if a user can be created
- I wanted to test it if a user was able to log in

As this is the first time I have written auto tests by myself,
I wanted to keep it basic

![auto-test-authentication.png](static/images/docs/testing/auto-test-authentication.png)

#### [Homepage](#automated-testing)

What was tested in this scenario

- I first created a failing test for breakfast

Changing the assertEqual variable to a number that is not zero

![auto-homepage-testing-what.png](static/images/docs/testing/auto-homepage-testing-what.png)

The results of a failing test

![auto-homepage-testing-results-fail.png](static/images/docs/testing/auto-homepage-testing-results-fail.png)

Testing for a passing test

![auto-homepage-testing-what-pass.png](static/images/docs/testing/auto-homepage-testing-what-pass.png)

#### [Test if correct menu gets returned based on slug](#automated-testing)

What was tested?

- I purposefully made a spelling error to see if the Supper Menu fails
- Then pass the correct test to see if it passes

Failing test

![menu_type_fail.png](static/images/docs/testing/auto_testing/menu_type_fail.png)

Passing test

![menu_type_passing.png](static/images/docs/testing/auto_testing/menu_type_passing.png)

#### [Test form invalid on Booking a table page](#automated-testing)

- First testing for a negative test
- changed seats form data to 2
- wanting to see what happens if the correct data is entered
- to make sure that form validation is working correctly
- Then changed form seats data to 20
- wanting to see if it gives me a false reading
- making this test, test for a false value

- Testing form invalid failing test

![test_form_invalid_fail.png](static/images/docs/testing/auto_testing/test_form_invalid_fail.png)

![test_form_invalid_fail_function.png](static/images/docs/testing/auto_testing/test_form_invalid_fail_function.png)

- Testing form invalid passing test

![test_form_valid_pass.png](static/images/docs/testing/auto_testing/test_form_valid_pass.png)

![test_form_invalid_pass_function.png](static/images/docs/testing/auto_testing/test_form_invalid_pass_function.png)

#### [Test form valid on Booking a table page](#automated-testing)

- Tested for incorrect value changed seats data to 20
- Just to get a negative result
- Tested for correct value changed seats data to 2
- To get a positive test result

- Testing form valid failing test

![test_form_valid_fail.png](static/images/docs/testing/auto_testing/test_form_valid_fail.png)

![test_form_valid_fail_function.png](static/images/docs/testing/auto_testing/test_form_valid_fail_function.png)

- Testing form valid passing test

![test_form_valid_pass1.png](static/images/docs/testing/auto_testing/test_form_valid_pass1.png)

![test_form_valid_pass_function.png](static/images/docs/testing/auto_testing/test_form_valid_pass_function.png)

#### [Test protected pages against anonymous user](#automated-testing)

- Test for a failing test, if status code is not 302
- For some reason this test, tests against a 302 http status code
- 302 status codes mean resources permanently removed, in other words, it was there but then were moved somewhere else

- Test anonymous user failing test

![test_protected_page_anonymous_fail.png](static/images/docs/testing/auto_testing/test_protected_page_anonymous_fail.png)

![test_protected_page_anonymous_fail_function.png](static/images/docs/testing/auto_testing/test_protected_page_anonymous_fail_function.png)

- Test anonymous user passing test

![test_protected_page_anonymous_pass.png](static/images/docs/testing/auto_testing/test_protected_page_anonymous_pass.png)

![test_protected_page_anonymous_pass_function.png](static/images/docs/testing/auto_testing/test_protected_page_anonymous_pass_function.png)

#### [Test protected pages against users that are logged in or not](#automated-testing)

- Testing if the status code is something other than 200 if it returns an error message
- Testing if the status code is 200, a passing test

- Test user failing test

![test_protected_page_user_fail.png](static/images/docs/testing/auto_testing/test_protected_page_user_fail.png)

![test_protected_page_user_fail_function.png](static/images/docs/testing/auto_testing/test_protected_page_user_fail_function.png)

- Test user passing test

![test_protected_page_user_pass.png](static/images/docs/testing/auto_testing/test_protected_page_user_pass.png)

![test_protected_page_user_pass_function.png](static/images/docs/testing/auto_testing/test_protected_page_user_pass_function.png)

---

## [Bugs](#table-of-content)

| Title                                                        | Solved |
|--------------------------------------------------------------|--------|
| The text is not aligned correctly to the Authentication Icon | Yes    |
| Labels are not correctly sitting next to the Icons           | Yes    |
| Problem with Hamburger Menu                                  | Yes    |
| Hamburger menu jumps as I try and open and close menu        | No     |
| Operational error in database as trying to run auto test     | Yes    |
| Carousel image not being aligned correctly                   | Yes    |
| Favicon icon not displaying                                  | Yes    |
| Heroku auto refreshing unnecessarily                         | Yes    |
| Navbar not at top of screen                                  | Yes    |   
| Performance issues in page loading                           | Yes    |
| Too many connections to database at once                     | Yes    |
| Styling of homepage                                          | Yes    |
| Carousel arrows                                              | Yes    |
| Copyright test not showing in footer                         | Yes    |
| Copyright text overlapping with developer content            | Yes    |
| Next booking not being displayed                             | Yes    |
| Not recognizing daylight savings mode                        | No     |
| Table over lapping on smaller devices                        | Yes    |
| TypeError in console                                         | Yes    |
| Am I Responsive does not display image                       | No     |

### [The text is not aligned correctly to the Authentication Icon](#bugs)

The text was not aligned correctly to the icon above it

![header-text-incorrect.png](static/images/docs/bugs/header-text-incorrect.png)

- This bug was solved
- by placing it inside a container
- then I could manipulate it with CSS

![header-text-correct.png](static/images/docs/bugs/header-text-correct.png)

### [Labels are not correctly sitting next to the Icons](#bugs)

The label is sitting to far below the icons
And not aligning correctly

![header-label-incorrect.png](static/images/docs/bugs/header-label-incorrect.png)

This issue was solved with flexbox and CSS
They were already in their own container class
I just had to alter the CSS properties

![header-label-correct.png](static/images/docs/bugs/header-label-correct.png)

### [Problem with Hamburger Menu](#bugs)

What is the Problem?

- When I am testing responsive design and the Hamburger menu is open
- It doesn't want to display the page icons

![page-icons-not-displayed.png](static/images/docs/bugs/page-icons-not-displayed.png)

How was this Problem solved?

- I separated my code out into a services directory inside the templates directory
- Created two div containers giving each one its own class
- The first had a class of mobile
- The Second had a class of tablet
- I would then hide and un hide the two depending on what size screen it was on
- The reason for breaking up the code is that I needed to call the icons in two different locations
- I am attempting to practice DRY (Don't Repeat Yourself) run coding style

![page-icons-displaying.png](static/images/docs/bugs/page-icons-displaying.png)

### [Hamburger menu jumps as I try and open and close menu](#bugs)

What is the Issue?

- The hamburger menu is jumping up and down as the menu is opened or closed
- The bug is not visible from the screenshot below

![hamburger-menu.png](static/images/docs/bugs/hamburger-menu.png)

- I have since changed to the horizontal icon but the bug is still there

### [Operational error in database as trying to run auto test](#bugs)

Problem?

- When I tied to run python manage.py test
- I get the following error
- error message "django.db.utils.OperationalError: near 'None': syntax error"

![OperationalError.png](static/images/docs/bugs/operationalError.png)

Solution?

- Destroy all data in database using the flush command
- I used this command as I suspected that it was an issue in the database
- I then went on to delete all migration files, but accidentally deleted directories at the same time
- Then tried to makemigrations and migrate
- But, for some reason it was not picking up my app like: home, menu, about, book_table models
- so I did a bit of googling to find that I can makemigrations on a single app
- which is what I did: python manage.py makemigrations home
- doing that for all of my apps
- this then created the migrations directory and the initial migration for that app
- after running makemigrations on all my apps, I then had to migrate my db
- then the page could load properly after that and all was sorted out
- which I could also run python manage.py test
- I was no longer getting that error
- Then test files were now running as they were supposed to
- the issue was all sorted, but now I have to create all my data again
- re-populating my database with data from fixtures JSON files
- I had to run the command one at a time python manage.py loaddata fixtures/fixture/chef_special.json

![database_working correctly.png](static/images/docs/bugs/database_working%20correctly.png)

Note to myself for a future reference?

- In future don't use the flush command as it will completely wipe my db
- try and delete my migrations directory and start from there

### [Carousel image not being aligned correctly](#bugs)

Problem?

- The image is not being aligned neatly to the carousel on Mobile devices
- This was tested on the iPhone 6/7/8 display

![carousel_not_aligned.png](static/images/docs/bugs/carousel_not_aligned.png)

Solution?

- This bug has been solved using cards
- as cards were easier to keep content in a container

### [Favicon icon not displaying](#bugs)

Problem?

- Favicon icon does not want to load on server start

favicon is not loaded in the browser tab

![favicon_browser_tab.png](static/images/docs/bugs/favicon/favicon_browser_tab.png)

favicon is not loaded in the console

![favicon_console_error.png](static/images/docs/bugs/favicon/favicon_console_error.png)

Solution?

- As soon as I turned some methods in the class Menu
- To functions, as they were static methods
- The icon loaded correctly as intended
- Not quiet sure why or how it worked

![favicon_issue_solved.png](static/images/docs/bugs/favicon/favicon_issue_solved.png)

### [Heroku auto refreshing unnecessarily](#bugs)

Problem?

- for some reason, heroku is auto refreshing
- I expected that it is a problem with django_browser_reload package
- This package I use for in development
- It refreshes my server on file change

Refreshes browser tab unnecessarily

![heroku_refresh_browser_tab.png](static/images/docs/bugs/heroku_refresh_browser_tab.png)

Refreshing in the Heroku console logs

![heroku_refresh_console_logs.png](static/images/docs/bugs/heroku_refresh_console_logs.png)

Solution?

- I solved this problem by adding a simple logic to settings.py and urls.py
- If Debug == 'True' then add django_browser_reload to constant lists
- It needed to be a string for the Debug constant for when environment variables load
- It loads it as a string

Added logic to settings.py file

![heroku_refresh_logic_to_settings.png](static/images/docs/bugs/heroku_refresh_logic_to_settings.png)

Added logic to urls.py file

![heroku_refresh_logic_to_urls.png](static/images/docs/bugs/heroku_refresh_logic_to_urls.png)

### [Navbar not at top of screen](#bugs)

Problem?

- The navbar is not quite sitting at the top of the screen

![navbar_not_at_top.png](static/images/docs/bugs/navbar_not_at_top.png)

Solution?

- this bug was solved with simple CSS

### [Performance issues in page loading](#bugs)

Problem?

- The score that I received is too low for lighthouse testing
- I need to bring that score up
- I think that there is too much logic that is happening in the background
- I might have to consider a pip package for multi threading

![performance_lighthouse.png](static/images/docs/bugs/performance/performance_lighthouse.png)

Solution?

- I have solved this bug by simplify some of my logic that I use

![performance_lighthouse_solved.png](static/images/docs/bugs/performance/performance_lighthouse_solved.png)

### [Too many connections to database at once](#bugs)

Problem?

- When trying to connect to the database on the menu page, I am getting a connection error
- There are too many models trying to connect at once

![db_connections.png](static/images/docs/bugs/db_connections.png)

Solution?

- with this error, I was using thread module
- with using thread module, you sometimes might get a thread lock issue
- the computer doesn't know what todo, or it sends to many signals to elephantSQL
- whichever issue it was, I have now completely removed thread module
- and made two global variables to gather data that I needed
- then filter it out for when I need it

![menu_connection_issue.png](static/images/docs/bugs/menu_connection_issue.png)

- These variables have since been moved inside the class

### [styling of homepage](#bugs)

Problem?

- The styling of the homepage does not look the same as the rest of the site

![styling_homepage_problem.png](static/images/docs/bugs/styling_homepage/styling_homepage_problem.png)

Solution?

- I have now created it as a card within the carousel
- It is responsive from 375 pixels
- the indicators at the bottom will disappear on screen sizes less than 400 px
- the indicator is clickable for if you want to go to a specific item
- with side indicators to click for left or right images

![carousel_styling_above400.png](static/images/docs/bugs/styling_homepage/carousel_styling_above400.png)

![carousel_styling_below400.png](static/images/docs/bugs/styling_homepage/carousel_styling_below400.png)

![carousel_styling_laptop.png](static/images/docs/bugs/styling_homepage/carousel_styling_laptop.png)

![carousel_styling_tablet.png](static/images/docs/bugs/styling_homepage/carousel_styling_tablet.png)

### [carousel arrows](#bugs)

![arrows.png](static/images/docs/bugs/carousel_arrows/arrows.png)

- carousel arrows are being displayed when there is no carousel to display
- on certain devices the arrows don't seem to want to show up properly
- at this stage, I am not sure how to change that

![arrows_2.png](static/images/docs/bugs/carousel_arrows/arrows_2.png)

### [copyright text not showing in footer](#bugs)

- The current year is not showing when
- on the logout, login and sign out forms

![copyright text.png](static/images/docs/bugs/copyright_text/copyright_text.png)

### [copyright text overlapping with developer content](#bugs)

Problem?

- Overlapping text in footer

![overlapping_1.png](static/images/docs/bugs/copyright_text_overlapping/overlapping_1.png)

Solution?

- changed the left and right margin from 0.5em to 1 em

![overlapping_2.png](static/images/docs/bugs/copyright_text_overlapping/overlapping_2.png)

### [next booking not being displayed](#bugs)

Problem?

- The Next booking is supposed to show the last booking in the history table

![last_booking_1.png](static/images/docs/bugs/next%20booking/last_booking_1.png)

![last_booking_2.png](static/images/docs/bugs/next%20booking/last_booking_2.png)

Solution?

- There was just a simple variable that I had to add
- I also changed from next booking to last booking
- As last booking made more sense

![last_booking_3.png](static/images/docs/bugs/next%20booking/last_booking_3.png)

### [not recognizing daylight savings mode](#bugs)

Problem?

- Django does not recognize daylight savings time
- For some reason, Django does not change time zones
- As I have just reached daylight savings mode

This is the current date and time of my computer

![time_zone_1.png](static/images/docs/bugs/daylight_time/time_zone_1.png)

Solution?

- This bug has not been solved yet
- This is also added as an extra feature for future reference

This is what was saved in the database with current model
Notice that the Booking created time is an hour difference

![time_zone_2.png](static/images/docs/bugs/daylight_time/time_zone_2.png)

### [table over lapping on smaller devices](#bugs)

Problem?

- The table was not responding when getting to smaller devices

![overlapping_1.png](static/images/docs/bugs/table_over_lapping/overlapping_1.png)

![overlapping_2.png](static/images/docs/bugs/table_over_lapping/overlapping_2.png)

Solution?

- Hide the last child element on smaller devices
- In this case, the Delete and Update buttons

![overlapping_3.png](static/images/docs/bugs/table_over_lapping/overlapping_3.png)

- I have decided that delete and update buttons
- it will only be used for screen sizes bigger than tablet

### [TypeError in console](#bugs)

Problem?

- TypeError occurs after a few seconds of page load
- This error occurs from the timeout section in the script.js file

![TypeError_1.png](static/images/docs/bugs/typeerror/TypeError_1.png)

![TypeError_2.png](static/images/docs/bugs/typeerror/TypeError_2.png)

Solution?

- added a try/catch block for TypeError
- in the catch block nothing will occur
- I didn't see anywhere on the internet were you can't do a try/catch like this

![TypeError_3.png](static/images/docs/bugs/typeerror/TypeError_3.png)

### [Am I Responsive does not display image](#bugs)

Problem?

- Am I Responsive does not want to display a screenshot of my live website

![responsive.png](static/images/docs/bugs/amiresponsive.png)

Solution?

- Not sure what this problem is it might be a loading issue

---

## [Credits](#table-of-content)

- How the hamburger menu was achieved was taken from [here](https://www.w3schools.com/howto/howto_js_mobile_navbar.asp)
- All icons in this project were designed
  by [Icons8](https://icons8.com/?utm_source=figma-plugin-icons8&utm_medium=cross-promo&utm_campaign=web-version) with
  the help of Figma
- All images that you see on the homepage for Chef's Specials were taken from homepage, I tried my best to make sure
  that there was no copyright on it
- [Document that assisted me with CRUD operation using Class-Based Views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/)
- [Document that help me with form validation and success url](https://stackoverflow.com/questions/54129416/django-how-do-i-perform-a-createview-redirect-properly)
- [Setting form validation with widgets](https://medium.com/@alex.kirkup/making-error-messages-visible-in-django-forms-1abea48c802a)
- [How to display messages in the template](https://stackoverflow.com/questions/25470452/django-clear-form-field-after-a-submit)
- [example on how to test if file exists](https://www.w3resource.com/python-exercises/unittest/python-unittest-exercise-5.php#:~:text=We%20use%20the%20self.,We%20use%20the%20self.)
- [convert to base64 string](https://dev.to/nemecek_f/django-how-to-send-image-file-as-part-of-response-j05) this was
  used for themes, but decided to take themes out, I am planning on this for a future feature
- [Luke Buchanan](https://www.linkedin.com/in/lukebuchanan67/) - Mentor
- [Code Institute](https://codeinstitute.net/) - Bootcamp
- [reference for the success message](https://stackoverflow.com/questions/36087752/django-messaging-framework-how-to-only-display-success-messages)
- [Example of how to use the Delete View](https://www.geeksforgeeks.org/deleteview-class-based-views-django/)

---
