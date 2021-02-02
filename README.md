# Flask App Boilerplate

A Flask application template with some boilerplate code.


    1. Open in PyCharm > add interpreter
    2. Open terminal > pip install -r requirements.txt
    3. Create .env file at root level OR export BASE_APP=wsgi.py (enable flask run/shell commands)
    4. flask run



## Setting up

##### Create your own repository from this Template

Navigate to the [main project page](https://github.com/GaryMcPolin/flask-base) and click the big, green "Use this template" button at the top right of the page. Give your new repository a name and save it.

##### Clone the repository 

```
$ git clone https://github.com/GaryMcPolin/flask-base.git <repo-name>
$ cd <repo-name>
$ ./git_init.sh
```

##### Initialize a virtual environment

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


##### Add Environment Variables

Create a file called `.env` that contains environment variables. **Very important: do not include the `.env` file in any commits. This should remain private.** You will manually maintain this file locally, and keep it in sync on your host.

Variables declared in file have the following format: `ENVIRONMENT_VARIABLE=value`. You may also wrap values in double quotes like `ENVIRONMENT_VARIABLE="value with spaces"`.

1. In order for Flask to run, there must be a `SECRET_KEY` variable declared. Generating one is simple with Python 3:

   ```
   $ python -c "import secrets; print(secrets.token_hex(16))"
   ```

   This will give you a 32-character string. Copy this string and add it to your `.env`:

   ```
   SECRET_KEY=Generated_Random_String
   ```

Other useful variables include:

| Variable        | Default   | Discussion  |
| --------------- |-------------| -----|
| `ADMIN_EMAIL`   | `flask-base-admin@example.com` | email for your first admin account |
| `ADMIN_PASSWORD`| `password`                     | password for your first admin account |
| `DATABASE_URL`  | `data-dev.sqlite`              | Database URL. Can be Postgres, sqlite, etc. |
| `REDISTOGO_URL` | `http://localhost:6379`        | [Redis To Go](https://redistogo.com) URL or any redis server url |
| `RAYGUN_APIKEY` | `None`                         | API key for [Raygun](https://raygun.com/raygun-providers/python), a crash and performance monitoring service |
| `FLASK_CONFIG`  | `default`                      | can be `development`, `production`, `default`, `heroku`, `unix`, or `testing`. Most of the time you will use `development` or `production`. |


##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Other setup (e.g. creating roles in database)

## License
[MIT License](LICENSE.md)


## todo

Inital DB Setup / Migrations
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

How to Update Schema:
1. Make changes to models.py
2. flask db migrate
3. flask db upgrade
More at: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database


Useful Commands:
- flask run (vs python wsgi.py)
- flask shell (work outside app context - good for testing db stuff)
