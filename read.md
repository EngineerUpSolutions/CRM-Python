1 clone the repository
2 activate the virtual environment for python 
 route: /home/daniels/Documents/PYTHON-CRM/CRM-Python/dcrm

 source virt/Scripts/activate
 deactivate

2.2 check plugins and dependencies installing pending 

3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver


4 Username, and Password

python3 manage.py createsuperuser


5 install mysql and set up


pip install pytest
pytest