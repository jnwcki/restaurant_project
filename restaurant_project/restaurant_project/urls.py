"""restaurant_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from main import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from main.views import MainView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout_then_login, name='logout'),
    url(r'^restaurants/$', views.RestaurantListView.as_view(), name='restaurant_list_view'),
    url(r'^restaurant/(?P<pk>\d+)$', views.RestaurantDetailView.as_view(), name='restaurant_detail_view'),
    url(r'^order_history/$', views.OrderHistoryView.as_view(), name='order_history_view'),
    url(r'^restaurant/(?P<pk>\d+)/create_order/$', login_required(views.OrderCreateView.as_view()), name='order_create_view'),
    url(r'^order_comfirmation/(?P<pk>\d+)$', views.OrderConfirmationView.as_view(), name='order_confirmation_view'),
    url(r'^order_summary/(?P<pk>\d+)$', views.OrderDetailView.as_view(), name='order_detail_view'),
    url(r'^order/(?P<pk>\d+)/update/$', views.OrderUpdateView.as_view(), name='order_update_view'),
    url(r'^item/(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='item'),
    url(r'^$', MainView.as_view(), name="main_view"),
    url(r'^signup/consumer/$', views.SignupConsumer.as_view(), name='signup'),
    url(r'^signup/manager/$', views.SignupManager.as_view(), name='signup_manager'),
    url(r'^update_profile/(?P<pk>\d+)$', views.UserProfileUpdate.as_view(), name='update_profile_view'),
]
