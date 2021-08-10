"""greenhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.db import router
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 


#users
from users.views import users as users_views
from users.views.login import UserLoginAPIView as login

#products
from products import views


urlpatterns = [
    #users paths
    path('admin/', admin.site.urls),
    path('users/', users_views.UserListView.as_view(), name='users'),
    path('users/login/', login.as_view(), name='login'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/verify/', users_views.account_verification, name='verify'),
    
    #products paths
    path('products/create/', views.create, name='create'),
    path('products/list/', views.get_all, name='list'),
    path('products/get/<int:productId>/', views.get_one, name='get')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
