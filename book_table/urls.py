from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookTableView.as_view(), name='table')
]
