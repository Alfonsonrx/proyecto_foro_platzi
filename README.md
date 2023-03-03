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

## Muestra visual de ejemplo

Index
![image](https://user-images.githubusercontent.com/65643251/222619566-0d67d0c2-b834-4635-bf1c-58d5a71da6a6.png)

Detalle foro
![image](https://user-images.githubusercontent.com/65643251/222619975-db6646cd-0acc-41a0-bb51-e5150bce2422.png)

Detalle foro con comentario
![image](https://user-images.githubusercontent.com/65643251/222620057-f2e5b383-dfa4-4692-87dc-1f29f475d660.png)

Crear foro
![image](https://user-images.githubusercontent.com/65643251/222620223-aa3c844e-d670-4b24-8ded-0d3c4998523b.png)

Perfil propio
![image](https://user-images.githubusercontent.com/65643251/222620329-253c29cc-02df-4605-83b8-6c8fb74435dd.png)

Perfil ajeno
![image](https://user-images.githubusercontent.com/65643251/222620400-b4442eed-9bf3-488d-bd70-57ea4c734f49.png)

Login
![image](https://user-images.githubusercontent.com/65643251/222620510-0972ff9d-24d3-439c-ada4-5970db3338bc.png)

Sign up
![image](https://user-images.githubusercontent.com/65643251/222620601-1d589e22-d25e-4aa7-a568-b962daff48c5.png)
