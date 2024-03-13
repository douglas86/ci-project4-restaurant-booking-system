from django.urls import path

from . import views

app_name = 'book_table'

urlpatterns = [
    path('create/', views.BookTableCreateView.as_view(), name='create'),
    path('', views.BookTableView.as_view(), name='table')
]
