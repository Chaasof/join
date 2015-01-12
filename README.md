Join Portal
===========

## Description
Mozilla Tunisia Join

## Running
pip and virtualenv need to be installed on your machine.

**1. Setting a virtual environment:**
  ```shell
    mkdir venv
    virtualenv venv
    source venv/bin/activate
  ```
   
**2. Cloning the project**
  ```shell
    cd venv
    git clone https://github.com/medfiras/join
  ```
  
 **3. Installing dependencies:**
  ```shell
    cd join
    pip install -r requirements.txt
  ```
  
**4. Editing the settings file:**
  
  * Admin username and email
     
    ```
      ADMINS = (
        ('Username', 'admin@example.com'),
      )
    ```
  
  + Database settings
  
    ```
      DATABASES = {
        'default': 
        {
          'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': 'db_name',                      # Or path to database file if using sqlite3.
          # The following settings are not used with sqlite3:
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': '',         # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
          'PORT': '',         # Set to empty string for default.
        }
      }
    ```
  
  + Email SMTP configuration
    
    Edit "EMAIL_HOST_USER" and "EMAIL_HOST_PASSWORD" with your gmail adress and password
    
    ```
      EMAIL_HOST_USER = 'email@gmail.com'
      EMAIL_HOST_PASSWORD = 'password'
    ```
