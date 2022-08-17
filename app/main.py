import code
from operator import index
from typing import Optional
from urllib import response
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Player(BaseModel):
    id   : int
    name : str
    Class: str
    #section: str(Optional) = None

cricketTeam = [{'id': 1, 'name': 'Rajiv','Class':'X'},
               {'id': 2, 'name':'Rudra','Class':'XII'},
               {'id': 4, 'name':'Dilip', 'Class':'VI'}]

def getPlayer(id):
    for player in cricketTeam:
        if player['id'] == id:
            return player

def find_player_index(id):
    for i, p in enumerate(cricketTeam):
        if p['id'] == id:
            return i

@app.get("/")
async def greetingMessage():
    return "Hi, Let's Learn API using Python & fastapi framework"

@app.get("/cricketTeam")
async def getCricketTeam():
    return{"Team": cricketTeam}

"""Below two end points are for the same operation
but status code related stubs are differntly coded"""

"""
@app.get("/cricketTeam/{id}")
async def get_Player(id: int, response: Response):
    player = getPlayer(id)
    if not player:
        response.status_code = status.HTTP_404_NOT_FOUND
        return{"message": f"post with id: {id} was not found !"}
    return{"Player Details": player}
"""

@app.get("/cricketTeam/{id}")
async def get_Player(id: int):
    player = getPlayer(id)
    if not player:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail= f"player {id} was not found !")
        '''response.status_code = status.HTTP_404_NOT_FOUND
        return{"message": f"post with id: {id} was not found !"}'''
    return{"Player Details": player}

"""Below two end points are for the same operation
but status code related stubs are differntly coded"""
"""
@app.post("/createPlayer")
async def create_Player(player: Player,response: Response):
    cricketTeam.append(player.dict())
    if player in cricketTeam:
        response.status_code = status.HTTP_201_CREATED
    return{"Updated Cricket Team": cricketTeam}
"""

@app.post("/createPlayer", status_code=status.HTTP_201_CREATED)
async def create_Player(player: Player):
    cricketTeam.append(player.dict())
    return{"Updated Cricket Team": cricketTeam}

@app.put("/updatePlayer/{id}")
async def crickTeam_update_Put(id:int, player: Player):
    index = find_player_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Player with id: {id} does not exist")

    player_dict = player.dict()
    player_dict['id'] = id
    create_Player[index] = player_dict
    return{"data": player_dict}


# @app.patch()
# async def crickTeam_update_Patch(id: int, status_code = status.HTTP_202_ACCEPTED):
#     pass


@app.delete("/player/{id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_Player(id: int):
    index = find_player_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Player with id: {id} does not exist")
    cricketTeam.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
