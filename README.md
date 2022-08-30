# Club Atletico José Marmol

La aplicación Club_app esta destinada a la administración de un club. En la misma es posible realizar las siguientes acciones: 
-Registrar los datos personales de los alumnos y su actividad en el club.
-Registro de profesores y consulta de profesores indicando una actividad.
-Registro de actividades y visualización de las que hayan sido registradas hasta el momento de la consulta.
-Creación de Noticias que seran de suma relevancia para los empleados del club.
-Envio de mail con consultas para los integrantes del staff del club.

Los integrantes del grupo somos:

Diego Pistolesi. Se encargó de la idea de la app, creación de los modelos principales, funcionamiento general de la página y la cracion de la app que permite enviar mails.

Germán Rodas. Se encargó del apartado visual, utilizando CSS, creación de la app que controla el apartado de "Noticias", con la integración de ckeditor, puesta a punta final de programación final y depuración del código.


Casos de prueba:

1- Hay un inconveniente a tener en cuenta con respecto al avatar. Por como está implementado, solo se ve desde la página de Inicio. 
Las prubas con:
- {{avatar.imagen.url}}
- {{usuario.avatar.imagen.url}}
- {{imagen.url}}
- {{avatar.url}}
No funcionan. La única forma en la que actualmente funciona es poniendo {{url}},  tomando como llegada del contexto la página de inicio.
Falta más investigación para poder recerar eso en padre.html y que quede reflejado en las demás templates.

2- Para poder enviar mails, actualmente gmail no permite la desactivacion de seguridad para aplicaciones menos seguras. La forma de conectarse resultó en tener que genrar una "contraseña de aplicaciones" especifica desde el gmail y aplicarlo en el archivo settings.py para poder enviar mail correctamente.

3- Saltaba un error al querer cargar imagenes en la parte de cargar profesores de la aplicación sin tomar la imágen. La resolución fue al aplicarle el parseo"enctype="multipart/form-data"". Si no se aplica este método, inexplicablemente se queda trabajo y no deja subir datos ni avisar que inconveniente está dando.

4- Para que, al aplicar el ckeditor a el formulario de carga de noticias, no muestre los caracteres de bold, italic y demás adiciones en el código, hubo que aplicarle un código especial a la visualicación, utilicando un código especial de django. El mismo es{{nombre.cuerpo | safe}}. Esto permite decirle a django que el texto es seguro y permite la visualización de las modificaciones, traduciendo las tabulaciones especiales de html.
