from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book, Publisher, Member, Order
from django.shortcuts import render


# def index(request):
#     booklist = Book.objects.all()
#     context = {'booklist': booklist}
#     print(f"Context: {context}")  # Debug
#     return render(request, 'myapp/index.html', context)

def index(request):
    booklist = Book.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'booklist': booklist})


def about(request):
    return render(request, 'myapp/about.html')
    # No context variables needed - we're not passing any data


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return  render(request, 'myapp/detail.html', {'book': book})
    # Context variable: {'book': book} passes the book to template