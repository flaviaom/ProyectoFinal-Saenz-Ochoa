from django import forms
from AppSalud.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class PacienteFormulario(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'fecha_nacimiento', 'direccion', 'telefono', 'imagen']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad', 'telefono', 'correo']

    especialidad = forms.ChoiceField(choices=Doctor.opciones_especialidad, widget=forms.Select(attrs={'class': 'form-control'}))

class ServicioForm(forms.ModelForm):
    class Meta:
        model = ServicioMedico
        fields = ['nombre', 'descripcion', 'costo']

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

    widgets = {
        'fecha': forms.TextInput(attrs={'type': 'datetime-local'}),
    }

class RegistroUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class EditarUsuario(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['receptor', 'asunto', 'contenido']