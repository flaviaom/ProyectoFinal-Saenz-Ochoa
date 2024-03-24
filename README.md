# ProyectoFinal-Saenz-Ochoa
Proyecto Final del curso de Python de CoderHouse, realizado en conjunto por Luis Sáenz y Flavia Ochoa.
Ambos construimos el concepto de la página y armamos los modelos en base a nuestras ideas. 
+ Flavia se encargó del diseño de la página y encontrar nuevas maneras de representar el contenido de la página. Esto implicó principalmente la modificación de la plantilla html "padre" y asegurarse que las demás plantillas heredadas se visualicen correctamente, así como que estén debidamente conectadas a las vistas y urls del Proyecto.
+ Luis creó los 4 modelos y sus CRUDs respectivos, asegurando el ciclo completo desde la creación del modelo, los formularios y las vistas. Algunas vistas están basadas en funciones y otras están basadas en clases. Un punto importante fue asegurar la correcta migración de los modelos y creación de base de datos. También revisó que los urls cumplan su propósito. 

Fue un súper trabajo en equipo :) 

## Introducción
Esta es una web para una clínica, que sirve como un portal de gestión para el personal de la clínica (Usuarios), quienes pueden Crear, Ver, Editar y Eliminar Pacientes, Doctores, Servicios y Citas. 

## Link a video
En este video se muestran las principales funcionalidades de la página.
Link: ``

## Pasos para iniciar
1. Primero hacer las migraciones de ser necesario: `python manage.py makemigrations`
2. Seguido del migrate: `python manage.py migrate`
3. Finalmente para correr el servidor: `python manage.py runserver`

## SUPERUSER  
usuario: flavialuis
contraseña: python1234

## Modelos
Esta página tiene 6 modelos creados
+ Usuario: username, Nombre, Apellido, Email, Contraseña, Avatar 

+ Paciente: Nombre, Fecha de nacimiento, Dirección, Teléfono e Imagen
+ Doctor: Nombre, Especialidad, Teléfono, correo
+ Servicio: Nombre, Descripcion, Costo
+ Cita: Paciente, Médico, Fecha, Motivo y Servicio
+ Mensaje: Emisor, Receptor, Asunto, Contenido y Fecha de Envío

## Formularios
### Para insertar datos
+ Crear Usuario
+ Crear Paciente
+ Crear Doctor
+ Crear Servicio
+ Agendar cita
### Para buscar datos
+ Buscar cita

## URLS
Accede a la aplicación en tu navegador web en la dirección `http://localhost:8000`.

### URLs Disponibles

- **Inicio**: `http://localhost:8000/`
- **Acerca de Nosotros**: `http://localhost:8000/about/`
- **Iniciar Sesión**: `http://localhost:8000/login/`
- **Registrarse**: `http://localhost:8000/signup/`
- **Cerrar Sesión**: `http://localhost:8000/logout/`
- **Editar Usuario**: `http://localhost:8000/edit/`
- **Cambiar Contraseña**: `http://localhost:8000/contra/`
- **Agregar Avatar**: `http://localhost:8000/avatar/`
- **Enviar Mensaje**: `http://localhost:8000/mensajes/`

#### CRUD de Modelos

##### Usuarios

- **Crear Usuario**: `http://localhost:8000/crear_usuario/`
- **Ver Pacientes**: `http://localhost:8000/ver_pacientes/`
- **Editar Paciente**: `http://localhost:8000/actualizar_paciente/<id_del_paciente>/`
- **Eliminar Paciente**: `http://localhost:8000/borrar_paciente/<id_del_paciente>/`

##### Doctores

- **Crear Doctor**: `http://localhost:8000/crear_doctor/`
- **Ver Doctores**: `http://localhost:8000/ver_doctores/`
- **Editar Doctor**: `http://localhost:8000/editar_doctor/<id_del_doctor>/`
- **Eliminar Doctor**: `http://localhost:8000/borrar_doctor/<id_del_doctor>/`

##### Servicios

- **Crear Servicio**: `http://localhost:8000/crear_servicio/`
- **Ver Servicios**: `http://localhost:8000/ver_servicios/`
- **Editar Servicio**: `http://localhost:8000/editar_servicios/<id_del_servicio>/`
- **Eliminar Servicio**: `http://localhost:8000/borrar_servicio/<id_del_servicio>/`

##### Citas

- **Agendar Cita**: `http://localhost:8000/agendar_cita/`
- **Buscar Cita**: `http://localhost:8000/buscar_cita/`
- **Ver Citas**: `http://localhost:8000/ver_citas/`
- **Editar Cita**: `http://localhost:8000/editar_cita/<id_de_la_cita>/`
- **Eliminar Cita**: `http://localhost:8000/borrar_cita/<id_de_la_cita>/`
