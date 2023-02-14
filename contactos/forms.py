from django import forms
from .models import all_states, phones_types


class NewContactForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'nombre(s)',
        'type' : 'text'
        }),
        label = 'Nombre(s)*',
        max_length = 35,
        required=True
    )

    lastname = forms.CharField(
        widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'apellido(s)',
        'type' : 'text'
        }),
        label = 'Apellido(s)*',
        max_length = 35,
        required=True
    )

    photo = forms.FileField(
        widget=forms.FileInput(attrs={
        'class' : 'form-control'
        }),
        label = 'Foto',
        required=False
    )

    birthday = forms.DateField(
        widget=forms.DateInput(attrs={
        'class' : 'form-control',
        'type' : 'date'
        }),
        label = 'Fecha de Nacimiento',
        required=True
    )


class AddressForm(forms.Form):

    street = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'type' : 'text',
        'placeholder' : 'calle'
    }),
    label='Calle*',
    max_length=40,
    required=True
    )

    exterior_number = forms.CharField(widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'type' : 'number',
        'placeholder' : 'número exterior'
    }),
    label='Numero exterior*',
    max_length=10,
    required=True
    )

    internal_number = forms.CharField(widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'type' : 'number',
        'placeholder' : 'número interior'
    }),
    label='Número interior',
    max_length=5,
    required=False
    )

    neighborhood = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'type' : 'text',
        'placeholder' : 'colonia'
    }),
    label='Colonia*',
    max_length=60,
    required=True
    )

    municipality = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'type' : 'text',
        'placeholder' : 'municipio'
    }),
    label='Municipio*',
    max_length=60,
    required=True
    )

    state = forms.TypedChoiceField(widget=forms.Select(attrs={
        'class' :'form-control',
        'type' : 'select'
    }),
    label='Estado*',
    choices=all_states(),
    required=True
    )

    references = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'type' : 'text',
        'placeholder' : 'referencias...'
    }),
    label='Referencias',
    required=False,
    max_length=200
    )


class PhoneForm(forms.Form):

    types = forms.TypedChoiceField(widget=forms.Select(attrs={
        'class' : 'form-control',
        'type' : 'select'
    }),
    label='Tipo*',
    choices=phones_types,
    required=True
    )

    alias = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'alias'
    }),
    label='Alias*',
    required=True,
    max_length=30
    )

    number = forms.CharField(widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'type': 'number',
        'placeholder' : 'número telefónico'
    }),
    label='Numero*',
    required=True,
    max_length=10
    )