# flask app -csc308

## Flask backend RESTful api for REACT app

Implements simple id, name and job database using python dictionaries

Current implemented responses include:

- GET (for all users and user based on id)
- POST (new user)
- DELETE (deletes user based on id)

## To run code

Ensure that python is installed and includes these libraries:

```{txt}
flask
flask-cors
```

To start the flask server (on macos/linux)

```{sh}
export FLASK_APP=flask_app.py
export FLASK_ENV=development
flask run 
```
