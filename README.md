# price-monitor
Machine Coding

Steps to Run the project:
<!-- Make sure Python v3+ is installed or use python3 command -->
1. Clone this repo
2. In the "price-monitor" directory ,run the below commands
<!--     Create a virtual environment to isolate our package dependencies locally -->

    python3 -m venv env
    
    source env/bin/activate
    
    pip install -r requirements.txt
    
    cd price
    
    python manage.py migrate
    
    python manage.py loaddata fixture.json #This file is located in the same directory as manage.py
    
    python manage.py runserver 9000 #You can specify which port you want to run it on.
    


How to acccess the rest apis:

Go to the url localhost:9000

It will redirect you to django rest framework browsable screen

You can view the data that you loaded through fixtures

To modify the data login using the option on top right corner and use the brosable interface to update or create new data, you can see the endpoints and format in the same screen.

# Username : admin
# password : Super12#
