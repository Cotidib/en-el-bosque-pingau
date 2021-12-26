# en-el-bosque-pingau
Proyecto de Ingeniería Audiovisual 2021

### Sitio publicado
* [Cotidib.pythonanywhere.com](Cotidib.pythonanywhere.com)
* https://enelbosque.pythonanywhere.com/

## Funcionamiento de la web

La página web fue desarrollada en el marco del Proyecto de Ingeniería Audiovisual del año 2021. Está destinada a dar contexto sobre los objetivos de la asignatura y a brindar información sobre las dos partes que componen el Proyecto de Ingeniería Audiovisual. Además de la difusión del proyecto en su conjunto, otro de los propósitos que cumple la página es gestionar un sistema de reservas para que se pueda visitar la instalación procurando mantener las medidas sanitarias y evitar las aglomeraciones durante el COVID-19.

La página fue desarrollada tanto para dispositivos móviles como de escritorio, bajo el método de diseño “mobile first”.

## Justificación de la elección de tecnología

La página fue desarrollada con el framework Django, usando HTML5, CSS3 y JavaScript para implementar el Front End y SQLite para la base de datos.

Particularmente, Django fue elegido como framework principal dado que ofrece un desarrollo rápido y tiene una curva de aprendizaje alcanzable para implementar el desarrollo Back End. Ello en conjunto con conocimientos previos de Python llevó a que este framework fuera la mejor opción.

En cuanto al uso de librerías externas, se utilizó Glider.js para la implementación de un slider con fotografías en la página principal y Masonry.js en conjunto con imagesLoaded para la implementación de una galería de fotografías en la página correspondiente al cortometraje.

## Dependencias y versiones
* Python versión 3.9
* Django versión 3.2.7
* Glider.js versión 1.0
* Masonry.js versión 4.2.2

## Instalacion y ejecucion local
1. Clonar repositorio de GitHub
2. Asegurarse de tener instalados Python y Django en sus versiones correspondientes. Django puede instalarse en un virtual environment.
3. En el archivo settings.py dentro de la carpeta pingauweb, cambiar DEBUG a True y ALLOWED_HOSTS a [] (array vacío).
4. Dentro de la carpeta raíz, usar el comando `python manage.py runserver` para correr la versión local.

## Especificaciones

### Definición, siglas y abreviaturas
A continuación se especificarán en detalle las definiciones de los términos más importantes utilizados, así como la explicación de las siglas y abreviaturas utilizadas.

* RF: Acrónimo para Requerimiento Funcional.
* RNF: Acrónimo para Requerimiento No Funcional.
* CU: Acrónimo para Caso de Uso. Un caso de uso es la definición de todos los pasos y/o actividades que un actor debe hacer para realizar una actividad o un proceso.

### Categorización
Los requerimientos funcionales y no funcionales definidos son categorizados de acuerdo a las siguientes categorías:

Esencial: Se entiende por requerimiento Esencial, a todo requerimiento que debe ser implementado con la máxima prioridad y que es imperativo para poder implementar otros requerimientos.
Deseable: Se entiende por requerimiento Deseable, a todo requerimiento que puede ser implementado o no, pero que aporta un alto valor a la aplicación.
Opcional: Se entiende por requerimiento Opcional, a todo requerimiento que no es sustancial para los usuarios de la aplicación pero que puede aportar cierto valor a la aplicación. Estos requerimientos no generan dependencia con otros requerimientos, por lo que su implementación queda a criterio de tiempo y costo disponible.

### Especificación de requerimientos funcionales

* RF1
Nombre: Enlaces Principales de Navegación en Escritorio.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio.
Descripción: La barra de navegación debe contar con los enlaces “Proyecto Ingau”, “Cortometraje”, “Instalación”, “Créditos” y “ Reservas” hacia sus respectivas páginas.

* RF2
Nombre: Enlaces Principales de Navegación en Dispositivo Móvil.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Móvil.
Descripción: La barra de navegación debe contar con los enlaces “Proyecto Ingau”, “Cortometraje”, “Instalación” y “Créditos” hacia sus respectivas páginas.

* RF3
Nombre: Submenu Proyecto Ingau.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El enlace “Proyecto Ingau” de la barra de navegación debe desplegar un submenú con los enlaces “Qué es”, “Los proyectos” y “Sobre nosotros”.

* RF4
Nombre: Submenu Cortometraje.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El enlace “Cortometraje” de la barra de navegación debe desplegar un submenú con los enlaces “Sinopsis”, “Ver” y “Detrás de escenas”.

* RF5
Nombre: Submenú Instalación.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El enlace “Instalación” de la barra de navegación debe desplegar un submenú con los enlaces “Qué es” y “Reservas”.

* RF6
Nombre: Pie de página.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: En el pie de la página, deben mostrarse enlaces directos hacia la página de Instagram y el email.

* RF7
Nombre: Qué es Proyecto Ingau.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página principal debe contar con una sección de información sobre la materia Proyecto de Ingeniería Audiovisual.

* RF8
Nombre: Los proyectos de Proyecto Ingau.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página principal debe contar con una sección de enlaces directos hacia la página del cortometraje y de la instalación.

* RF9
Nombre: Sobre nosotros del Proyecto Ingau.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página principal debe contar con una sección de fotografías tipo slider con los miembros del equipo.

* RF10
Nombre: Sinopsis del Cortometraje.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página del Cortometraje debe contar con una sección con la sinopsis.

* RF11
Nombre: Trailer del Cortometraje.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página del Cortometraje debe contar con una sección para el trailer, donde luego del estreno se sustituirá por el cortometraje.

* RF12
Nombre: Detrás de escenas del Cortometraje.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página del Cortometraje debe contar con una sección con fotografías dispuestas en galería tipo Masonry con imágenes del detrás de escenas del rodaje del cortometraje. 

* RF13
Nombre: Créditos.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página de Créditos debe contar con una sección con los roles y los nombres de los miembros del equipo que participaron en los proyectos.

* RF14
Nombre: Que es la Instalación.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página de la Instalación debe contar con una sección con información sobre la instalación.

* RF15
Nombre: Dónde está la Instalación.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página de la Instalación debe contar con un mapa donde se indique la ubicación de la instalación.

* RF16
Nombre: Formulario de reservas.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: La página de la Instalación debe contar con un formulario para realizar una reserva.

* RF17
Nombre: Campo Nombre en formulario de reservas.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El formulario de reserva debe contar con el campo obligatorio de texto “Nombre y Apellido”,

* RF18
Nombre: Campo Email en formulario de reservas.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El formulario de reserva debe contar con el campo obligatorio “Email” y solo admite formatos de email válidos.

* RF19
Nombre: Campo Cantidad de personas en formulario de reservas.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El formulario de reserva debe contar con el campo “Cantidad de personas” donde se debe poder seleccionar un número del 1 al 4.

* RF20
Nombre: Campo Dia en formulario de reservas.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El formulario de reserva debe contar con el campo “Día” donde se debe poder seleccionar “2021-11-25” o “2021-11-26”.

* RF21
Nombre: Campo Hora en formulario de reservas.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El formulario de reserva debe contar con el campo “Hora” donde se debe poder seleccionar un horario entre las 17:00 y las 21:00, cada uno con 15 minutos de duración.

* RF22
Nombre: Horarios disponibles según el día.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: Al seleccionar un día en el campo “Dia” del formulario de reserva, deben desplegarse los horarios disponibles para el día seleccionado en el campo “Hora”.

* RF23
Nombre: Boton Reservar.
Caracterización: Esencial.
Actor: Usuario.
Dispositivo: Escritorio y Móvil.
Descripción: El formulario de reserva debe contar con un botón de “Reservar”.

* RF24
Nombre: Deshabilitar hora ya reservada.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ Al enviar una reserva, la hora reservada debe dejar de mostrarse en el formulario.

* RF25
Nombre:​ Deshabilitar día con todas las horas reservadas.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ Si todas las horas de un mismo día fueron reservadas, ese día debe dejar de mostrarse en el formulario.

* RF26
Nombre:​ Deshabilitar botón Reservar.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ Si todos los horarios de todos los días ya fueron reservados, debe deshabilitarse el botón de “Reservar” y mostrar un mensaje de “Ya no quedan fechas disponibles”.

* RF27
Nombre:​ Confirmación de reserva.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ Al enviar una reserva, la página debe redirigir a una página de confirmación y el usuario debe recibir un email de confirmación en el email ingresado.

* RF28
Nombre:​ Página de carga.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ Debe mostrarse una página de carga siempre que se ingrese a una página cuyas imágenes todavía no se encuentren cargadas.

### Especificación de Requerimientos No Funcionales

* RNF1
Nombre:​ Acceso de adminsitrador.
Caracterización:​ Esencial.
Actor:​ Administrador.
Dispositivo: Escritorio y Móvil.
Descripción:​ Solamente el administrador debe poder ingresar al panel de control.

* RNF2
Nombre:​ Clave de acceso a email para aplicaciones.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ Para la configuración del envío de confirmación de email automático, debe utilizarse un token de acceso para aplicaciones de google en lugar de la contraseña del email.

* RNF3
Nombre:​ Ver reservas.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ En el panel de control deben poder verse las reservas registradas.

* RNF4
Nombre:​ Diseño responsivo.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ La página debe desplegarse correctamente tanto en dispositivos móviles como de escritorio.

* RNF5
Nombre:​ Optimización de imágenes.
Caracterización:​ Esencial.
Actor:​ Usuario.
Dispositivo: Escritorio y Móvil.
Descripción:​ Las fotografías debe estar optimizadas y deben tener el tamaño en pixeles correspondiente a lo que verdaderamente va a ocupar.

### Especificación de casos de uso

CU1
Nombre: Navegar a Proyecto Ingau.
Requerimientos: RF1, RF2.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página.
Curso básico: 
El usuario presiona el botón ‘Proyecto Ingau’ de la barra de navegación.
La página redirecciona hacia la página principal.

CU2
Nombre: Navegar a Cortometraje.
Requerimientos: RF1, RF2.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página.
Curso básico: 
El usuario presiona el botón ‘Cortometraje’ de la barra de navegación.
La página redirecciona hacia la página del cortometraje.

CU3
Nombre: Navegar a Instalación.
Requerimientos: RF1, RF2.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página.
Curso básico: 
El usuario presiona el botón ‘Instalación’ de la barra de navegación.
La página redirecciona hacia la página de la instalación.

CU4
Nombre: Navegar a Créditos.
Requerimientos: RF1, RF2.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página.
Curso básico: 
El usuario presiona el botón ‘Créditos’ de la barra de navegación.
La página redirecciona hacia la página de créditos.

CU5
Nombre: Navegar a Reservas.
Requerimientos: RF1.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página.
Curso básico: 
El usuario presiona el botón Reservas de la barra de navegación.
La página redirecciona hacia la sección de reservas de la página de la instalación.

CU6
Nombre: Submenu Proyecto Ingau.
Requerimientos: RF3.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página desde la versión de escritorio.
Curso básico: 
El usuario pasa el puntero sobre el botón Proyecto Ingau.
Se despliega un submenú con los enlaces “Qué es”, “Los proyectos” y “Sobre nosotros”.

CU7
Nombre: Submenu Proyecto Ingau.
Requerimientos: RF3.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página desde la versión movil.
Curso básico: 
El usuario presiona el botón ‘+’ junto al botón Proyecto Ingau.
Se despliega un submenú con los enlaces “Qué es”, “Los proyectos” y “Sobre nosotros”.

CU8
Nombre: Submenu Cortometraje.
Requerimientos: RF4.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página desde la versión de escritorio.
Curso básico:
El usuario pasa el puntero sobre el botón Cortometraje.
Se despliega un submenú con los enlaces “Sinopsis”, “Ver” y “Detrás de escenas”.

CU9
Nombre: Submenu Cortometraje.
Requerimientos: RF4.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página desde la versión móvil.
Curso básico:
El usuario presiona el botón ‘+’ junto al botón Cortometraje.
Se despliega un submenú con los enlaces “Sinopsis”, “Ver” y “Detrás de escenas”.

CU10
Nombre: Submenú Instalación.
Requerimientos: RF5.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página desde la versión de escritorio.
Curso básico:
Curso básico:
El usuario pasa el puntero sobre el botón Instalación.
Se despliega un submenú con los enlaces “Qué es” y “Reservas”.

CU11
Nombre: Submenú Instalación.
Requerimientos: RF5.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario ha ingresado a la página desde la versión móvil.
Curso básico:
Curso básico:
El usuario presiona el botón ‘+’ junto al botón Instalación.
Se despliega un submenú con los enlaces “Qué es” y “Reservas”.

CU12
Nombre: Enlaces en pie de página.
Requerimientos: RF6.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones:  El usuario ha ingresado a la página.
Curso básico:
El usuario presiona uno de los iconos del pie de página.
Se redirecciona al enlace correspondiente.

CU13
Nombre: Enlace directo a Cortometraje desde página principal.
Requerimientos: RF8.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página principal.
Curso básico:
El usuario navega hacia la sección ‘Los proyectos’.
Presiona el botón Cortometraje
La página redirecciona a la página del Cortometraje.

CU14
Nombre: Enlace directo a Instalación desde página principal.
Requerimientos: RF8 .
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página principal.
Curso básico:
El usuario navega hacia la sección ‘Los proyectos’.
Presiona el botón Instalación
La página redirecciona a la página de la Instalación.

CU15
Nombre: Uso del slider.
Requerimientos: RF9.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página principal.
Curso básico:
El usuario navega hacia la sección ‘Sobre nosotros’.
El usuario navega las fotografías en formato de slider.

CU16
Nombre: Reproduccion de video.
Requerimientos: RF11.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página Cortometraje.
Curso básico:
El usuario navega hacia la sección del trailer.
El usuario reproduce el video.

CU17
Nombre: Nombre y Apellido obligatorio en formulario de reserva.
Requerimientos: RF17.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página Instalación, en la sección reservas.
Curso básico:
El usuario completa el campo Nombre y Apellido.
El usuario completa los demás campos con datos válidos.
El usuario presiona el botón Reservar.
La reserva se completa correctamente.
Curso alternativo:
El usuario no completa el campo Nombre y Apellido.
El usuario completa los demás campos con datos válidos.
El usuario presiona el botón Reservar.
No es posible efectuar la reserva y se indica que el campo es obligatorio.

CU18
Nombre: Email obligatorio en formulario de reserva.
Requerimientos: RF18.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página Instalación, en la sección reservas.
Curso básico:
El usuario completa el campo Email con un dato válido.
El usuario completa los demás campos.
El usuario presiona el botón Reservar.
No es posible efectuar la reserva y se indica que el campo es obligatorio.
Curso alternativo 1:
El usuario no completa el campo Email.
El usuario completa los demás campos.
El usuario presiona el botón Reservar.
No es posible efectuar la reserva y se indica que el campo es obligatorio.
Curso alternativo 2:
El usuario completa el campo Email con un formato invalido.
El usuario completa los demás campos.
El usuario presiona el botón Reservar.
No es posible efectuar la reserva y se indica que el formato es incorrecto.

CU19
Nombre: Horarios disponibles según el día.
Requerimientos: RF22.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página Instalación, en la sección reservas.
Curso básico:
El usuario selecciona uno de los días en el campo Dia.
Las opciones en el campo Hora cambian correspondiendo al dia seleccionado.

CU20
Nombre:  Reservar.
Requerimientos: RF23, RF27.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página Instalación, en la sección reservas.
Curso básico:
El usuario completa todos los campos del formulario con datos válidos.
El usuario presiona el botón Reservar.
La página redirecciona a la página de confirmación.
El usuario recibe un email de confirmación.

CU21
Nombre: Hora ya reservada no disponible.
Requerimientos: RF24.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página Instalación, en la sección reservas.
Curso básico:
El usuario completa todos los campos del formulario con datos válidos.
El usuario presiona el botón Reservar.
El usuario navega de regreso hacia la página de Instalación.
El usuario selecciona el dia que seleccionó anteriormente para su reserva.
El usuario ya no ve disponible el horario que envió para su reserva.

CU22
Nombre: Dia con todos los horarios reservados.
Requerimientos: RF25.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página Instalación, en la sección reservas y todos los horarios de una de las fechas ya se han reservado.
Curso básico:
En el campo Dia, el usuario solo ve una única fecha disponible.

CU23
Nombre: Todos los días con todos los horarios reservados.
Requerimientos: RF26.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario se encuentra en la página Instalación, en la sección reservas. Todos los horarios de ambos días ya han sido reservados.
Curso básico:
El usuario ve un mensaje de “Ya no quedan fechas disponibles”.
El usuario rellena todos los campos del formulario con datos validos.
El usuario presiona el botón Reservar.
El botón se encuentra deshabilitado y la reserva no se ejecuta.

CU24
Nombre: Pantalla de carga.
Requerimientos: RF28.
Prioridad: Esencial.
Actores: Usuario.
Precondiciones: El usuario no ha ingresado a la pagina todavia.
Curso básico:
El usuario ingresa a la página por primera vez.
La pantalla de carga se mantiene activa hasta que todo el contenido de la página termine de cargarse.


