from django.forms import ModelForm, DateInput, TextInput, formset_factory
from django import forms
from .models import all_states, phones_types, Contact, Address, Phone
from django.core.validators import RegexValidator

class NewContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'lastname', 'photo', 'birthday']
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
            'name' : TextInput(attrs={'type' : 'text'})
        }

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = [ 'contact', 'street', 'exterior_number', 'internal_number', 'neighborhood', 'municipality', 'state', 'references']
        widgets = {
            'contact': forms.HiddenInput()
        }

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['contact', 'phone_type_options', 'alias', 'number']
        widgets = {
            'contact': forms.HiddenInput()
        }

