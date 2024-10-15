from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.book_list,name='list'),
    path('book/create/<int:pk>/',views.book_detail,name='detail'),
    path('book/add/',views.add_book,name='add_book'),
    path('book/update/<int:pk>/', views.update_book, name='update'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete'),

]