# STR:WER - eCommerce Street Wear Shop
[![Build Status](https://travis-ci.org/delegacz/md-milestone-4.svg?branch=master)](https://travis-ci.org/delegacz/md-milestone-4)

[Visit Live Project](https://md-milestone-project-4.herokuapp.com/)

STR:WER is a ecommerce shop for all things street wear, manualy picked inventory of the most desirables items from the world of street wear. 

Use code: 123ABC for 100$ OFF
 
## UX
### Who is this website for?
This website is aimed at people who are interested in a street wear culture and would like to purchase clouthing articles(Sneakers, and Outdoor/Outer Cloathing)

### What does it fulfill?
This website fulfills the need of users to discover and purchase products by providing a range of products and an ability to order and pay for them

### User Stories 

- As a user , I want add product to the cart , so that I can purchase it.
- As a user, I want to fill an refund form, so that I can revice refund for returned product
- As a user, I want to sing up, so that I can make a purchase
- As a user, I want to search through products, so that I cant find a jacket I want


## Features

 
### Existing Features
- Refunds - allows customer to request a refund by providing ref code and submitting a form
- Coupon Codes  - allows users to lower the price of the order by using code at checkout
- Pagination - allows user to browse through products by changing displayed page
- Add to Cart - Allows users to add an item to the cart for later checkout, cart page also gives user an opportunity to modify quantity of the product or remove it before progressing to checkout
- Stripe Integration - Allows users to pay for thier order using Stripe
- Order Summary - Allows users to see an detailed view at thier order on checkout page and apply coupon code for a discount 


### Features Left to Implement
- Size Selector
- Gender Selector
- More product Categories
- Product Reviews
- Advanced product Gallery


## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Stripe](https://stripe.com/)
    - The project uses **Stripe** for credit/debit cart processing and payment gateway
- [Django](https://www.djangoproject.com/)
    - The project uses **Django** as python web framework
- [Python](https://www.python.org/)
    - The project uses **Python** as a main programic language
- [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - The project uses **AllAuth** to provide ability to Sign in/ Log In for users
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - The project uses **Crispy Forms** to simplify styling of django generated forms
- [django countries](https://pypi.org/project/django-countries/)
    - The project uses **Django Countries** to provice Country choice field in the forms
- [django filter](https://django-filter.readthedocs.io/en/master/guide/usage.html)
    - The project uses **Django Filter** to provice search and pagination functionality
- [Pillow](https://pillow.readthedocs.io/en/stable/)
    - The project uses **Pillow** as python Imaging Library
- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** to simplify and streamline template creation process
- [JavaScript](https://www.javascript.com/)
    - The project uses **JavaScript** for DOM manipulation and Stripe integration
- [Git](https://git-scm.com)
    - The project uses **GIT** for version controll and backup
- [GitHub](https://github.com)
    - The project uses **Github** for remote repository storage and commit log
- [Heroku](https://www.heroku.com/home)
    - The project uses **Heroku** as a deployment platform and hosting
- [Amazon Web Services - AWS](https://aws.amazon.com)
    - The project uses **AWS** for image/file storage
- [Travis CI](https://travis-ci.org)
    - The project uses **Travis CI** for continuous integration

## Testing
Unit tests were written form models, views and froms and can be accesed in `ecommerce/test.py` and can be run in console by using `python manage.py test`. 
- Model Tests - Checks that models given data, calculate and output it properly
- View Testing - Checks if view given data output to correct template and request comes back with status 200,. Some view could not be tested as I couldnt figure out how to test views that are calling other methods for values
- Form Validity Testing - Checks if forms are valid, the checkout form could not tested as I could not figure out how to test CountryField provided by django countries
### Front-end Testing

Website was tested on multipule brosers(Firefox, Chrome, Opera, Safari) and divices(Iphone X, Iphone Xr) in order to tests mobile responsivity and if all CSS and JavaScript function properly, One issue was found. See Below in **Issues Found**
### Travis CI
Project uses Tavis CI for Build Testing per Commit

Travis Setup Process:
##### 
##### Setting up Envirement Virables for Travis CI
- Virables are added in project configuration tab `More Options > Settings`
- SECRET_KEY had to be encrypted following these steps in command line:

`travis login --pro`

`travis encrypt SOMEVAR="secretvalue" --add`

### Code Validation
Code was validated using followig:
 - [W3 HTML Validator](https://validator.w3.org) - HTML Validation
 - [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) - CSS Validation
 - [JS Hint](https://jshint.com) - JavaScript Validation
### Issues Found
1.

In Safari CSS `background-image: url();` does not display a background image when image is not saved properly. For example `.jpg` will not work if these creteria are not met:
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
- All the product photos are from nike.com and are used for educational purposes only, Nike and Nike Swoosh are registered trademaks belonging to Nike

### Acknowledgements