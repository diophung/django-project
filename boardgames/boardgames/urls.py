"""boardgames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_view

from main import views as main_views
from user import views as user_views
from tictactoe import views as tictactoe_views

admin.autodiscover()

urlpatterns = [
    url(r'^user/', user_views.home, name="user_home"),
    url(r'^admin/', admin.site.urls, name='boardgames_admin'),
    url(r'^$', main_views.home, name='boardgames_main_home'),
    url(r'^home/', main_views.home, name='boardgames_main_home'),
    url(r'^login/', auth_view.login, {'template_name': 'login.html'}, name='boardgames_login'),
    url(r'^logout/', auth_view.logout, {'next_page': 'boardgames_main_home'}, name='boardgames_logout'),
    url(r'^tictactoe/new_invitation', tictactoe_views.new_invitation, name="tictactoe_new_invitation"),
    url(r'^tictactoe/view_invitation', tictactoe_views.view_invitation, name="tictactoe_view_invitation")
]
