# Secret Notes (Training Project)

###### What is it?

This web application allows the user to create their own encrypted notes and categorize them. If necessary, the user can decrypt them, for this he needs to log in and enter the previously created password in the field.

###### Used modules and libraries

The project was created in the Integrated development environment - IDE PyCharm (JetBrains).
Required modules to run the project (see requirements.txt):

- asgiref==3.3.1
- Django==3.1.4
- Pillow==8.0.1
- psycopg2-binary==2.8.6
- pycryptodomex==3.9.9
- pytz==2020.4
- sqlparse==0.4.1

###### Application launch

Here we will describe the launch of the application using the example of the PyCharm IDE.

1. It is necessary to create a working directory for the subsequent cloning of the project (create a folder, then place our project there).

2. Clone the project from GitHub to your created folder.

   ```apl
   git clone https://github.com/serg-lubeshko/HW.git
   ```

   If you have difficulty cloning, you can go to https://github.com/serg-lubeshko/HW.git and download the archive

   ![image-20201214202829379](pictures%20for%20readme/1.gif)

3. When downloading using the Download Zip method, the file must be unzipped and placed in the working directory.

4. Launch IDE PyCharm. Download our project

   ```apl
   File > open> [Our project]
   ```

5. Pycharm, if correctly installed earlier, creates the virtual environment itself and loads the necessary modules from the requirements.txt file If this did not happen, then you need to create:

   - virtual environment (venv). (see instructions. https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

   - install modules manually from requirements.txt file, or use command in Pycharm terminal:

     ```apl
     pip install -r requirements.txt
     ```

6. According to the terms of reference, this project uses the PostgreSQL DBMS (link https://www.postgresql.org/). After installing it, you need to create a database in PostgreSQL using PGadmin and configure settings in settings.py of our project.

![2](pictures%20for%20readme/2.png)

Then in the PyCharm Termenal enter the command:

```apl
python manage.py  migrate
```

7. Create administrator:

   ```apl
   python manage.py  createsuperuser
   ```

8. Now we need to take a look at the project. Remember to start the web server with the python manage.py runserver command. Go to the browser and type the address http://127.0.0.1:8000:

   ```apl
   python manage.py runserver
   ```

9. Our project is ready to go!

![3](pictures%20for%20readme/4.gif)