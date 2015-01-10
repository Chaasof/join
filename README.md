Join Portal
===========

## Description
Mozilla Tunisia Join

## Running
pip and virtualenv need to be installed on your machine.

  1-Setting a virtual environment:
   <pre>
     mkdir venv
     virtualenv venv
     source venv/bin/activate
   </pre>
   

  2-Cloning the project
   <pre>
     cd venv
     git clone https://github.com/medfiras/join
   </pre>

 
  3-Installing dependencies:
   <pre>
     cd join
     pip install -r requirements.txt
   </pre>
  
  
  4-Editing the settings file:
  
  4.1-Admin username and email
     
   <pre>
      ADMINS = (
        ('Username', 'admin@example.com'),
      )
   </pre>
  
  4.2-Database settings
  
   <pre>
     DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': 'db_name',                      # Or path to database file if using sqlite3.
          # The following settings are not used with sqlite3:
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
          'PORT': '',                      # Set to empty string for default.
      }
    }
   </pre>
  
  4.3-Email SMTP configuration
    
    Edit "EMAIL_HOST_USER" and "EMAIL_HOST_PASSWORD" with your gmail adress and password
    
   <pre>
      EMAIL_HOST_USER = 'email@gmail.com'
      EMAIL_HOST_PASSWORD = 'password'
   </pre>
