# Library - CSoC Dev Task 2

## Introduction

Welcome to the Week 2 of CSOC Dev. In this assignment, you will be working on the Django backend of a library web application. A boilerplate has already been created for you and all that remains is to fill in the code wherever we've asked you to, or wherever you feel required.

A very basic frontend has already been created for visualizing the results. You need not mess with it until the later stages of the assignment.


### Setting up the project

- Make sure `python3.7` and `pip` are installed. Install `pipenv` by running `pip install pipenv`.
- Install python dependencies using the command `pipenv install` Please use only pipenv for managing dependencies (Follow this [link](https://realpython.com/pipenv-guide/) if you are new to pipenv).
- To activate this project's virtualenv, run `pipenv shell`.
- Run `python manage.py migrate` to apply migrations.
- Start the development server using `python manage.py runserver`

### Working
* There will be several books present in the Library, which can be added or removed only from the backend (Book model).
* Every book will have several instances. Again, this can be added or removed only from the backend. Note that each instance denotes a physical copy of the book (BookCopy model).
* As an example, if a book B1 has 5 copies, then there shall be 5 BookCopy instances corresponding to the book B1.
* While borrowing a book, a logged in user can borrow any instance of the BookCopy model whose status is available. A user is allowed to borrow multiple copies of the same book. After successfully borrowing a copy, the number of copies of the book available in the library will decrease. That is, if the user borrows the book B1, then the number of instances of book B1 will become 4. The instance won't get deleted on borrowing as it represents a physical copy of the book.
* A user can return a copy of the book, and thereby, the number of copies of the book available will increase by 1, for each book copy returned.
* The library system would also allow the user to rate a particular book, which will be used to calculate the average rating of the book. The ratings will be given to a book, and not to the copy of a book. Also, a user can rate a book multiple times, and in that case, only the last rating given by the user to the book will persist.


## Tasks
#### Stage 1 (50 Points)
Complete the following views without altering the frontend. Necessary details have been mentioned as comments in the views themselves. Only a logged in user can view the loaned books or issue a book.

* Book Detail View
* Book List View
* View Loaned Books
* Issue a Book

#### Stage 2 (30 Points)
Complete the view for returning an issued book. You need to write this view all by yourself.
* Your view will accept Book Copy ID as an argument and mark the appropriate Book Copy as returned and return an appropriate response.
* You additionally need to write the JavaScript code to make a POST request to your view and display an appropriate message to the user after the response arrives.

#### Stage 3 (60 Points)
In this stage, you will need to implement a rating system all by yourself.
* You may need to fiddle around with the models, create some new views and make changes to the existing templates.
* Your system should allow the user to enter any integer between 0 to 10 (both inclusive) and the final rating would be the average of all the user ratings given to the book and should be a real number.
* The ratings would be given to a Book issued by a user, and not a Book Copy.
* The ratings must be modifiable. Also, if a user has rated a book multiple times, then only the last rating given by the user should matter, any previous ratings should not contribute to the average rating of the book.
* As an example, if there are two users U1 and U2, and they have rated a book as 8 and 10, respectively, then the average rating would be 9.0. If the user U1 later changes the rating to 9, then the average rating of the book should become 9.5.
* Only a logged in user should be allowed to rate a book, but others may view the average rating of the book.
* You can add an integer field with a submit button in the Book Detail template or the Book List template itself.
> **_NOTE:_**  This work must be done in the store app itself.

#### Stage 4 (60 Points)
In the authentication app, fill in the views for login, logout and user registration. You will also need to create basic frontend templates for these views. Refer to the existing templates if you have any issue.

## Deadline
You'll have a week to complete this task. Hence, the deadline of this task is 7th May, 2020.

## Submission
* Follow the instructions to setup and run this project.
* Complete the task by making the required changes in the files.
* When done, commit your work locally and push it to your origin (forked repository).
* Make a pull request to our repository, stating the tasks which you have completed.
* Let us review your pull request.

