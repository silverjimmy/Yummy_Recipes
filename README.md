
#Yummy Recipe App
 ----------------

This app is developed under the Andela SLC Challenge for Day2.

It's a simple Flask application that users can use to save there favourite Food Recipes, given that some foods have more than one procedure to prepare a good meal l have provided that option too.

Feel free to check it out

How to run the app
------------------
Make sure python is installed used python3.6 for the app.

-install pip3
  ```
  sudo apt-get install python3-pip
  ```
-Installing flask and setting up app.
   ```
  pip install flask
  ```
-Getting dependencies
  ```
  Run pip install requirements.txt
  ```
Run the app
-----------
Use python 
```
run.py
``` 
in terminal when in file directory to start the application.

Run coverall test
-----------------
-Coveralls shall be installed already as it's a dependance listed under the requirements.txt
  use :
        ```
        nosetests --with-coverage --cover-package=app
        ```
        
       
can also run a nosetest using:
        ```
        nosetests run.py
        ``` 
