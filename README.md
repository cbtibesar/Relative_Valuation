# Relative_Valuation
The purpose of the application is to provide the user an easy way to create what are called relative valuations, which are essentially comparisons of 
different stocks and their financials. This makes it easy to determine which stocks incertain industries may be performing better than their competitors. 

This application was built as a personal project to practice web development. The backend is built using Django Rest Framework with Python, and the
frontend is React.js. Json Web Tokens (JWT) are used for authenitcation. The frontend also used the Material UI library, providing many pre-built, clean-looking components to use.

## Dependencies
The dependencies in the backend are mangaged by a conda virtual environment. I recommend using a python virtual environment to run the application. The dependencies required can be installed using ```pip```. They include:  
```django```  
```django-cors-headers```  
```djangorestframework```  
```djangorestframework-simplejwt```   
```yfinance```  

```yfinance``` will install the other necessary packages such as ```numpy``` and ```pandas```.

## Run on local machine

In order to run the application on your local machine, of course start by cloning the repository. From a command line within the main application folder, you will need to start by creating the initial migrations and sqlite file for the database. To do this, run:  
```python manage.py makemigrations```  
```python manage.py makemigrations relative_table_api```  
```python manage.py makemigrations users```  

Followed by:  
```python manage.py migrate```  
```python manage.py migrate relative_table_api```  
```python manage.py migrate users```  


You should see migration folders created within the respective folders. Then you can run: ```python manage.py runserver```, 
which will run the Django application at port 8000. 


To run the frontend, navigate to ```Relative_Valuation_Frontend``` folder, and run ```npm install``` to install the required npm packages, including the Material UI packages. Then you can run ```npm start```, which will host the fontend at port 3000. 

## Management
The application includes an administrative type user, called a superuser. To create a superuser, you can run ```python manage.py createsuperuser``` and
follow the prompts. To manage the users and datasets of the application, you can navigate to ```http://localhost:8000/admin/``` while the server is running, and login as the superuser.

