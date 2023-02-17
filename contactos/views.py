from django.shortcuts import render, HttpResponse, redirect
from .forms import NewContactForm, AddressForm, PhoneForm
from contactos.models import Contact, Address, Phone
from django.forms import formset_factory
# Create your views here.

def index(request):
    vista = 'Contactos'
    
    contactos = Contact.objects.order_by('name')

    return render(request, 'index.html', 
                {'vista' : vista,
                'contactos' : contactos})


def New_Contact(request):

    new_contact_form = NewContactForm()

    context = {
        'vista' : 'Nuevo contacto',
        'form': new_contact_form
        }
    
    return render(request, 'new_contact.html', context)



def save_contact(request):

    if request.method == 'POST':

        form = NewContactForm(request.POST)

        if form.is_valid():
            
            form.save()

            created = Contact.objects.order_by('updated_at').last()

            primary_key = created.id

            print(created)
            print(primary_key)
            return  redirect('edit', id=primary_key)


def edit_contact(request, id):
    contact = Contact.objects.get(pk=id)
    contact_form = NewContactForm(instance=contact)
    primary_key = contact.id

# EXCEPCION PARA TELÉFONO
    try:
        phone = Phone.objects.get(contact_id=contact.id)
        phone_form = PhoneForm(instance=phone)
        phone_form_post = PhoneForm(request.POST, instance=phone)
        phone_exist = True

    except Phone.DoesNotExist:
        phone_form = None
        phone_form_post = False
        #phone_form = PhoneForm(initial={'contact':contact})
        #phone_form_post = PhoneForm(request.POST)
        phone_exist = False

# EXCEPCION PARA DIRECCIÓN
    try:
        address = Address.objects.get(contact_id=contact.id)
        address_form = AddressForm(instance=address)
        address_form_post = AddressForm(request.POST, instance=address)
        address_exist = True

    except Address.DoesNotExist:
        address_form = AddressForm(initial={'contact':contact})
        address_form_post = AddressForm(request.POST)
        address_exist = False


    context = {
        'addressform': address_form,
        'form': contact_form,
        'phoneform': phone_form,
        'vista': 'Editar',
        'key': primary_key
    }


    if request.method == 'POST':

        contact_form = NewContactForm(request.POST, instance=contact)
        address_form_post
        phone_form_post

        if contact_form.is_valid() or address_form_post.is_valid() or phone_form_post.is_valid():
            contact_form.save()
            print('Se editó el contacto')

            address_form_post.save()

            print('Se creó o editó la dirección')
            return redirect('edit', id=primary_key)

        else:
            return redirect('index')

    else:
        return render(request, 'edit_contact.html', context)



def delete_contact(request, id):

    contact = Contact.objects.get(pk=id)

    contact.delete()

    return redirect('index')