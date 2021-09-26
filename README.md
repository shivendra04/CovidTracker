# CovidTracker
1. Admin module contains Admin related activities like adding the admin detail and updating covid results
2. USER module contains User related activities like adding new user and doing self assessement
3. Zone module contains zone related activited i.e getting Zone details
4. template folder contains templates from respective modules for fornt end 

## Installing:-
1. git clone https://github.com/shivendra04/Recommend.git
2. Change the connection used in the project in the setting.py to your connection or use default Inbuilt Database (SQLite3) provided by Django

## Executing Program:-
1. Create the database in your system and change the connection details in the settings.py or uncomment the default the setting and comment out the current database configuration
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'userrecommend', 'HOST':'localhost', 'POST':'3306', 'USER':'root', 'PASSWORD':'root', } }

2. Open command prompt and navigate to CovidTracker\covidTracker> C:\Users\BizAct-110\Desktop\CovidTracker\CovidTracker>

3. write py manage.py makemigration (it will generate t-SQL for all the required database tables in the server) C:\Users\BizAct-110\Desktop\CovidTracker\CovidTracker> py manage.py makemigrations

4. Type py manage.py migrate (it will run the sql generated in the above step. i.e it will create the tables in the database.) C:\Users\BizAct-110\Desktop\CovidTracker\CovidTracker> py manage.py migrate

5. You can also create superuser to see all the details in the admin panel. C:\Users\BizAct-110\Desktop\CovidTracker\CovidTracker> py manage.py createsuperuser

6. type command py manage.py runserver C:\Users\BizAct-110\Desktop\Recommendation\recommend> py manage.py runserver



Tables created in backened:
![alt text](https://github.com/shivendra04/CovidTracker/blob/master/ReadmeImages/Admin_Table.PNG?raw=true)

