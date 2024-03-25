from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to="pacientes", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"

class Doctor(models.Model):
    opciones_especialidad = [
            ('pediatria', 'Pediatría'),
            ('cardiologia', 'Cardiología'),
            ('neurologia', 'Neurología'),
            ('psicologia', 'Psicología'),
            ('traumatologia', 'Traumatología'),
            ('oncologia', 'Oncología'),
            ('otros', 'Otros'),
        ]
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=30, choices = opciones_especialidad)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.especialidad} -- {self.nombre}"

class ServicioMedico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas_paciente')
    fecha = models.DateField()
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas_medico')
    motivo = models.TextField()
    servicio = models.ForeignKey(ServicioMedico, on_delete=models.CASCADE, related_name='citas_servicio', default=None, null= True)
    def __str__(self):
        return f"{self.fecha} -- {self.paciente}"
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    asunto = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto