# pylint: disable=trailing-whitespace
# trunk-ignore-all(isort)
# Lab 4 Part 3 - Django ORM Queries
# Save this as: part3_queries.py in your project root directory

import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiteS25.settings")
django.setup()

from myapp.models import Publisher, Book, Member, Order

def print_separator(title):
    """Helper function to create clean section separators"""
    print("=" * 60)
    print(f" {title}")
    print("=" * 60)

def run_all_queries():
    """Execute all Part 3 queries with formatted output"""
    
    # Basic listing queries
    print_separator("BASIC LISTING QUERIES")
    
    print("a. All books in the database:")
    books = Book.objects.all()
    for book in books:
        print(f"   - {book.title} ({book.get_category_display()}) - ${book.price}")
    print(f"   Total books: {books.count()}\n")
    
    print("b. All members in the database:")
    members = Member.objects.all()
    for member in members:
        print(f"   - {member.username}: {member.first_name} {member.last_name} ({member.get_status_display()})")
    print(f"   Total members: {members.count()}\n")
    
    print("c. All orders in the database:")
    orders = Order.objects.all()
    for order in orders:
        print(f"   - Order {order.pk}: {order.get_order_type_display()} by {order.member.username} on {order.order_date}")
    print(f"   Total orders: {orders.count()}\n")
    
    # Advanced filtering queries
    print_separator("ADVANCED FILTERING QUERIES")
    
    print("a. Members whose last name is 'Jones':")
    jones_members = Member.objects.filter(last_name='Jones')
    for member in jones_members:
        print(f"   - {member.username}: {member.first_name} {member.last_name}")
    print(f"   Total found: {jones_members.count()}\n")
    
    print("b. Publishers with headquarters in 'USA':")
    usa_publishers = Publisher.objects.filter(country='USA')
    for publisher in usa_publishers:
        print(f"   - {publisher.name} (City: {publisher.city})")
    print(f"   Total found: {usa_publishers.count()}\n")
    
    print("c. Members that live in 'Windsor':")
    windsor_members = Member.objects.filter(city='Windsor')
    for member in windsor_members:
        print(f"   - {member.username}: {member.first_name} {member.last_name}, {member.address}")
    print(f"   Total found: {windsor_members.count()}\n")
    
    print("d. Members that live on an 'Avenue' and live in AB province:")
    avenue_ab_members = Member.objects.filter(address__icontains='Avenue', province='AB')
    for member in avenue_ab_members:
        print(f"   - {member.username}: {member.first_name} {member.last_name}, {member.address}, {member.province}")
    print(f"   Total found: {avenue_ab_members.count()}\n")
    
    print("e. Members that have borrowed the book 'A New World':")
    new_world_borrowers = Member.objects.filter(borrowed_books__title='A New World')
    for member in new_world_borrowers:
        print(f"   - {member.username}: {member.first_name} {member.last_name}")
    print(f"   Total found: {new_world_borrowers.count()}\n")
    
    print("f. Books that cost more than $100.00:")
    expensive_books = Book.objects.filter(price__gt=100.00)
    for book in expensive_books:
        print(f"   - {book.title}: ${book.price}")
    print(f"   Total found: {expensive_books.count()}\n")
    
    print("g. Members that do NOT live in province AB:")
    non_ab_members = Member.objects.exclude(province='AB')
    for member in non_ab_members:
        print(f"   - {member.username}: {member.first_name} {member.last_name} ({member.province})")
    print(f"   Total found: {non_ab_members.count()}\n")
    
    print("h. Orders placed by a client whose first_name is 'Mary':")
    mary_orders = Order.objects.filter(member__first_name='Mary')
    for order in mary_orders:
        print(f"   - Order {order.pk}: {order.get_order_type_display()} on {order.order_date}")
    print(f"   Total found: {mary_orders.count()}\n")
    
    print("i. Members whose member status are 'Premium Member':")
    premium_members = Member.objects.filter(status=2)
    for member in premium_members:
        print(f"   - {member.username}: {member.first_name} {member.last_name}")
    print(f"   Total found: {premium_members.count()}\n")
    
    print("j. Books that have between 100 and 280 pages (inclusive) and belong to category 'Science&Tech':")
    science_books = Book.objects.filter(num_pages__gte=100, num_pages__lte=280, category='S')
    for book in science_books:
        print(f"   - {book.title}: {book.num_pages} pages")
    print(f"   Total found: {science_books.count()}\n")
    
    print("k. Get the first name of the Member of the Order with pk=1:")
    try:
        order_1 = Order.objects.get(pk=1)
        print(f"   - Order 1 member first name: {order_1.member.first_name}")
    except Order.DoesNotExist:
        print("   - Order with pk=1 does not exist")
    print()
    
    print("l. All Books that the Member with username 'bill' is currently borrowing:")
    try:
        bill_member = Member.objects.get(username='bill')
        bill_books = bill_member.borrowed_books.all()
        for book in bill_books:
            print(f"   - {book.title}")
        print(f"   Total books borrowed by bill: {bill_books.count()}")
    except Member.DoesNotExist:
        print("   - Member with username 'bill' does not exist")
    print()
    
    print("m. Members who live in AB and have auto_renew enabled:")
    ab_auto_renew = Member.objects.filter(province='AB', auto_renew=True)
    for member in ab_auto_renew:
        print(f"   - {member.username}: {member.first_name} {member.last_name}")
    print(f"   Total found: {ab_auto_renew.count()}\n")
    
    print("n. Books that 'mary' has purchased:")
    mary_purchases = Book.objects.filter(order__member__username='mary', order__order_type=0)
    for book in mary_purchases:
        print(f"   - {book.title}")
    print(f"   Total books purchased by mary: {mary_purchases.count()}\n")
    
    print("o. City where the headquarters of the publisher of the book borrowed by 'alan' is located:")
    try:
        alan_member = Member.objects.get(username='alan')
        alan_books = alan_member.borrowed_books.all()
        if alan_books.exists():
            book = alan_books.first()  # Assuming alan borrows exactly one book
            publisher_city = book.publisher.city
            print(f"   - Alan borrowed '{book.title}' published by {book.publisher.name} in {publisher_city}")
        else:
            print("   - Alan has not borrowed any books")
    except Member.DoesNotExist:
        print("   - Member with username 'alan' does not exist")
    print()
    
    print_separator("QUERY EXECUTION COMPLETED")
    print("All queries have been executed successfully!")

if __name__ == "__main__":
    run_all_queries()