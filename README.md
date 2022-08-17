# API design & development using FastAPI 
API development using python3 & FastAPI framework

## Initial steps
Post creating a workspace and virtual environment, updated pip & installed fastapi
Created .gitignore file to ignore python & venv
Created License file with MIT License

## Beginning of API development
imported FastAPI class from fastapi module
Instantiated an object "app" of type FastAPI
Added a decorator @app to initiate a get end point of type root
* @app.get("/")
An async method greetingMessage is defined to return a message

## Local data  in list
* Created a list of cricket players as dictonaries which are wrapped in cricketTeam list
* Created an end point to fetch & display the team
* Created an end point to fetch & display a player details with the help of player id
* Created an end point to create player record & append to the list
* Created an end point to update a player details of user choice with put method
* created an end point to delete a player record from the list

## Altered the file structure & created a package
* Moved the file main.py into the package titled app & also create __init__.py file within the package

