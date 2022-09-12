"""Django_Stdy01 URL Configuration

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
# from django.urls import path
from app01 import views  # 导入views
from django.urls import path, include
from captcha.views import captcha_refresh

urlpatterns = [
    path('index/', views.index),
    path('user/list/', views.user_list),
    path('news/', views.news),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
    path('info/delete/', views.info_delete),
    path('captcha/', include('captcha.urls')),  # 生成验证码
    path('refresh/', captcha_refresh),      # 点击可以刷新验证码
]
