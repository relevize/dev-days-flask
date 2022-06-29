# Dev Days Flask

This is a dev days project! I wanted to build a small project that would get me more familiar with the technology used in the Relevize API. Technologies like:
* Flask
* Marshmallow
* SQLAlchemy
* JWT
* Flask-Migrate

## Project Plan

I want to create an API, `Captains Log`. A journal not just for captains, but for your crew as well. 

| crew_member | log            |
| :---------- | :------------- |
| id          | id             |
| name        | star_date      |
| rank        | log_entry      |
|             | redacted       |
|             | crew_member_id |

Basic user stories:
- [x] CrewMembers should be able to be added
- [ ] Logs should be able to be added (Not edited or deleted, but may be 'redacted' by the captain - for starfleet records)
- [ ] CrewMemebers should not be able to view other CrewMembers logs, unless they are captains

Some Tech Goals:
- [x] Create basic flask app
- [x] Connect flask app to SQLAlchemy
- [x] Use flask-migrate to update the SQLAlchemy database
- [x] Use marshmallow for seialization and validation
- [x] Enforce JWT on some routes
    - [x] Used only on `/logs/all` `GET` requests (that's as far as I got)
- [x] Create auth decorators
    - [x] One to extract requesting crew member data 
    - [x] One to reject crew members from accessing route if they are not captain
- [x] Be able to seed database

## Take Aways

Things I kinda struggle with still
 * `__init__.py` lol - why!?
 * imports are harder than they should be! I gave up on a script and just made a seed endpoint.
 * Can I pass data into the schema? Data that can be referenced by Marshmallow `field.methods`?
    * Ex) removing `log_entry` from being returned 

## Running the project locally

I haven't tested this out, but it should get you in the right direction.
* clone the repository
* `cd` into the repository and enter the poetry shell with `poetry shell` (stay in the shell for the rest of the commands)
* install the projects dependencies with `poetry install`
* use the command `flask db upgrade` to get a db created and to upgrade it to the latest migration
    * I *think* this will create the db for you
* if you want some seed data, you can hit the `/seed` endpoint - *THIS WILL DELETE ALL EXISTING DATA* then add the seed data
* set some flask env variables with the following
    * `export FLASK_APP=captains_log`
    * `export FLASK_ENV=development` (this should be optional)
    * `flask run`

After following those steps you should be able to hit all of the `/crew_member` endpoints with no problem. Some of the `/log` endpoints will require an auth token. You can aquire a token by calling the `/auth/:id` endpoint with a crew_member id. When you are done fiddling around you can exit the poetry shell by using the `exit` command.


---
---

# Notes From Documentation I Read

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

## Marshmallow

Marshmallow will deserialize incoming data and serialize outgoing data based on a schema!

You can deserialize outgoing data using `load`. 
```py
data = crew_member_schema.load(request.get_json()
```

You can serialize incoming data using `dump`.
```py
crew_member = CrewMember.query.filter_by(id=id).first()
dumped_crew_member = crew_member_schema.dump(crew_member)
```

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
* enums

## Json Web Token

I'm kind of winging this - I'm basing it off [this article](https://realpython.com/token-based-authentication-with-flask/).
