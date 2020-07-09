# trumpy

### Simple graphs of Donald's posts with django and vue js

To run the project follow the steps:
- run ```git clone git@github.com:Ivan1994Petrov/trumpy.git``` from the terminal or just download it
- open the terminal and go to the repo directory 
- create python virtual env ```virtualenv -p python3.6 venv```
- activate the virtual env ```. venv/bin/activate```
- navigate to requirements.txt and run ```pip install -r requirements.txt```
- download nltk stopwords ```python -m nltk.downloader stopwords```
- create migrations ```./manage.py makemigrations``` and ```./manage.py migrate```
- run the command for fetching data ```./manage.py sync_db``` (it may take up to one to two minutes)
- run the server ```./manage.py runserver```
- open new terminal in the same dir
- go to frontend ```cd frontend```
- install npm ```npm install```
- run ```npm run build``` and ```npm run serve```
- open http://localhost:8080/ in browser
- to run the tests ```./manage.py test```

### Further work:

- use Mongo DB
- use ajax for frontend
- try to deploy the project on heroku or aws
