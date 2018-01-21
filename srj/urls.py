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
from django.conf import settings
from django.conf.urls.static import static
from srjdjango import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Homeview.as_view(),name='home'),
    url(r'^about_us$',views.Aboutusview.as_view(),name='about_us'),
    url(r'^history_of_jewel$',views.Historyofjewelview.as_view(),name='hoj'),
    url(r'^use_of_jewel$',views.Useofjewelview.as_view(),name='uoj'),
    url(r'^history_of_gold$',views.Useofjewelview.as_view(),name='hog'),
    url(r'^products/gold$',views.Goldview.as_view(),name='gold'),
    url(r'^products/silver$',views.Goldview.as_view(),name='silver'),
    url(r'^products/navaratna$',views.Goldview.as_view(),name='navaratna'),
    url(r'^jewel_care$',views.Jewelcareview.as_view(),name='jewelcare'),
    url(r'^enquiry$',views.Enquiryview.as_view(),name='enquiry'),
    url(r'^wellsaid$',views.wellsaidview,name='wellsaid'),
    url(r'^contact_us$',views.Contactview.as_view(),name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
