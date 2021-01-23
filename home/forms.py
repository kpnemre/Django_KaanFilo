from django import forms
from .models import Offer, ContactInfo

from crispy_forms.helper import FormHelper


class OfferForm(forms.ModelForm):
	class Meta:
		model = Offer
		fields = ['name','surname', 'company', 'email', 'number', 'city', 'number_of_car', 'renting_time', 'message']
		
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder']= "İsminiz"
		self.fields['name'].widget.attrs['class']= "form-control-sm"
		self.fields['surname'].widget.attrs['placeholder']= "Soyadınız"
		self.fields['surname'].widget.attrs['class']= "form-control-sm"
		self.fields['company'].widget.attrs['class']= "form-control-sm"
		self.fields['company'].widget.attrs['placeholder']= "Şirket"
		self.fields['email'].widget.attrs['class']= "form-control-sm"
		self.fields['email'].widget.attrs['placeholder']= "Email adresiniz"
		self.fields['number'].widget.attrs['class']= "form-control-sm"
		self.fields['number'].widget.attrs['placeholder']= "Telefon numaranız"
		self.fields['city'].widget.attrs['class']= "form-control-sm"
		self.fields['city'].widget.attrs['placeholder']= "Şehir adı"
		self.fields['number_of_car'].widget.attrs['class']= "form-control-sm"
		self.fields['number_of_car'].widget.attrs['placeholder']= "Kiralamaz istdeğiniz araç sayısı"
		self.fields['renting_time'].widget.attrs['class']= "form-control-sm"
		self.fields['renting_time'].widget.attrs['placeholder']= "Kiralamak istediğiniz gün sayısı"
		self.fields['message'].widget.attrs['class']= "form-control-sm"
		self.fields['message'].widget.attrs['placeholder']= "Mesajınız..."


		self.helper = FormHelper()
		self.helper.form_show_labels = False


class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactInfo
		fields = ('name', 'email', 'topic', 'content',)
		
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder']= "İsminiz"
		self.fields['name'].widget.attrs['class']= "form-control-sm"
		self.fields['email'].widget.attrs['placeholder']= "Email adresiniz"
		self.fields['email'].widget.attrs['class']= "form-control-sm"
		self.fields['topic'].widget.attrs['class']= "form-control-sm"
		self.fields['topic'].widget.attrs['placeholder']= "Konu"
		self.fields['content'].widget.attrs['class']= "form-control-sm"
		self.fields['content'].widget.attrs['placeholder']= "Mesajınız"
		self.helper = FormHelper()
		self.helper.form_show_labels = False 