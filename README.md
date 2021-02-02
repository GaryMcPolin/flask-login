# Flask Login Boilerplate

A boilerplate application with implementation of a basic flask login




## Setting up

### Clone the repository 

```
$ git clone https://github.com/GaryMcPolin/flask-login.git
$ cd flask-login
```

### Initialize a virtual environment

Windows:
```
$ python3 -m venv venv
$ venv\Scripts\activate.bat
```

Unix/MacOS:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
Learn more in [the documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments).


### Add Environment Variables

Create a file called `.env` that contains environment variables. **Very important: do not include the `.env` file in any commits. This should remain private.** You will manually maintain this file locally, and keep it in sync on your host.

Variables declared in file have the following format: `ENVIRONMENT_VARIABLE=value`. You may also wrap values in double quotes like `ENVIRONMENT_VARIABLE="value with spaces"`.

1. Tell flask where to find your application by adding `FLASK_APP` to the environment variables
   ```
   $ echo "FLASK_APP=wsgi.py" >> .env
   ```
2. In order for Flask to run, there must be a `SECRET_KEY` variable declared. Generating one is simple with Python 3:

   ```
   $ python -c "import secrets; print(secrets.token_hex(16))"
   ```

   This will give you a 32-character string. Copy this string and add it to your `.env`:

   ```
   SECRET_KEY=Generated_Random_String
   ```
    Other useful variables include:
    
    | Variable        | Value   | Discussion  |
    | --------------- |-------------| -----|
    | `DATABASE_URL`  | `data-dev.sqlite`              | Database URL. Can be Postgres, sqlite, etc. |


### Install the dependencies
Do this after activating your virtual environment
```shell script
$ (venv) pip install -r requirements.txt
```

### IDE setup
    1. Open project in PyCharm > add interpreter > python 3.8 or above

### Database setup
Follow Miguel Grinberg's [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
```shell script
$ (venv) flask db init
$ (venv) flask db migrate
$ (venv) flask db upgrade
```

## License
[MIT License](LICENSE.md)


## Other
Useful Links:
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
Useful Commands:
- flask run (vs python wsgi.py)
- flask shell (work outside app context)
