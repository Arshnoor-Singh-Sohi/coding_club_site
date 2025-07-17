from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book, Publisher, Member, Order
from django.shortcuts import render

from .forms import FeedbackForm, SearchForm, OrderForm

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

def getFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.cleaned_data['feedback']

            if feedback == 'B':
                choice = ' to borrow books.'
            elif feedback == 'P':
                choice = ' to purchase books.'
            else:
                choice = ' None.'

            return render(request, 'myapp/fb_results.html', {'choice': choice})
        else:
            return HttpResponse('Invalid Data')
    else:
        form = FeedbackForm()
        return render(request, 'myapp/feedback.html', {'form': form})
    
def findbooks(request):
    """
    UPDATED view to handle:
    - Optional category field (Part 3b)
    - New max_price field with filtering (Part 3c)
    """
    
    if request.method == 'POST':
        # User submitted the search form
        form = SearchForm(request.POST)
        
        if form.is_valid():
            # Get the validated data from the form
            name = form.cleaned_data['name']        # User's name (could be empty)
            category = form.cleaned_data['category'] # Selected category (could be empty now!)
            max_price = form.cleaned_data['max_price'] # Maximum price (required)
            
            # PART 3: Updated filtering logic
            # Start with books that cost less than or equal to max_price
            booklist = Book.objects.filter(price__lte=max_price)
            
            # If a category was selected, filter by category too
            if category:  # Only filter by category if user selected one
                booklist = booklist.filter(category=category)
            
            # Get the readable category name for display
            category_display = None
            if category:
                # Convert category code to readable name
                category_choices = dict(SearchForm.CATEGORY_CHOICES)
                category_display = category_choices.get(category)
            
            # Pass data to the results template
            context = {
                'name': name,                   # User's name
                'category': category_display,   # Readable category name
                'booklist': booklist,          # Filtered books
                'max_price': max_price         # Maximum price for display
            }
            return render(request, 'myapp/results.html', context)
        else:
            # Form has errors - show the form again with error messages
            return render(request, 'myapp/findbooks.html', {'form': form})
    
    else:
        # GET request - show empty search form
        form = SearchForm()
        return render(request, 'myapp/findbooks.html', {'form': form})

def place_order(request):
    """
    This view handles placing new orders using ModelForm.
    This form allows users to place orders for book(s).
    """
    
    if request.method == 'POST':
        # User submitted the order form
        form = OrderForm(request.POST)
        
        if form.is_valid():
            # Get the selected books before saving
            books = form.cleaned_data['books']
            
            # Save the order but don't commit to database yet (commit=False)
            order = form.save(commit=False)
            
            # Get member and order type from the saved order
            member = order.member
            order_type = order.order_type
            
            # Now save the order to the database
            order.save()
            
            # IMPORTANT: For ManyToMany fields, save the relationships after saving the main object
            form.save_m2m()  # This saves the books relationship
            
            # Special logic for borrow orders (order_type = 1)
            if order_type == 1:  # If this is a borrow order
                # Add each book to the member's borrowed_books
                for book in order.books.all():
                    member.borrowed_books.add(book)
            
            # Render success page with order details
            return render(request, 'myapp/order_response.html', {
                'books': books, 
                'order': order
            })
        else:
            # Form has errors - show the form again with error messages
            return render(request, 'myapp/placeorder.html', {'form': form})
    
    else:
        # GET request - show empty order form
        form = OrderForm()
        return render(request, 'myapp/placeorder.html', {'form': form})