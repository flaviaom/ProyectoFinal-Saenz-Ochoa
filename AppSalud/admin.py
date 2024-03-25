from django.contrib import admin
from AppSalud.models import *

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Cita)
admin.site.register(Avatar)
admin.site.register(ServicioMedico)
admin.site.register(Mensaje)