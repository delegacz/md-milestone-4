# STR:WER - eCommerce Street Wear Shop
[![Build Status](https://travis-ci.org/delegacz/md-milestone-4.svg?branch=master)](https://travis-ci.org/delegacz/md-milestone-4)

[Visit Live Project](https://md-milestone-project-4.herokuapp.com/)

STR:WER is an e-commerce shop for all things streetwear, manually picked inventory of the most desirables items from the world of streetwear. 

Use code: 123ABC for 20 EURO OFF
 
## UX
[Wireframe Figma link](https://www.figma.com/proto/uAMIGE0TGB2uONuI1yjFCM/md-miestone-4?node-id=3%3A2&viewport=407%2C404%2C0.26897957921028137&scaling=min-zoom)

### Who is this website for?
This website is aimed at people who are interested in streetwear culture and would like to purchase clothing articles(Sneakers, and Outdoor/Outer Clothing)

### What does it fulfill?
This website fulfills the need of users to discover and purchase products by providing a range of products and an ability to order and pay for them

### User Stories 

- As a user, I want to add a product to the cart, so that I can purchase it.
- As a user, I want to fill a refund form, so that I can receive a refund for the returned product
- As a user, I want to sign up, so that I can make a purchase
- As a user, I want to search through products, so that I can find a jacket I want

## Features

 
### Existing Features
- Refunds - allows the customer to request a refund by providing ref code and submitting a form
- Coupon Codes - allows users to lower the price of the order by using code at checkout
- Pagination - allows user to browse through products by changing the displayed page
- Add to Cart - Allows users to add an item to the cart for later checkout, cart page also allows the user to modify the quantity of the product or remove it before progressing to checkout
- Stripe Integration - Allows users to pay for their order using Stripe
- Order Summary - Allows users to see a detailed view at their order on the checkout page and apply coupon code for a discount


### Features Left to Implement
- Size Selector
- Gender Selector
- More product categories
- Product Reviews
- Advanced product Gallery


## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Stripe](https://stripe.com/)
    - The project uses **Stripe** for credit/debit card processing and payment gateway
- [Django](https://www.djangoproject.com/)
    - The project uses **Django** as python web framework
- [Python](https://www.python.org/)
    - The project uses **Python** as the main programming language
- [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    -The project uses **AllAuth** to provide the ability to Sign in/Login for users
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - The project uses **Crispy Forms** to simplify styling of Django generated forms
- [django countries](https://pypi.org/project/django-countries/)
    - The project uses **Django Countries** to provide a Country choice field in the forms
- [django filter](https://django-filter.readthedocs.io/en/master/guide/usage.html)
    - The project uses **Django Filter** to provide search and pagination functionality
- [Pillow](https://pillow.readthedocs.io/en/stable/)
    - The project uses **Pillow** as python Imaging Library
- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** to simplify and streamline the templates creation process
- [JavaScript](https://www.javascript.com/)
    - The project uses **JavaScript** for DOM manipulation and Stripe integration
- [Git](https://git-scm.com)
    - The project uses **GIT** for version control and backup
- [GitHub](https://github.com)
    - The project uses **Github** for remote repository storage and commits log
- [Heroku](https://www.heroku.com/home)
    - The project uses **Heroku** as a deployment platform and hosting
- [Amazon Web Services - AWS](https://aws.amazon.com)
    - The project uses **AWS** for image/file storage
- [Travis CI](https://travis-ci.org)
    - The project uses **Travis CI** for continuous integration

## Testing
My tests focus on the business logic and presentation rather than testing Django itself. Unit tests were written form models, views and forms and can be accessed in `ecommerce/test.py` and can be run in the console by using `python manage.py test`. 
- Model Tests - Checks that models given data, calculate and output it properly
- View Testing - Checks if view given data output to correct template and request comes back with status 200. Some view could not be tested as I couldn't figure out how to test views that are calling other methods for values
- Form Validity Testing - Checks if forms are valid, the checkout form could not be tested as I could not figure out how to test CountryField provided by Django countries

### Front-end Testing
This project was developed in Desktop First mindset - The website was tested on multiple browsers(Firefox, Chrome, Opera, Safari) and devices(iPhone X, iPhone Xr) to tests mobile responsivity and if all CSS and JavaScript function properly, One issue was found. See Below in **Issues Found**
### Travis CI
The project uses Tavis CI for Build Testing per Commit

Travis Setup Process:
##### 
##### Setting up Envirement Virables for Travis CI
- Variables are added in project configuration tab `More Options > Settings`
- SECRET_KEY had to be encrypted following these steps in the command line:

`travis login --pro`

`travis encrypt SOMEVAR="secretvalue" --add`

### Code Validation
Code was validated using followig:
 - [W3 HTML Validator](https://validator.w3.org) - HTML Validation
 - [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) - CSS Validation
 - [JS Hint](https://jshint.com) - JavaScript Validation
### Issues Found
1.

In Safari CSS `background-image: url();` does not display a background image when the image is not saved properly. For example `.jpg` will not work if these criteria are not met:
- progressive encoding is used
- the image is a background (for an element or the whole page)
- the image is too large (exact threshold unknown)

and  `.webp` seem not to be supported

To fix this issue image have to be resaved for example by using Photoshop

[StackOverflow Thread Source](https://stackoverflow.com/questions/17341728/background-image-not-showing-in-safari)

2.

After implemeting `django-filter` to introduce search functionality my pagination on `homeview` dissapeared.

That was resolved by rewriting `homeview` code to work with `django-filter`

## Deployment
This project was developed using [Miscrosoft Visual Studio Code](https://code.visualstudio.com/).
Git was used for version control and backup, it was then pushed to a remote repository on [GitHub](https://www.github.com/),
Once code was functional it was deployed to [Heroku](https://www.heroku.com/)

## Heroku Deployment process
1. Create Heroku Account
2. Create Heroku App
3. Create `requirements.txt` file:<br>
`pip freeze > requirements.txt`
4.  Create `Procfile` containg `web: python app.py`
5. Login to Heroku through terminal:<br> `heroku login`
6. Clone the repository:<br> `$ git:clone -a appname`<br>`$cd appname`
7. Deploy the repository:<br>`git add .`<br>`git commit -am "message"`<br>`git push heroku master`

## Resources Used 
- [FreeCodeComp django tutorial](https://www.youtube.com/watch?v=YZvRrldjf1Y&)
- [StackOverflow Threads 1](https://stackoverflow.com/questions/17341728/background-image-not-showing-in-safari)
- [StackOverflow Threads 2](https://stackoverflow.com/questions/44048156/django-filter-use-paginations)
- [Django Documentation](https://docs.djangoproject.com/en/3.0/)
- [django filter documentation](https://django-filter.readthedocs.io/en/master/guide/usage.html)
- [MDB Bootstrap Template](https://mdbootstrap.com/)
- [Travis CI](https://docs.travis-ci.com/)

## Credits

### Content
- All products, Images, Product description are from [Nike Store](https://www.nike.com)

### Media
- All the product photos are from nike.com and are used for educational purposes only. Nike and Nike Swoosh are registered trademarks belonging to Nike

### Acknowledgements