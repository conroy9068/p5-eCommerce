# MarketFlex

- [MarketFlex - Overview](#overview)
- [User Experience (UX)](#user-experience-ux)
  - [Agile Development](#agile-development)
    - [User Stories](#user-stories)
- [Design](#design)
  - [Database Schema](#database-schema)
  - [Wireframes](#wireframes)
  - [Typography](#typography)
  - [Colours](#colours)
- [Features](#features)
  - [Nav Bar](#nav-bar)
  - [Landing Page](#landing-page)
  - [Product List Page](#product-list-page)
  - [Product Detail View](#product-detail-view)
  - [Search, Order & Filter](#search-order--filter)
  - [Basket](#basket)
  - [Order Form](#order-from)
  - [Order Confirmation Page](#order-confirmation-page)
  - [Profile Page](#profile-page)
  - [Register, Log In & Log Out](#register-log-in--log-out)
  - [Footer](#footer)
  - [Product Create](#product-create)
  - [Product Edit](#product-edit)
  - [Contact Page](#contact-page)
  - [Error Pages](#error-pages)
  - [Messages](#messages)
- [Features Left to Implement](#features-left-to-implement)
- [Bugs](#bugs)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Libraries & Frameworks](#libraries--frameworks)
- [Web Marketing](#web-marketing)
- [Search Engine Optimization](#search-engine-optimization)
  - [sitemap.xml](#sitemapxml)
  - [robots.txt](#robotstxt)
  - [Sitemap Google Registration](#sitemap-google-registration)
- [Deployment](#deployment)
  - [Heroku Deployment](#heroku-deployment)
  - [Local Deployment](#local-deployment)
- [Tools](#tools)
- [Credits](#credits)
  - [Content](#content)
  - [Information Resources](#information-resources)


## Overview

MarketFlex is a fully responsive e-commerce platform built using Django. This site allows people to browse and purchase tools and equipment used in many inductries like the automotive and metal fabrication industy to name two.

The site allows user to search for specific items they are looking for and filter all items on a number of parameters. The site allows them to create a user profile so that they can quickly purchase items each time they visist the site and also keeps a record of there past orders.

User can make purchasesas a guest without having a profile also if they chose not to register with an account.

The option to sign up to newletters is also avaiable to the user, this will keep them up to date with the latest promotions and sales on offer.

The site also has admin users, admin users have access to create, update and delete products on the site.

View the live project [Here](https://p5-ecommerce-fb6cb413b539.herokuapp.com/)

![Responsive Design Screenshot](README/assets/am-i-responsive.png)

## User Experience (UX)

### Agile Development

The agile methodology was used in the development of this project. This is when each feature to the site is broken down into smaller tasks and each then is developed. The tool used to manage this was GitHub projects.

The breakdown of tasks was done using user stories, each story would describe the task the end user would like to do to achieve a desire goal. The user stories contained acceptance criteria that outline what the site needed to do in order to meet the requirements of the user story. Then there are tasks which described the technical work thats needed to be done to complete each User Story.

Story points are an estimated level of effort the developer thinks will be required to develop that feature.

The MoSCoW Prioritization technique was used to assign priorities for Product Backlog Items to be completed. Using this allowed for each user story to be prioritized.

User Story Sample
USER STORY:
As a Site User, I want to be able to navigate the site. The navigation needs to be simple and easy to understand. Navigating should be fluid

ACCEPTANCE CRITERIA:
- criteria one: As a Site User, i can navigate between different product categories
- criteria two: As a Site User, I can easily search for a product by its name
- criteria three: As a Site User, I can easily navigate to my shopping bag
- criteria four: As a Site User, I can easily navigate to my profile settings
- criteria five: As a Site User, I can easily login and logout of my profile


TASKS:
- [ ]  Create a fixed Nav Bar
- [ ]  Add a search bar with search functionality
- [ ]  Add a link for users to access the shopping bag page
- [ ]  Add a link for users to access their profile details page
- [ ]  Add a link for users so they can login if not logged in and a link to logout for users that are logged in.

BUG TICKETS:

- [ ]

STORYPOINTS: 4

### User Stories
User stories where done using the agile methodology above. The user stories where created and managed using GitHub projects. A lin to all the user stories can be found below.

View user stories [Here]()


## Design


### Database Schema


### Wireframes


### Typography

- Lato

### Colours
![Image Description](./README_ASSESTS/color-palette.png)

- [Coolors](https://coolors.co/)

- #13293D: A dark navy blue, often used for text or background elements that require a dark, strong presence.
- #006494: A rich medium blue, good for accents and to draw attention to elements.
- #247BA0: A calming mid-tone blue, suitable for backgrounds, buttons, or headers.
- #1B98E0: A bright sky blue, stands out well against both light and dark elements, good for call-to-action buttons or links.
- #E8F1F2: A very light blue with a hint of grey, excellent for backgrounds or for a light, airy feeling in the design.


## Features


### Nav Bar


### Landing Page


### Product List Page


### Product Detail View


### Search, Order & Filter


### Basket


### Order From


### Order Confirmation Page


### Profile Page


### Register, Log In & Log Out


### Footer


### Product Create


### Product Edit


### Contact Page


### Error Pages


### Messages


## Features Left to Implement

* Ability to add reviews for products
* Stock management system to track stock levels and allow admin to add stock. The sale of an item would also update the stockm level automatically.
* A blog section to keep users up to date with the latest news and promotions.
* An about us page to give the user more information about the company.


## Bugs


# Testing

Browse to the [TESTING.md](TESTING.md) file for the full testing documentation.

## Technologies Used

### Languages Used

- HTML5

- CSS3

- JavaScript

- Python

### Libraries & Frameworks

- Django:

  - The Django web framework was used to create the full-stack web application.

- Django Crispy Forms

	- ??

- Django allauth

	- ??

- Django storage

	- ??

- Stripe Library

	- ??

- Django countries

	- ??

- Psycopg2-Binary

  - A PostgreSQL database adapter for Python, providing efficient and secure database connections.

- PostgreSQL:

  - PostgreSQL was used as the object-relational database system.

- ElephantSQL:

  - ElephantSQL was used to host the database.

- Git:

  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- GitHub:

  - GitHub is used to store the projects code after being pushed from Git.

- Heroku:

  - Heroku was used for the deployed application.

- Gunicorn

  - A Python WSGI HTTP server for UNIX, used to run Python web applications.


### Validator Testing



## Web Marketing


## Search Engine Optimization


### sitemap.xml


### robots.txt


### Sitemap Google Registration



## Deployment

### Heroku Deployment
1. Create a Heroku account by going to https://signup.heroku.com/
2. Create a new app by clicking the "New" button in the top right corner and then click "Create new app".
3. Enter a name for the app and select the region closest to you.
4. Click the "Create app" button.
5. Select "settings" from the top menu.
6. Click the "Reveal Config Vars" button.
7. Enter the following environment variables with your values:
  - STRIPE_PUBLIC_KEY
  - STRIPE_SECRET_KEY
  - STRIPE_WH_SECRET
  - SECRET_KEY
8. Click buildpacks from the top menu.
9. Add the following buildpacks:
  - heroku/python
10. Click the "Deploy" tab from the top menu.
11. Click the "Connect to GitHub" button.
12. Search for your repository and click the "Connect" button.
13. Click the "Enable Automatic Deploys" button.
14. Click the "Deploy Branch" button.
15. Click the "View" button to launch the app.


### Local Deployment
1. Clone the repository by clicking the "Clone or download" button in github.
2. In your IDE open a new terminal.
3. Change the current working directory to the location where you want the cloned directory to be made.
4. Type git clone, and then paste the URL you copied in Step 2.
5. Press Enter. Your local clone will be created.
6. Create a virtual environment by typing python -m venv venv in the terminal.
7. Activate the virtual environment by typing venv\bin\activate in the terminal.
8. Install the requirements by typing pip install -r requirements.txt in the terminal.
9. Create a .env file in the root directory and add the following environment variables:
  - os.environ.setdefault("STRIPE_PUBLIC_KEY", "xxxxxxxxx")
  - os.environ.setdefault("STRIPE_PRIVATE_KEY", "xxxxxxxxx")
  - os.environ.setdefault("STRIPE_WH_SECRET", "xxxxxxxxx")
  - os.environ.setdefault("SECRET_KEY", "xxxxxxxxxx")
  - os.environ.setdefault("DEBUG", "False || True")
10. Migrate the database by typing python manage.py makemigrations and then python manage.py migrate in the terminal.
11. Create a superuser by typing python manage.py createsuperuser in the terminal.
12. Run the app by typing python manage.py runserver in the terminal.


### Tools

* [VS Code]() - IDE application used to develop code in.
* [Balsamiq](https://balsamiq.com/wireframes/) - Low Fidelity Wireframes
* [W3C Validator](https://validator.w3.org/) - Validator that checks the markup validity for Web Documents in HTML.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Validator that checks CSS validity.
* [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) - Validator that checks syntax and stlistic problems in Python code.
* [Am I responsive](https://ui.dev/amiresponsive) - Generates Responsive images for your website.
* [Chrome DevTools and Lighthouse](https://developer.chrome.com/docs/devtools/) - Web Developer Tools.

## Credits


### Content
- All the products content were taken from [Abcon](https://www.abcon.com/)
- All the products images were taken from [Abcon](https://www.abcon.com/)


### Information Resources

- [W3Schools - Python](https://www.w3schools.com/python/)
- [Stack Overflow](https://stackoverflow.com/)
- [Youtube](https://youtube.com/)




