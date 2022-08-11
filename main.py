from fastapi import FastAPI

app = FastAPI()

cricketTeam = [{'id': 1, 'name': 'Rajiv','Class':'X'},
               {'id': 2, 'name':'Rudra','Class':'XII'},
               {'id': 4, 'name':'Dilip', 'Class':'VI'}]

def getPlayer(id):
    for player in cricketTeam:
        if player['id'] == id:
            return player

@app.get("/")
async def greetingMessage():
    return "Hi, Let's Learn API using Python & fastapi framework"

@app.get("/cricketTeam")
async def getCricketTeam():
    return{"Team": cricketTeam}

@app.get("/cricketTeam/{id}")
async def get_Player(id: int):
    player = getPlayer(id)
    return{"Player Details": player}

