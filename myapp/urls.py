from django.urls import path
from myapp import views

# App namespace - helps avoid URL naming conflicts
app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:book_id>/', views.detail, name='detail'),
]