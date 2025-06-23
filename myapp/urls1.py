from django.urls import path
from myapp import views1

# App namespace - helps avoid URL naming conflicts
app_name = 'myapp'

urlpatterns = [
    # URL pattern for index view
    # When someone visits myapp/, it calls views1.index
    path('', views1.index, name='index'),

    # URL pattern for about view  
    # When someone visits myapp/about, it calls views1.about
    path('about/', views1.about, name='about'),


    # URL pattern for detail view with book_id parameter
    # When someone visits myapp/5, it calls views1.detail with book_id=5
    # <int:book_id> captures an integer from the URL and passes it to the view
    path('<int:book_id>/', views1.detail, name='detail'),
]