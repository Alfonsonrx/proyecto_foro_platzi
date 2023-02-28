# Proyecto Foro Platzi
Este proyecto es una pagina web de foros basico, ha sido realizado para un curso de Platzi, 
tambien probar mis conocimientos y habilidades en Django, que tengo ideado utilizar en futuros proyectos

## Ejecutar localmente  

Clonar repositorio

~~~bash  
git clone https://github.com/Alfonsonrx/proyecto_foro_platzi.git
~~~

Ir al directorio principal

~~~bash  
cd proyecto_foro_platzi
~~~

Crear enviroment e instalarle librerias

~~~bash  
py -m venv venv

.\venv\Scripts\activate

pip install -r .\requirements.txt
~~~

Dirigirse al directorio del proyecto y generar las Migrations 

~~~bash
cd foro_platzi

py manage.py makemigrations
~~~

Si por alguna razon no se generan los modelos, recurrir a los siguientes comandos

~~~bash
py manage.py makemigrations foros
py manage.py makemigrations forum_profile
~~~

Migrar los modelos

~~~bash
py manage.py migrate
~~~

Crear usuario admin para ingresar a vista de administradores

~~~bash
py manage.py createsuperuser
~~~

Iniciar el servidor

~~~bash  
py manage.py runserver
~~~