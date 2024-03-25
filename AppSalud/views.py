from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppSalud.models import Paciente, Doctor, Cita, Avatar
from AppSalud.forms import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator 

# Create your views here.

## VISTA DE INICIO
def inicio(request):
    if request.user.is_authenticated:
        mensaje = f"Bienvenido {request.user.username}"
    else:
        mensaje = "Inicia sesión para desbloquear todas las funciones"
    return render(request, "inicio.html", {'mensaje': mensaje})

## INICIAR SESIÓN
def iniciar_sesion(request):
    if request.method == "POST":
            formulario = AuthenticationForm(request, data = request.POST) #almacena la informacion el form

            if formulario.is_valid():
                info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

                usuario = authenticate(username = info_dic['username'], password = info_dic['password'])

                if usuario is not None : 
                    
                    login(request, usuario)

                return render(request, "inicio.html", {'mensaje':f'Bienvenido {usuario}'})
            
            else:
        
                return render(request, "inicio.html",{'mensaje':'Error en el inicio de sesión'})
    else:
        formulario = AuthenticationForm()  
    
    return render(request,'registro/inicio_sesion.html',{"formu":formulario})

## REGISTRARSE
def registrarse(request):

    if request.method == "POST":
        formulario = RegistroUsuario(request.POST)

        if formulario.is_valid():

            formulario.save()
            return render(request, "inicio.html", {"mensaje":"Usuario creado. Gracias por registrarte!"})
    
    else:
        formulario = RegistroUsuario()

    return render(request, "registro/registro.html", {"formu":formulario})

## AGREGAR AVATAR
@login_required
def agregar_avatar(request):

    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario_actual = User.objects.get(username=request.user)
            nuevo_avatar = Avatar(usuario= usuario_actual, imagen= info['imagen'])

            nuevo_avatar.save()
            return render(request, "inicio.html", {"mensaje":"Has creado tu avatar!"})
    
    else:
        formulario = AvatarFormulario()

    return render(request, "registro/nuevo_avatar.html", {"formu":formulario})


# EDITAR EL PERFIL
@login_required
def editarPerfil(request):

    usuario = request.user #cual es el usuario que tiene la sesion activa

    if request.method == 'POST':

        miFormulario = EditarUsuario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "inicio.html")

    else:

        miFormulario = EditarUsuario(initial={'username':usuario.username, 'first_name':usuario.first_name,
                                                'last_name':usuario.last_name, 'email': usuario.email})


    return render(request, "registro/editar_usuario.html", {"formu":miFormulario})

# CAMBIAR CONTRASEÑA

class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "registro/cambiar_contra.html"

# CERRAR SESIÓN

def cerrar_sesion(request):

    logout(request)

    return render(request, "inicio.html", {"mensaje":"Has cerrado sesión con éxito. Vuelve pronto!  "})

# ENVIAR MENSAJE
@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('inbox')  # Redirigir a la bandeja de entrada del usuario
    else:
        form = MensajeForm()
    return render(request, 'enviar_mensaje.html', {'form': form})

####################### VISTAS BASADAS EN FUNCIONES ####################

####################### CRUD DE PACIENTE #######################

### CREATE PACIENTE
def crear_paciente(request):
        if request.method == "POST":
            formulario = PacienteFormulario(request.POST, request.FILES) #almacena la informacion el form

            if formulario.is_valid():
                infopac = formulario.cleaned_data #convierte la info del form a un diccionario de python

                paciente_nuevo = Paciente(
                    nombre = infopac["nombre"],
                    fecha_nacimiento = infopac["fecha_nacimiento"],
                    direccion = infopac["direccion"],
                    telefono = infopac["telefono"],
                    imagen = infopac['imagen']
                    )
                
                paciente_nuevo.save()
                return render(request, "inicio.html")
            
        else:
            formulario = PacienteFormulario()

        return render(request, "pacientes/crear_paciente.html", {"formu":formulario})

### READ PACIENTES
def ver_pacientes(request):

    todos_pacientes = Paciente.objects.all() #obtener todos los pacientes que existen

    return render(request, "pacientes/ver_pacientes.html", {"total":todos_pacientes})

### UPDATE PACIENTES
@login_required
def actualizar_paciente(request, paciente_id):
    paciente_elegido = Paciente.objects.get(id=paciente_id)

    if request.method == "POST":
        formulario = PacienteFormulario(request.POST, request.FILES, instance=paciente_elegido)
        if formulario.is_valid():
            formulario.save()
            return render(request, "inicio.html")
    else:
        formulario = PacienteFormulario(instance=paciente_elegido)

    return render(request, "pacientes/actualizar_paciente.html", {"formu": formulario})

### DELETE PACIENTES

@method_decorator(login_required, name='dispatch')
class PacienteEliminar(DeleteView):
    model = Paciente
    template_name = "pacientes/borrar_paciente.html"
    success_url = '/AppSalud/'

####################### CRUD DE DOCTOR #######################

### CREATE DOCTOR
def crear_doctor(request):
        if request.method == "POST":
            formulario = DoctorForm(request.POST) #almacena la informacion el form

            if formulario.is_valid():
                infodoc = formulario.cleaned_data #convierte la info del form a un diccionario de python

                doctor_nuevo = Doctor(
                    nombre = infodoc["nombre"],
                    especialidad = infodoc["especialidad"],
                    telefono = infodoc["telefono"],
                    correo = infodoc["correo"],
                    )
                
                doctor_nuevo.save()
                return render(request, "inicio.html")
            
        else:
            formulario = DoctorForm()

        return render(request, "doctores/crear_doctor.html", {"formu":formulario})

### READ DOCTOR
def ver_doctores(request):

    todos_doctor = Doctor.objects.all() #obtener todos los doctores que existen

    return render(request, "doctores/ver_doctores.html", {"total":todos_doctor})
    
### UPDATE DOCTOR
@method_decorator(login_required, name='dispatch')
class DoctorEditar(UpdateView):
    model = Doctor
    template_name = 'doctores/actualizar_doctor.html'
    fields = ['nombre','especialidad']
    success_url = '/AppSalud/'

### DELETE DOCTOR
@method_decorator(login_required, name='dispatch')
class DoctorBorrar(DeleteView):
    model = Doctor
    template_name = "doctores/borrar_doctor.html"
    success_url = '/AppSalud/'

####################### CRUD DE SERVICIOS #######################

### CREATE SERVICIO
def crear_servicio(request):
        if request.method == "POST":
            formulario = ServicioForm(request.POST) #almacena la informacion el form

            if formulario.is_valid():
                infoserv = formulario.cleaned_data #convierte la info del form a un diccionario de python

                servicio_nuevo = ServicioMedico(
                    nombre = infoserv["nombre"],
                    descripcion = infoserv["descripcion"],
                    costo = infoserv["costo"],
                    )
                
                servicio_nuevo.save()
                return render(request, "inicio.html")
            
        else:
            formulario = ServicioForm()

        return render(request, "servicios/crear_servicio.html", {"formu":formulario})

### READ SERVICIOS
def ver_servicios(request):

    todos_servicio = ServicioMedico.objects.all() #obtener todos los servicios que existen

    return render(request, "servicios/ver_servicios.html", {"total":todos_servicio})

### UPDATE SERVICIOS
@method_decorator(login_required, name='dispatch')
class ServicioEditar(UpdateView):
    model = ServicioMedico
    template_name = 'servicios/actualizar_servicio.html'
    fields = ['nombre','descripcion','costo']
    success_url = '/AppSalud/'

### DELETE SERVICIOS
@method_decorator(login_required, name='dispatch')
class ServicioBorrar(DeleteView):
    model = ServicioMedico
    template_name = "servicios/borrar_servicio.html"
    success_url = '/AppSalud/'

####################### CRUD DE CITAS ####################### 

### CREATE CITAS
def agendar_cita(request):
    infocita = {}

    if request.method == 'POST':
        formulario = CitaForm(request.POST)
        
        if formulario.is_valid():
             infocita = formulario.cleaned_data #convierte la info del form a un diccionario de python

        cita_nueva = Cita.objects.create(
                paciente= infocita.get("paciente"),
                fecha= infocita.get("fecha"),
                medico= infocita.get("medico"),
                motivo= infocita.get("motivo"),   
                servicio= infocita.get("servicio"),  
        )

        cita_nueva.save()
        return render(request, "inicio.html")
    
    else:
        form = CitaForm()

    return render(request, 'citas/agendar_cita.html', {'formu': form})


### BUSCAR CITA
def buscar_cita(request):
    
    if request.GET:
        paciente = request.GET["paciente"]  #leer el diccionario de info del formulario y obtengo el valor de busqueda
        cita = Cita.objects.filter(paciente__nombre__icontains=paciente) #filtrar todos las citas que tengan dicho nombre!!

        mensaje = f"Estamos buscando las citas del paciente {paciente}"

        return render(request, "citas/buscar_cita.html", {"mensaje":mensaje, "resultados":cita})

    
    return render(request, "citas/buscar_cita.html") #si todavia no hay una busqueda

### READ CITAS
def ver_citas(request):

    todos_citas = Cita.objects.all() #obtener todos las citas creadas

    return render(request, "citas/ver_citas.html", {"total":todos_citas})
    
### UPDATE CITA
@method_decorator(login_required, name='dispatch')
class CitaEditar(UpdateView):
    model = Cita
    template_name = 'citas/actualizar_cita.html'
    fields = ['fecha','medico','motivo','servicio']
    success_url = '/AppSalud/'

### DELETE CITA
@method_decorator(login_required, name='dispatch')
class CitaBorrar(DeleteView):
    model = Cita
    template_name = "citas/borrar_cita.html"
    success_url = '/AppSalud/'

####################### VISTAS BASADAS EN CLASES ####################

# Ver Doctores
class DoctorLista(ListView):
    model = Doctor
    template_name = 'doctores/lista_doctores.html'

# Crear Doctor
class DoctorCrear(CreateView):
    model = Doctor
    template_name = "doctores/nuevo_doctor.html"
    fields = ['nombre','especialidad']
    success_url ='/AppSalud/ver_doctores/'

# Delete del Doctor
class DoctorBorrar(DeleteView):
    model = Doctor
    template_name = "doctores/borrar_doctor.html"
    success_url = '/AppSalud/'


############## ABOUT US ####################
    
def about_us(request):
    return render(request, "registro/about.html")