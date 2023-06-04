"""shop_locator URL Configuration

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
from django.urls import path
from shops.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', shop_list, name='shop_list1'),
    # path('all_shops/', shops, name='shops'),
    path('', all_shop_list, name='shop_list'),
    path('shops/<int:pk>/', shop_detail, name='shop_detail'),
    path('shops/create/', shop_create, name='shop_create'),
    path('shops/<int:pk>/update/', shop_update, name='shop_update'),
]
