![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## [Introduction](#table-of-content)

This is Part of my Fourth Project at Code Institute.

This is a simple Restaurant Booking System, were I can book tables based on a date and time
I am also able to see the Restaurant's Menu and Chef's specials.

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
- [Features](#features)
  - [Features that have been included in this project](#features-that-have-been-included-in-this-project)
  - [Future features to be added at a later stage](#future-features-to-be-added-at-a-later-stage)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
- [Credits](#credits)

---

## [Planning](#table-of-content)

### [Wireframes](#planning)

#### Homepage

![wireframe-homepage.png](static/images/readme/planning/wireframe-homepage.png)

#### Menu Page

![wireframe-menupage.png](static/images/readme/planning/wireframe-menupage.png)

#### About Page

![wireframe-about.png](static/images/readme/planning/wireframe-about.png)

#### Book a table Page

![wireframe-book-table.png](static/images/readme/planning/wireframe-book-table.png)

### [Ux-design](#planning)

### Home Page

![ux-homepage.png](static/images/readme/planning/ux-homepage.png)

### Menu Page

![ux-menupage.png](static/images/readme/planning/ux-menupage.png)

### Book Table Page

![ux-book-table.png](static/images/readme/planning/ux-book-table.png)

### About Page

![ux-about.png](static/images/readme/planning/ux-about.png)

### [Colour Pallet](#planning)

My colour pallet was taken from [color space](https://mycolor.space/)

This is the color pallet that I am using

![color-pallet.png](static/images/readme/planning/color-pallet.png)

The reason for this color pallet:

I wanted to stick to a blueish theme for this restaurant

### [User Stories using MOSCOW Prioritization techniques](#planning)

Header

![Screenshot from 2024-02-04 14-57-56.png](static/images/readme/moscow-header.png)

### [How to start this project locally](#planning)

- when using ssh
- git clone git@github.com:douglas86/ci-project4-restaurant-booking-system.git
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
- And create a new database instance make sure that the version of PostgresSQL is greater than 12
- Once created then copy and paste the url in the env.py for the DATABASE_URL string
- once that is done, then you can run the command below to run the server
- python manage.py runserver
- you can use ctrl + click on the server name that should open up a web browser at the correct port

env.py

![env.png](static/images/readme/env.png)

### [How this project was deployed to Heroku](#planning)

- head over to [Heroku Dashboard](https://dashboard.heroku.com/apps)
- create a new app and add all the environment variables to your config vars
- make sure to add DISABLE_COLLECTSTATIC with the value of 1
- if this variable is not used Heroku will spit out an error
- change DJANGO_DEBUG with the value of False
- make sure that there is a runtime.txt file
- this will tell Heroku what version of python to use
- make sure that requirements.txt is up to date
- make sure to see if Heroku hasn't automatically add a build pack for PostgresSQL
- if it has delete it as this project is using elephantSQL instead
- connect github and the repo to Heroku and build the project

### [Technology Used](#planning)

- HTML/CSS - html templating and css styling
- Python—logic used in this project
- JavaScript—Used for Models and other front end logic
- Django - Python Framework for developing this project
- PostgresSQL - using elephantSQL for database
- Heroku - cloud deployment
- GitHub - version control
- Pycharm - IDE for development

---

## [Features](#table-of-content)

### [Features that have been included in this project](#features)

### [Future features to be added at a later stage](#features)

---

## [Testing](#table-of-content)

### [Manual Testing](#testing)

### [Automated Testing](#testing)

---

## [Credits](#table-of-content)

---
