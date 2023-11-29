# Drifting Bottles 

### Set Up & Initialization
(1) Download the code repo from github

(2) Create and activate a python virtual environment within the project directory
~~~
python3 -m venv kivy_venv
~~~

Activate: Windows
~~~
kivy_venv\Scripts\activate
~~~

Activate: Mac
~~~
source kivy_venv/bin/activate
~~~
(3) Install kivy within the venv 
~~~
pip install kivy
~~~
(4) Run the main file to activate the app!
python main.py

### Code Structure
~~~
.
├── README.md
├── __pycache__
├── output.txt
├── src
│   ├── assets
│   │   ├── bottle.png
│   │   ├── person.png
│   │   ├── search.png
│   │   ├── setting.png
│   │   └── wifi.png
│   ├── components
│   │   ├── LandingPage
│   │   │   ├── __pycache__
│   │   │   │   └── main_page.cpython-311.pyc
│   │   │   └── main_page.py
│   │   ├── Profile
│   │   │   ├── __pycache__
│   │   │   │   └── profile_page.cpython-311.pyc
│   │   │   └── profile_page.py
│   │   ├── Settings
│   │   │   ├── __pycache__
│   │   │   │   └── settings.cpython-311.pyc
│   │   │   └── settings.py
│   │   └── ThrowBottle
│   │       ├── __pycache__
│   │       │   └── create_bottle.cpython-311.pyc
│   │       └── create_bottle.py
│   └── main.py
├── test.py
~~~
