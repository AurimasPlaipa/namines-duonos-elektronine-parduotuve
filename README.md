# Flammer-shop
Flammer website!

A fullstack website along with python/flask SQLAlchemy database. 
have a look here - 
the technology i've used here –
•	Python 
•	SQLAlchemy  database
•	the local and test environments use sqlite for the database
•	Javascript(frontend)
•	Bootstrap
•	Flask
•	Fontawesome


what can you do with this site ?
•	can buy a product
•	can visit your cart
•	can delete any of order as your wish
•	there is a dashboard for normal user & for admin
•	an admin can update a product status & can make a admin too
•	a admin also can delete any product he wants
•	can sign in with google & can register a account & can login

Getting started

Installation
Install with pip:
$ pip install -r requirements.txt


Running the app
If you want to test the app locally you will need to follow these steps. Make sure that you have a python environment properly configured. We also recommend you to use a virtual environment.

1.	Clone the application:
    git clone https://github.com/Kristinafffff/Flammer-shop.git
    
2.	Install the requirements:
    cd source/
    
    pip install -r requirements.txt
3.	Create the database:
    python create_db.py
    
4.	Run the developement version of the app:
    python run_dev.py


Flask_data_analysis
This application used data sets stored at mysql. It will pull the requested data and display graph using Matplotlib, Pandas and Seaborn.

Step 1:
Create a folder.
$ mkdir webstore
Create a virtual enviroment.
$pip install virtualenv
$ cd realestate_display_graph
$ virtualenv env
$ source env/bin/activate


Step 2:
Install requirements.txt
$pip install -r requirements.txt


Step 3:
Edit config.py with database credentials.
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/database'


Step 4:
Edit main_app.py with database credentials.
engine=create_engine('mysql+pymysql://username:password@localhost/database')
Step 5:
Run project.
$ python main_app.py





