
Blog en Django

Este es un proyecto de un blog desarrollado con Django, un framework web de Python, diseñado en Visual Studio Code. El proyecto permite a los usuarios crear, leer, editar y eliminar publicaciones en el blog, además de permitir la autenticación de usuarios.

---

Índice

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Tecnologías](#tecnologías)
- [Configuración del Entorno de Desarrollo](#configuración-del-entorno-de-desarrollo)
- [Base de Datos](#base-de-datos)
- [Autores](#autores)

---

 Instalación

 Requisitos

Para ejecutar este proyecto, necesitarás tener instalado:

- Python 3.x: El lenguaje de programación principal utilizado en el proyecto. Puedes descargarlo desde su [página oficial](https://www.python.org/).
- Pip: El gestor de paquetes de Python (generalmente ya se instala con Python).
- Django: El framework web para Python que se utiliza para desarrollar este blog. Si no lo tienes, se instalará como dependencia.
- Visual Studio Code: Editor de código recomendado, aunque puedes usar cualquier editor que prefieras.

 Pasos de Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/johne55teban/django-blog.git
2.	Accede a la carpeta del proyecto:
3.	cd django-blog
4.	Crea un entorno virtual (opcional pero recomendado):
5.	python -m venv venv
6.	Activa el entorno virtual:
o	En Windows: 
o	venv\Scripts\activate
o	En Mac/Linux: 
o	source venv/bin/activate
7.	Instala las dependencias:
8.	pip install -r requirements.txt
9.	Configura la base de datos: Django utiliza SQLite3 por defecto como sistema de base de datos, por lo que no es necesario realizar ninguna configuración adicional. Solo tienes que ejecutar las migraciones para crear las tablas necesarias:
10.	python manage.py migrate
11.	Crea un superusuario (para acceder al panel de administración):
12.	python manage.py createsuperuser
Sigue las instrucciones para crear un usuario administrador.
________________________________________
Uso
Para ejecutar el servidor de desarrollo de Django:
python manage.py runserver
Accede al blog a través de http://127.0.0.1:8000/ en tu navegador.
Si quieres acceder al panel de administración de Django, usa la URL http://127.0.0.1:8000/admin/ e inicia sesión con el superusuario que creaste.
________________________________________
Características
•	Autenticación de usuarios: Los usuarios pueden registrarse, iniciar sesión y gestionar su perfil.
•	CRUD de publicaciones: Los usuarios pueden crear, editar, eliminar y visualizar publicaciones en el blog.
•	Comentarios: Los usuarios pueden dejar comentarios en las publicaciones.
•	Panel de administración de Django: Gestiona las publicaciones, comentarios y usuarios desde la interfaz administrativa.
•	Paginación: Las publicaciones se muestran de manera paginada en el sitio.
________________________________________
Contribución
Si deseas contribuir al proyecto, sigue estos pasos:
1.	Haz un fork del repositorio.
2.	Crea una nueva rama (git checkout -b feature-nueva).
3.	Realiza tus cambios y haz un commit (git commit -am 'Añadir nueva funcionalidad').
4.	Sube los cambios a tu repositorio (git push origin feature-nueva).
5.	Abre un pull request.
________________________________________
Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
________________________________________
Tecnologías
•	Python 3.x: Lenguaje de programación utilizado para desarrollar este proyecto.
•	Django: Framework web para Python.
•	SQLite3: Base de datos por defecto.
•	HTML/CSS: Para el diseño de las plantillas.
•	Bootstrap (opcional): Si deseas usar un framework CSS para darle estilo a la aplicación.
•	Visual Studio Code: Editor de código recomendado.
________________________________________
Configuración del Entorno de Desarrollo
Si estás utilizando Visual Studio Code como tu editor de código, te recomiendo algunas extensiones y configuraciones que te ayudarán a trabajar de manera más eficiente con este proyecto:
1.	Extensiones recomendadas:
o	Python: Para soporte completo de Python y Django.
o	Django: Extensión que proporciona características específicas de Django.
o	Prettier: Para formatear el código automáticamente.
o	Pylint o Flake8: Para análisis estático del código y mejorar la calidad del mismo.
2.	Configuración de entorno: Si prefieres trabajar con un entorno virtual en Visual Studio Code, sigue estos pasos:
o	Abre la carpeta del proyecto en VS Code.
o	Abre la terminal integrada y activa el entorno virtual: 
o	source venv/bin/activate  # En Mac/Linux
o	venv\Scripts\activate  # En Windows
o	Asegúrate de que el intérprete de Python esté configurado correctamente en VS Code. Ve a View > Command Palette, luego selecciona Python: Select Interpreter y elige el intérprete del entorno virtual.
________________________________________
Base de Datos
Este proyecto usa SQLite3 como base de datos por defecto. SQLite es una base de datos liviana que no requiere configuración adicional, y los datos se almacenan en un archivo local llamado db.sqlite3.
Si necesitas configurar una base de datos diferente (por ejemplo, PostgreSQL o MySQL), puedes modificar el archivo settings.py en la configuración de la base de datos. Sin embargo, para este proyecto no es necesario realizar cambios, ya que se utiliza SQLite3 de manera predeterminada.
________________________________________
Autores
•	Tu Nombre – johne55teban en GitHub
________________________________________
