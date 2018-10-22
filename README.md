# Quickr clone in django

## Setting up environment
- Install virtual environment
```
pip install virtualenv
```
- Create a virtual environment named env using the following command
```
virtualenv env
```
- Run the following command to install the dependencies
```
pip install -r requirements.txt
```
- Create .env file with 
    - SECRET_KEY
    - DEBUG
    - ALLOWED_HOSTS (separated by comma)

## Running

```
python manage.py runserver
```
