from django.shortcuts import render, HttpResponse, redirect
from .forms import NewContactForm, AddressForm, PhoneForm
from contactos.models import Contact, Address, Phone
# Create your views here.

def index(request):
    vista = 'Contactos'
    
    contactos = Contact.objects.order_by('name')

    return render(request, 'index.html', 
                {'vista' : vista,
                'contactos' : contactos})


def New_Contact(request):
    vista = 'Nuevo Contacto'
    new_contact_form = NewContactForm()
    return render(request, 'new_contact.html', {
        'vista' : vista,
        'form': new_contact_form})



def save_contact(request):

    if request.method == 'POST':

        name = request.POST['name']
        lastname = request.POST['lastname']
        photo = request.POST['photo']
        birthday = request.POST['birthday']

        contact = Contact(
            name = name,
            lastname = lastname,
            photo = photo,
            birthday = birthday
        )

        contact.save()

        created = Contact.objects.order_by('updated_at').last()

        primary_key = created.id

        print(created)
        print(primary_key)
        return redirect('edit', id=primary_key)
    

def edit_contact(request, id):

    contact = Contact.objects.get(pk=id)

    contact.name
    contact.lastname
    contact.photo
    contact.birthday
    primary_key = contact.id

    if request.method == 'POST':

        phone_form_in = PhoneForm(request.POST)
        address_form_in = AddressForm(request.POST)

        if  phone_form_in.is_valid():

            phone_type_options = request.POST['types']
            alias = request.POST['alias']
            number = request.POST['number']
            
            phone = Phone(
                phone_type_options = phone_type_options,
                alias = alias,
                number = number,
                contact_id = primary_key

            )

            phone.save()

            return redirect('index')
        
        elif address_form_in.is_valid():
            
            street = request.POST['street']
            exterior_number = request.POST['exterior_number']
            internal_number = request.POST['internal_number']
            neighborhood = request.POST['neighborhood']
            municipality = request.POST['municipality']
            state = request.POST['state']
            references = request.POST['references']

            address = Address(
                street = street,
                exterior_number = exterior_number,
                internal_number = internal_number,
                neighborhood = neighborhood,
                municipality = municipality,
                state = state,
                references = references,
                contact_id = primary_key
            )

            address.save()

            return redirect('index')

        return redirect('index')

    vista = 'Editar'
    addressform = AddressForm()
    contact_form = NewContactForm()
    phone_form = PhoneForm()

    return render(request, 'edit_contact.html', {
        'addressform' : addressform,
        'form' : contact_form,
        'phoneform' : phone_form,
        'vista' : vista})


def delete_contact(request, id):

    contact = Contact.objects.get(pk=id)

    contact.delete()

    return redirect('index')