from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm

# Create your views here.
def index(request):

    return render(request, 'mainapp/index.html',{
        'title': 'Inicio'
    })

def about(request):

    return render(request, 'mainapp/about.html',{
        'title': 'sobre-nosotros'
    })    

def register_page(request):
    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
# si el formulario es valio
        if register_form.is_valid():
            # se guarda 
            register_form.save()
            # redirect para retornar a otra pagina 

# mensaje flash
            messages.success(request, 'Te has registrado correctamente')

            return redirect('/inicio')
    return render(request, 'users/register.html',{
        'title': 'Registro',
        'register_form': register_form
    })    

def login_page(request):

    return render(request,'users/login.html',{
        'title': 'Identificate'
    })    

