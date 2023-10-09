"""
URL configuration for sepDjangoCompleteProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views as my_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", my_views.home, name='home_url'),
    path('add-prod/', my_views.add_products, name='add-prod-url'),
    path('view-prod/', my_views.view_products, name='view-prod-url'),
    path('register/', my_views.register, name='register-url'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login-url'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout_url'),
    path('delete/<id>', my_views.delete, name='delete-url'),
    path('update/<id>', my_views.update_product, name='update-url'),
    path('pay/<id>', my_views.pay, name='pay-url')

]
