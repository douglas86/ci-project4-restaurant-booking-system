![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## [Introduction](#table-of-content)

This is Part of my Fourth Project at Code Institute.

This is a simple Restaurant Booking System, were I can book tables based on a date and
see the Restaurant Menu and Chef's specials.

---

# Table of Content

- [Planning](#planning)
  - [Wireframes](#wireframes)
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

#### Header

Desktop

![header-desktop.png](static/images/readme/header-desktop.png)

Mobile

![header-mobile.png](static/images/readme/header-mobile.png)

### [Colour Pallet](#planning)

My colour pallet was taken off [color wheel](https://color.adobe.com/create/color-wheel) website

Colour Wheel

![color-wheel](static/images/readme/color-wheel.png)

Colour Pallet

![color-pallet.png](static/images/readme/color-pallet.png)

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
