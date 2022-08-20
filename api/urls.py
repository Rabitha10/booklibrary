from django.urls import path
from api import views

urlpatterns=[
    path('books/all/',views.BooksView.as_view()),
    path('books/all/<int:id>',views.BookDetails.as_view())
]