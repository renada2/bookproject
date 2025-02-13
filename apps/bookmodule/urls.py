from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="books.index"), 
    path('index2/<int:val1>/', views.index2, name='index2'), 
    path('list_books/', views.list_books, name= "books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"),
    
]
