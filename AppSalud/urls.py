from django.urls import path
from AppSalud.views import *

urlpatterns = [
    path('', inicio, name = 'Home'),
    path('about/',about_us, name = 'aboutus'),

    path('login/',iniciar_sesion, name = 'Login'),
    path('signup/',registrarse, name = 'Registrarse'),
    path('logout/',cerrar_sesion, name = 'Logout'), 
    path("edit/", editarPerfil, name="Editar Usuario"),
    path("contra/", CambiarContra.as_view(), name="Cambiar Contraseña"),
    path('avatar/', agregar_avatar, name='newavatar'),
    path('mensajes/', enviar_mensaje, name='newmessage'),

    # URL DE CRUD DE MODELOS

    path('crear_usuario/', crear_paciente, name='newuser'),
    path("ver_pacientes/", ver_pacientes, name='ver_pacientes'),
    path("actualizar_paciente/<int:paciente_id>/", actualizar_paciente, name="Editar Paciente"),
    path('borrar_paciente/<int:pk>', PacienteEliminar.as_view(), name= "Eliminar Paciente"),

    path('crear_doctor/', crear_doctor, name = 'newdoc'),
    path("ver_doctores/", ver_doctores, name = 'ver_doctores'),
    path('editar_doctor/<int:pk>', DoctorEditar.as_view(), name= "editar doctor"),
    path('borrar_doctor/<int:pk>', DoctorBorrar.as_view(), name= "borrar doctor"),

    path('crear_servicio/', crear_servicio, name='newserv'),
    path('ver_servicios/', ver_servicios, name='ver_servicios'),
    path('editar_servicios/<int:pk>', ServicioEditar.as_view(), name= "editar servicio"),
    path('borrar_servicio/<int:pk>', ServicioBorrar.as_view(), name= "borrar servicio"),

    path('agendar_cita/', agendar_cita, name = 'newcita'),
    path('buscar_cita/', buscar_cita, name = 'buscarcita'),
    path("ver_citas/", ver_citas, name = 'ver_citas'),
    path('editar_cita/<int:pk>', CitaEditar.as_view(), name= "editar cita"),
    path('borrar_cita/<int:pk>', CitaBorrar.as_view(), name= "borrar cita"),

    #url de CRUD hecho con clases

    path("lista_doctores/", DoctorLista.as_view()),
    path('nuevo_doctor/', DoctorCrear.as_view()),
]