from django.shortcuts import render
from django.shortcuts import get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'store/index.html')

def bookDetailView(request, bid):
    template_name='store/book_detail.html'
    context={
        'book':None, # set this to an instance of the required book
        'num_available':None, # set this 1 if any copy of this book is available, otherwise 0
    }
    # START YOUR CODE HERE
    
    
    return render(request,template_name, context=context)


def bookListView(request):
    template_name='store/book_list.html'
    context={
        'books':None, # set here the list of required books upon filtering using the GET parameters
    }
    get_data=request.GET
    # START YOUR CODE HERE
    
    
    return render(request,template_name, context=context)

@login_required
def viewLoanedBooks(request):
    template_name='store/loaned_books.html'
    context={
        'books':None,
    }
    '''
    The above key books in dictionary context should contain a list of instances of the 
    bookcopy model. Only those books should be included which have been loaned by the user.
    '''
    # START YOUR CODE HERE
    


    return render(request,template_name,context=context)

@csrf_exempt
@login_required
def loanBookView(request):
    response_data={
        'message':None,
    }
    '''
    Check if an instance of the asked book is available.
    If yes, then set message to 'success', otherwise 'failure'
    '''
    # START YOUR CODE HERE
    book_id = None # get the book id from post data


    return JsonResponse(response_data)

'''
FILL IN THE BELOW VIEW BY YOURSELF.
This view will return the issued book.
You need to accept the book id as argument from a post request.
You additionally need to complete the returnBook function in the loaned_books.html file
to make this feature complete
''' 
@csrf_exempt
@login_required
def returnBookView(request):
    pass


