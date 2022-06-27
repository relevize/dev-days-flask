# Dev Days Flask

This is a dev days project. It's goals are to:
[ ] build a basic flask project
[ ] incorporate marshmallow 
[ ] incorporate sqlschema
[ ] incorporate migrations
[ ] explore and better understand decorators
[ ] explore and better understand flask/python patterns

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