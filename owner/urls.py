from django.urls import path
from owner import views
# owner/books/100
urlpatterns=[
    path('book/add',views.AddBookView.as_view(),name='addbook'),
    path('book/all',views.BookListView.as_view(),name='booklist'),
    path('book/<int:id>',views.BookDetailView.as_view(),name='bookdetail'),
    path('book/change/<int:id>',views.BookEditView.as_view(),name='book_edit'),
    path('book/remove/<int:id>',views.BookDeleteView.as_view(),name='bookremove')



]