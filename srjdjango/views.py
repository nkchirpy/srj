from django.shortcuts import render
from django.views.generic import TemplateView,CreateView


# Create your views here.

class Indexview(TemplateView):
    template_name = 'srjdjango/index.html'

class Homeview(TemplateView):
    template_name = 'srjdjango/home.html'

class Historyview(TemplateView):
    template_name = 'srjdjango/history.html'

class Produtview(TemplateView):
    template_name = 'srjdjango/products.html'

class Enquiryview(TemplateView):
    template_name = 'srjdjango/enquiry.html'

class Contactview(TemplateView):
    template_name = 'srjdjango/contactus.html'
