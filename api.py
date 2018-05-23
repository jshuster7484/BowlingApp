from flask import Flask, jsonify, abort, request
from marshmallow import ValidationError
from models import Game, GameSchema, Player, PlayerSchema

app = Flask(__name__)

games = [
    Game(0, ['John'])
]

game_schema = GameSchema()
games_schema = GameSchema(many=True)


@app.route('/games', methods=['GET'])
def get_all_games():
    result = games_schema.dump(games)
    return jsonify({'games': result.data})


@app.route("/games/<int:game_id>")
def get_game(game_id):
    try:
        game = games[game_id]
    except IndexError:
        return jsonify({"message": "Game could not be found."}), 400
    game_result = game_schema.dump(game)
    return jsonify({'game': game_result.data})


@app.route('/games', methods=['POST'])
def create_game():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # try:
    #     data = game_schema.load(json_data)
    #     print(data)
    # except ValidationError as err:
    #     return jsonify(err.messages), 422

    # TODO: Validate input

    game = Game(len(games), json_data['players'])
    games.append(game)
    result = game_schema.dump(game)
    return jsonify({"message": "Created new game.", "game": result})


@app.route('/games/<game_id>', methods=['PUT'])
def update_game():
    return ''


@app.route('/games/<game_id>', methods=['DELETE'])
def delete_game():
    return ''


@app.route('/games', methods=['DELETE'])
def delete_all_games():
    return ''


if __name__ == '__main__':
    app.run(debug=True)
