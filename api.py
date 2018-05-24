from flask import Flask, jsonify, request
from models import Game, GameSchema, PlayerSchema

app = Flask(__name__)

games = {}
game_schema = GameSchema()
games_schema = GameSchema(many=True)
player_schema = PlayerSchema()


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'BowlingApp is running.'})


@app.route('/games', methods=['GET'])
def get_all_games():
    game_list = games.values()
    result = games_schema.dump(game_list)
    return jsonify({'games': result.data})


@app.route('/games/<int:game_id>')
def get_game(game_id):
    try:
        game = games[game_id]
    except KeyError:
        return jsonify({'message': 'Game could not be found.'}), 400

    game_result = game_schema.dump(game)
    return jsonify({'game': game_result.data})


@app.route('/games', methods=['POST'])
def create_game():
    json_data = request.get_json()

    # Validate Input
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400

    if 'game_id' in json_data and 'players' in json_data:
        game_id = json_data['game_id']
        players = json_data['players']

        if game_id in games:
            return jsonify({'message': 'Game with game id already exists.'}, 400)

        game = Game(game_id, players)
        games[game_id] = game
        result = game_schema.dump(game)
        return jsonify({'message': 'Created new game.', 'game': result})
    else:
        return jsonify({'message': 'A game id and a list of player names must be provided to create a game.'}), 400


@app.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    json_data = request.get_json()

    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400

    try:
        game = games[game_id]
    except KeyError:
        return jsonify({'message': 'Game could not be found.'}), 400

    if 'pins' in json_data and 'player' in json_data:
        player_name = json_data['player']
        pins = json_data['pins']
        player_index = None
        for index, player in enumerate(game.players):
            if player_name == player.name:
                player_index = index
        if player_index is not None:
            player = game.players[player_index]
            player.roll(pins)
            result = player_schema.dump(player)
            return jsonify({'message': 'Player rolled.', 'player': result})
        else:
            return jsonify({'message': 'Player name could not be found in game.'}), 400
    else:
        return jsonify({'message': 'A player name and the pins rolled must be provided.'}), 400


@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    try:
        del games[game_id]
    except KeyError:
        return jsonify({'message': 'Game could not be found.'}), 400

    return jsonify({'message': 'Game deleted.'}), 200


@app.route('/games', methods=['DELETE'])
def delete_all_games():
    games.clear()
    return jsonify({'message': 'All games deleted.'}), 200


if __name__ == '__main__':
    app.run(debug=True)
