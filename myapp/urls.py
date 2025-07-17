from django.urls import path
from myapp import views

# App namespace - helps avoid URL naming conflicts
app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:book_id>/', views.detail, name='detail'),

    # Part 1: Feedback form
    path('feedback/', views.getFeedback, name='feedback1'),

    # Part 2: Search form
    path('findbooks/', views.findbooks, name='findbooks'),

    path('place_order/', views.place_order, name='place_order'),
]