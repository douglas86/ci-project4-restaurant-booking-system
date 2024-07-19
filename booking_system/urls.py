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
from django.urls import path, include

from about.views import AboutView
from home.views import HomePageView
from .settings import DEBUG
from .views import UsernamePasswordResetView, ChangePasswordView

urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("accounts/password/reset/", UsernamePasswordResetView.as_view(), name="password_reset"),
    path("accounts/password/change/", ChangePasswordView.as_view(), name="password_change"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("menu/", include("menu.urls")),
    path("table/", include("book_table.urls")),
    path("", HomePageView.as_view(), name="home"),
]

# this logic is needed in development
# this will only run django_browser_reload during DEBUG True
if DEBUG == "True":
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
