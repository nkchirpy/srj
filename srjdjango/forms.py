from django import forms
from .models import Enquirymodel

class Enquiryform(forms.ModelForm):




    class Meta:
        model = Enquirymodel
        fields = ['name','email_address','contact_number','comments']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control is-valid oval_border','placeholder':'Enter your name','id':'form-name','name':'person_name'}),

            'email_address':forms.TextInput(attrs={'class':'form-control is-valid oval_border','type':'email','placeholder':'example@domain.com','id':'form-email'}),

            'contact_number':forms.TextInput(attrs={'class':'form-control is-valid oval_border','type':'None','id':'form-contact'}),

            'comments':forms.Textarea(attrs={'class':'form-control is-valid oval_border1','id':'form-comments',}),

        }
