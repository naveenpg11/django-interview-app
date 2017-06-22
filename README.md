# Django-Chat

Chat Application Using Django Channels

INSTALLATIONS:-

Installing with get-pip.py:
To install pip, securely download get-pip.py.

Then run the following:

python get-pip.py

virtualenv:

virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

Install virtualenv via pip:

$ pip install virtualenv

Create a virtual environment for a project:

$ cd my_project_folder

$ virtualenv my_project

$ cd my_project

$ .\Scripts\activate

Download the Git Project and Navigate into the Project in you Virtual Environment

pip install -r requirements.txt

Customize the Database Setting in Settings.py 

Finally, run:

python manage.py migrate

Make yourself a superuser account:

python manage.py createsuperuser

python manage.py runserver

Then, log into http://127.0.0.1:8000/admin/ and make a couple of Room objects. 

Create User accounts in http://127.0.0.1:8000/user/register and Login in to the site.

open a second window in another browser or in "incognito" mode - you'll be logging in to the same site with two user accounts. Navigate to http://127.0.0.1:8000/chat in both browsers and open the same chatroom.

Now, you can type messages and see them appear on both screens at once. You can join other rooms and try there, and see how you receive messages from all rooms you've currently joined. You can even see users who are online.
