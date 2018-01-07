"""srj URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from srjdjango import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Indexview.as_view(),name='index'),
    url(r'^home$',views.Homeview.as_view(),name='home'),
    url(r'^products$',views.Produtview.as_view(),name='products'),
    url(r'^enquiry$',views.Enquiryview.as_view(),name='enquiry'),
    url(r'^contact_us$',views.Contactview.as_view(),name='contact'),


    
]
