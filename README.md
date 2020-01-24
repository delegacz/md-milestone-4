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

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project loo ks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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
- Free code Academy django tutorial
- Stack overflow threads
- Django Documentation
- django filter documentation
- md5 template
- 

## Credits

### Content
- All products, Images, Product description are from [Nike Store](https://www.nike.com)

### Media
- All the product photos are from nike.com and are used for educational purposes only, Nike and Nike Swoosh are registered trademaks belonging to Nike

### Acknowledgements

- I received inspiration for this project from X








Used code
- [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Template](https://mdbootstrap.com/freebies/jquery/e-commerce/)
App description
- [Crispy Forms](#)
- [django countries](#)
- [bootstrap4](#)
- [Pillow](#)
main - project configuration
ecommerce - products managment
