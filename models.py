from marshmallow import Schema, fields


class Game:
    def __init__(self, game_id, names):
        new_players = []
        for name in names:
            new_players.append(Player(name))

        self.id = game_id
        self.players = new_players


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

        self.roll_number = 0
        self.rolls = [0]*21  # 21 rolls maximum in a game

        self.frame_index = 0
        self.frames = [[], [], [], [], [], [], [], [], [], []]
        self.completed = False

    def is_strike(self, frame):
        return frame == [10]

    def is_two_strikes(self, frame):
        return frame == [10, 10]

    def is_spare(self, frame):
        return sum(frame) == 10

    def roll(self, pins):
        """doc string"""
        #self.rolls[self.roll_number] = pins
        #self.roll_number += 1
        #self.update_score()

        self.frames[self.frame_index].append(pins)

        if self. frame_index != 9:
            if self.is_strike(self.frames[self.frame_index]) or len(self.frames[self.frame_index]) == 2:
                self.frame_index += 1
        else:
            if sum(self.frames[self.frame_index]) < 10 and len(self.frames[self.frame_index]) == 2 or len(self.frames[self.frame_index]) == 3:
                self.frame_index += 1

        # End Game
        if self.frame_index >= 9:
            self.completed = True

        self.new_score()

    def new_score(self):
        new_score = 0

        rolls = []
        for frame in self.frames:
            for roll in frame:
                rolls.append(roll)

        for index, frame in enumerate(self.frames):
            if index != 9 and self.is_strike(frame):
                new_score += 10 + self.get_next_two_rolls(index)
            elif index != 9 and self.is_spare(frame):
                new_score += 10 + self.get_next_roll(index)
            else:
                new_score += sum(frame)

        self.score = new_score

    def get_next_roll(self, frame_index):
        if len(self.frames) > frame_index + 1 and len(self.frames[frame_index + 1]) >= 1:
            return self.frames[frame_index + 1][0]
        else:
            return 0

    def get_next_two_rolls(self, frame_index):
        next_roll = self.get_next_roll(frame_index)
        if len(self.frames) > frame_index + 1 and len(self.frames[frame_index + 1]) >= 2:
            return next_roll + self.frames[frame_index + 1][1]
        elif len(self.frames) > frame_index + 2 and len(self.frames[frame_index + 2]) >= 1:
            return next_roll + self.frames[frame_index + 2][0]
        else:
            return next_roll

    def update_score(self):
        new_score = 0
        roll_index = 0
        turn_index = 0

        while turn_index < 10:
            if self.rolls[roll_index] == 10:
                new_score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
                new_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:
                new_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
            turn_index += 1

        self.score = new_score


class PlayerSchema(Schema):
    name = fields.Str()
    score = fields.Integer()
    current_frame = fields.List(fields.Str())
    frames = fields.List(fields.Str())


class GameSchema(Schema):
    id = fields.Str()
    players = fields.Nested(PlayerSchema, many=True)


