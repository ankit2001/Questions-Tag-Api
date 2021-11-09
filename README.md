# Media Scanner
## Environment setup:
<p>git clone https://github.com/punditji-live/app.git <br>
cd app <br>
sudo apt install python3 python3-pip or brew install python3 python3-pip<br> 
python3 -m venv ~/env <br>
source ~/env/bin/activate <br>
sudo -H pip install -r requirements.txt</p>

## Building using docker:
<p>git clone https://github.com/punditji-live/app.git <br>
cd app <br>
sudo docker-compose build<br>
sudo docker-compose run MediaScanner sh -c "python3 manage.py makemigrations"<br>
sudo docker-compose run MediaScanner sh -c "python3 manage.py migrate"<br>
sudo docker-compose run MediaScanner sh -c "python3 manage.py collectstatic"<br>
sudo docker-compose run MediaScanner sh -c "python3 runserver 0.0.0.0:8000"
</p>

## Migrations for models
<p>python manage.py makemigrations api <br>
python manage.py migrate</p>

## Create superuser to get admin access
<p>python manage.py createsuperuser <br>
(Enter required fields) </p>

## Run the server
<p>python manage.py runserver <br>
Get access to 127.0.0.1:8000 on web browser <br>
127.0.0.1:8000/admin for Django admin <br>
127.0.0.1:8000/api for using APIs</p>

# Documentation to use the APIs
## Developer Profile Register Api
<p>Post request to following url: <br>
<b>127.0.0.1:8000/api/developer-profile</b> <br>
Form will require Email, Name, Organisation and Password.</p>

## Developer LoginApi (accesing token)
<p>Post request to following url: <br>
<b>127.0.0.1:8000/api/developer-accessToken</b> <br>
Form will require Username and Password. <br>
Post request on this will generate Access token which can be used by developer. <br>
Use mod header extension in browser and put token there to give excess to token.</p>

## TextReport Api
<p>Post request to following url: <br>
<b>127.0.0.1:8000/api/text-report</b> <br>
Form will require Text Field.<br>
It will give a json response of Text report in key "report".</p>


