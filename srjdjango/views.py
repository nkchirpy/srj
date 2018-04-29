from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from srjdjango.models import Wellsaid,Enquirymodel
from srjdjango.forms import Enquiryform

# Create your views here.

def wellsaidview(request):
    user_said = Wellsaid.objects.all()
    return render(request, 'srjdjango/wellsaid.html', { 'user_said': user_said })
class Landview(TemplateView):
    template_name = 'srjdjango/land.html'

class Homeview(TemplateView):
    template_name = 'srjdjango/home.html'

class Aboutusview(TemplateView):
    template_name = 'srjdjango/about_us.html'

class Historyofjewelview(TemplateView):
    template_name = 'srjdjango/hoj.html'

class Useofjewelview(TemplateView):
    template_name = 'srjdjango/uoj.html'

class Historyofgoldview(TemplateView):
    template_name = 'srjdjango/hog.html'

class Historyofsilverview(TemplateView):
    template_name = 'srjdjango/hos.html'

class Historyofnavaratnaview(TemplateView):
    template_name = 'srjdjango/hon.html'

class Goldview(TemplateView):
    template_name = 'srjdjango/gold.html'

class Giftview(TemplateView):
    template_name = 'srjdjango/gift.html'

class Tradview(TemplateView):
    template_name = 'srjdjango/trad.html'

class Navaratnaview(TemplateView):
    template_name = 'srjdjango/navaratna.html'

class Jewelcareview(TemplateView):
    template_name = 'srjdjango/jewelcare.html'

# class Enquiryview(TemplateView):
#     template_name = 'srjdjango/enquiry.html'

class Enquiryview(CreateView):

    model = Enquirymodel
    form_class = Enquiryform
    template_name = 'srjdjango/enquiry.html'


class Contactview(TemplateView):
    template_name = 'srjdjango/contactus.html'
