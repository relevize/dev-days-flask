# Dev Days Flask

This is a dev days project. It's goals are to:
[ ] build a basic flask project
[ ] incorporate marshmallow 
[ ] incorporate sqlschema
[ ] incorporate migrations
[ ] incorporate basic pytests
[ ] create a seed file (optional)
[ ] explore and better understand decorators
[ ] explore and better understand flask/python patterns

## Example App Goals

I want to create an API, `Captains Log`. A journal not just for captains, but for your crew as well. 

Schema:
`CrewMember` 
    - id
    - name
    - rank/role
`Log`
    - id
    - crew_member_id
    - stardate
    - log_entry

Big API goals I may or may not get to:
[ ] CrewMembers should be able to be added
[ ] Logs should be able to be added (Not edited or deleted, but may be 'redacted' by the captain - for starfleet records)
[ ] CrewMemebers should not be able to view other CrewMembers logs, unless they are captains

## Poetry

[Poetry](https://python-poetry.org/docs/) is a dependency and package management tool for Python.

Helpful commands:
- Create a new project with poetry: `poetry new poetry-demo`
- Add poetry to an existing project: `poetry init`
- Add a dependency: `poetry add flask`
- Activating the virtual environment: `poetry shell`
- Deactivate the virtual environement with out exiting the shell: `deactivate`
- Deactivate the virtual environement and exit the shell: `exit`
    - Between `deactivate` & `exit` it's usually better to `exit`
- Install dependencies from the project: `poetry install`
    - This would be used if you just cloned the project, or if you are pulling latest

Do commit your `poetry.lock` file! 

## Flask

You will need to set some environement variables and then run the flask app in your poetry shell:
```py
export FLASK_APP=hello
export FLASK_ENV=development # this allows for extra development features, like the flask debugger!
flask run
```

Accessing the request data requires you to add `request` from the flask module: `from flask import request`.
The request object contains the following data:
- request.path = '/hello'
- request.method = 'POST'
- searching the url params: `searchword = request.args.get('key', '')`
- request.json()

You can get and set cookies!
```py
from flask import request, make_response

# Getting Cookies
@app.route('/')
def index():
    username = request.cookes.get('username')

# Setting Cookies
@app.route('/')
def index():
    resp = make_response()
    resp.set_cookie('username', 'tsuki cat')
    return resp
```

The `__init__.py` file will contain the application factory and tell python that the `captains_log` directory should be treated as a package.

## SQLAlchemy

You can interact with SQLAlchemy through the python shell. To enter the shell, be in the poetry shell, then type `python`.

More to come when I'm actually writing queries...

## Migrate

* Create a migration repository: `flask db init`
* Generate a migration: `flask db migrate -m "Initial migration"`
    * This will auto-magically create a migration based on your models. Results may very.
* Migrate up: `flask db upgrade`
* Migrate down: `flask db downgrade`
* Get the migration you're currently on: `flask db current`

## Python Stuff

* `__repr__`
* `@` - decorators

