# STR:WER - eCommerce Street Wear Shop
[![Build Status](https://travis-ci.org/delegacz/md-milestone-4.svg?branch=master)](https://travis-ci.org/delegacz/md-milestone-4)

[Visit Live Project](https://md-milestone-project-4.herokuapp.com/)

STR:WER is a ecommerce shop for all things street wear, manualy picked inventory of the most desirables items from the world of street wear.

Use code: 123ABC for 100$ OFF
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Refunds - allows customer to request a refund by providing ref code and submitting a form
- Coupon Codes  - allows users to lower the price of the order by using code at checkout
- Users Reviews - allows users to leave a review under a product


### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Stripe](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Django](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Python](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Crispy Forms](#)
    - The project uses **JQuery** to simplify DOM manipulation.
- [django countries](#)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Pillow](#)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Bootstrap](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [JavaScript](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Git](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [GitHub](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Heroku](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Amazon Web Services - AWS](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [StackOverflow](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Travis CI](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

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

## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

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
