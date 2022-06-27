# Dev Days Flask

This is a dev days project. It's goals are to:
[ ] build a basic flask project
[ ] incorporate marshmallow 
[ ] incorporate sqlschema
[ ] incorporate migrations
[ ] explore and better understand decorators
[ ] explore and better understand flask/python patterns

## Example App Goals

I want to create an API, `Captains Log`. A journal not just for captains, but for your crew as well. 

Schema:
`CrewMember` 
    - id
    - username
    - rank/role
`Log`
    - id
    - crew_member_id
    - stardate
    - log_entry

Big API goals I may or may not get to:
[ ] CrewMembers should be able to be added
[ ] Logs should be able to be added (Not edited or deleted, but may be 'redacted' - for starfleet records)
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
flask run
```