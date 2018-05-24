# Bowling App
An API to keep score of multiple bowling games.

## Installing
Install python 3.6  
Install the required packages:
```
pip3 install -r requirements.txt
```

## Running Tests
Run the following command from the BowlingApp directory:
```
python -m unittest discover
```

## Deployment
Run the following commands from the BowlingApp directory:  
Mac:
```
export FLASK_APP=api.py
python -m flask run
```

Windows:
```
set FLASK_APP=api.py
python -m flask run
```

## Operation
Navigate to http://127.0.0.1:5000 to verify that BowlingApp is running.  
Use a tool like curl or postman to make the following requests:

* __GET /games__ returns all current games.
* __POST /games__ will create a game. It requires the following json:
```
{
"game_id": 0,
"players": ["Player1", "Player2"]
}
```
* __GET /games/{game_id}__ will return the specified game.
* __PUT /games/{game_id}__ will add a roll to the player specified with the following json:
```
{
"player": "Player1",
"pins": 10
}
```
* __DELETE /games/{game_id}__ will delete the specified game.
* __DELETE /games__ will delete all games.
