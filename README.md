# Library - CSoC Dev Task 2

Welcome to week 2 of CSOC Dev. In this assignment, you will be working on the Django backend of a library web application. A boilerplate has been already been created for you and all that remains is to fill in code wherever we've asked you to.

A very basic frontend has already been created for visualizing the results. You need not mess with it until the later stages of the assignment.


### Setting up the project

- Install python dependencies using the command `pipenv install` Please use only pipenv for managing dependencies(Follow this [link](https://realpython.com/pipenv-guide/) if you are new to pipenv).
- Go to pipenv shell `pipenv shell`.
- Run `python manage.py migrate` to apply migrations.
- Start the development server using `python manage.py runserver`


## Tasks
#### Stage 1 (50 Points)
Complete the following views without altering the frontend. Necessary details have been mentioned as comments in the views themselves.

* Book Detail View (10 Points)
* Book List View (20 Points)
* View Loaned Books (10 Points)
* Issue a Book (10 Points)

#### Stage 2 (30 Points)
Complete the view for returning an issued book. You need to write this view all by yourself. Your view will accept book id as an argument and mark the appropriate book-copy as returned and return an appropriate response. You additionally need to write the javascript code to make a POST request to your view and display an appropriate message to the user after the response arrives.

#### Stage 3 (60 Points)
In this stage, you will need to implement a rating system all by yourself. You may need to fiddle arround with the models, create some new views and make changes to the existing templates. Your system should allow the user to enter any integer between 0 to 10(both inclusive) and the final rating would be the average of all user ratings and should be a real number.
We would prefer you to add an integer field with a submit button in the book detail template itself.
> **_NOTE:_**  This work must be done in the store app itself.

#### Stage 4 (60 Points)
In the authentication app, fill in the views for login, logout and user registration. You will also need to create basic frontend templates for these views. Refer to the existing templates if you have any issue.


