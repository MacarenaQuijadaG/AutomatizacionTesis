from django.shortcuts import render
from .models import *
# necesario para la autenticacion de usuarios en django
from django.contrib.auth import authenticate, login 
#necesario para direccionar otra url
from django.shortcuts import redirect 
from django.contrib import messages
from django.core.validators import validate_email

# Create your views here.
def home(request):
    if request.user.is_authenticated:
      return redirect('dashboard')
    else:
        if request.method=='POST':
            email = ''
            password = ''
            for key, value in request.POST.items():
                if key == 'email':
                    email = value
                if key == 'password':
                    password = value
            print(email)
            print(password)
            email_valid = True
            try:
                validate_email(email)
            except:
                email_valid=False
            if email!='' and password!='' and email_valid:
                usuario = authenticate(email=email, password=password)
                if usuario is not None:
                    login(request, usuario)
                    return redirect('dashboard')
                else:
                    messages.error(request,'Error al autenticar, tu correo institucional o tu contraseña son incorrectas.')
            else:
                if not email_valid:
                    messages.error(request, "El correo ingresado no es un correo válido.")
                if not email:
                    messages.error(request, "Ingresa tu correo institucional.")
                if not password:
                    messages.error(request, "Ingresa tu password.")
        return render(request, 'usuario/home.html')