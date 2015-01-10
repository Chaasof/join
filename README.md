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
