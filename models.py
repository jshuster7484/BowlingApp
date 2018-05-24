from marshmallow import Schema, fields

MAX_FRAMES = 10
MAX_PINS = 10
LAST_FRAME = MAX_FRAMES - 1


class Game:
    def __init__(self, game_id, names):
        new_players = []
        # Note: A dictionary would be better here, but ran out of time on how to implement the schema in marshmallow.
        for name in names:
            new_players.append(Player(name))

        self.id = game_id
        self.players = new_players


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.frame_index = 0
        self.frames = [[], [], [], [], [], [], [], [], [], []]
        self.completed = False

    def is_strike(self, frame):
        return frame == [MAX_PINS]

    def is_spare(self, frame):
        return sum(frame) == MAX_PINS

    def roll(self, pins):
        """Append the pins rolled to the current frame and increment the frame if necessary.
         If the last frame is reached end the player's game."""
        if not self.completed:
            current_frame = self.frames[self.frame_index]
            current_frame.append(pins)

            if self.frame_index != LAST_FRAME:
                if self.is_strike(current_frame) or len(current_frame) == 2:
                    self.frame_index += 1
            else:
                if sum(current_frame) < MAX_PINS and len(current_frame) == 2 or len(current_frame) == 3:
                    self.frame_index += 1

            # End the player's game
            if self.frame_index > LAST_FRAME:
                self.completed = True

            self.update_score()

    def update_score(self):
        """Update the player's score based on completed frames."""
        # Note: This algorithm could be made more efficient, but I preferred to make it more easily readable.
        new_score = 0
        for index, frame in enumerate(self.frames):
            if index != LAST_FRAME and self.is_strike(frame):
                new_score += MAX_PINS + self.get_next_two_rolls(index)
            elif index != LAST_FRAME and self.is_spare(frame):
                new_score += MAX_PINS + self.get_next_roll(index)
            else:
                new_score += sum(frame)

        self.score = new_score

    def get_next_roll(self, frame_index):
        """Return the value of the next roll. If it doesn't exist return 0."""
        if len(self.frames) > frame_index + 1 and len(self.frames[frame_index + 1]) >= 1:
            return self.frames[frame_index + 1][0]
        else:
            return 0

    def get_next_two_rolls(self, frame_index):
        """Return the value of the next two rolls. Only return the rolls that exist."""
        next_roll = self.get_next_roll(frame_index)
        if len(self.frames) > frame_index + 1 and len(self.frames[frame_index + 1]) >= 2:
            return next_roll + self.frames[frame_index + 1][1]
        elif len(self.frames) > frame_index + 2 and len(self.frames[frame_index + 2]) >= 1:
            return next_roll + self.frames[frame_index + 2][0]
        else:
            return next_roll


class PlayerSchema(Schema):
    name = fields.Str()
    score = fields.Integer()
    current_frame = fields.List(fields.Str())
    frames = fields.List(fields.Str())


class GameSchema(Schema):
    id = fields.Str()
    players = fields.Nested(PlayerSchema, many=True)


