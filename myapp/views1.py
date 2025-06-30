from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book, Publisher, Member, Order
from django.shortcuts import render


def index(request):
    """
        Index - View Displays the main landing page with a list of books.
    """
    booklist = Book.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index0.html', {'booklist': booklist})


def about(request):
    """"
        About view - Displays information about the ebook app
    """
    response = HttpResponse()
    message = '<p>This is an eBook APP</p>'
    response.write(message)
    return response


def detail(request, book_id):
    """
        Detail view - displays details for a specific book
    """
    # Use get_object_or_404 to automatically handle non-existent books
    book = get_object_or_404(Book, pk=book_id)

    response = HttpResponse()

    #Display book details
    title_para = '<p>Title: ' + book.title.upper() + '</p>'
    price_para = '<p>Price: $' + str(book.price) + '</p>'
    publisher_para = '<p>Publisher: ' + str(book.publisher) + '</p>'

    response.write(title_para)
    response.write(price_para)
    response.write(publisher_para)

    return response