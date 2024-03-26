from django.urls import path

from . import views

app_name = 'book_table'

urlpatterns = [
    path('create/', views.BookTableCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.BookTableUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.BookTableDeleteView.as_view(), name='delete'),
    path('', views.BookTableView.as_view(), name='table')
]
