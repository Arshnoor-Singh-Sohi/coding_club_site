from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book, Publisher, Member, Order


def index(request):
    """
        Index - View Displays the main landing page with a list of books.
    """
    response = HttpResponse()

    # Get books ordered by primary key (id)
    booklist = Book.objects.order_by('id')
    booklist = Book.objects.all().order_by('id')[:10]

    # Create heading for books
    heading1 = '<p>' + 'List of available books: ' + '</p>'
    response.write(heading1)

    #Display each book
    for book in booklist:
        para = '<p>' + str(book.id) + ':' + str(book) + '</p>'
        response.write(para)

    # Get publishers ordered by city in descending order
    publishers = Publisher.objects.all().order_by('-city')

    # Create heading for publishers
    heading2 = '<p>' + 'List of publishers: ' + '</p>'
    response.write(heading2)

    # Display each publisher with name and city
    for publisher in publishers:
        para = '<p>' + publisher.name + ' - ' + publisher.city + '</p>'
        response.write(para)

    return response


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