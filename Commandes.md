sudo apt install python3-pip
python3 -m pip install django
sudo apt install python3-django
django-admin startproject sigrox  // create project
python3 manage.py runserver       //run server

source ../env_django/bin/activate


python3 manage.py startapp products
python3 manage.py migrate user // after new app,
python3 manage.py makemigrations user
python3 manage.py sqlmigrate user 0002
python3 manage.py shell // commande sql
python3 manage.py makemigrations & python3 manage.py migrate




