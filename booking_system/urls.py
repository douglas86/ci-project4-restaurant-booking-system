"""
URL configuration for a booking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from about.views import AboutView
from book_table.views import BookTable
from home.views import HomePageView
from menu.views import MenuView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('admin/', admin.site.urls),
    path('menu/', MenuView.as_view(), name='menu'),
    path('table/', BookTable.as_view(), name='table'),
    path('', HomePageView.as_view(), name='home'),
]
