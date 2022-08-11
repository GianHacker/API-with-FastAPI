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
