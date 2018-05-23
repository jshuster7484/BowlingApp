import unittest
from models import Game, Player


class TestBowlingApp(unittest.TestCase):

    def setUp(self):
        self.game = Game(0, ['TestPlayer'])

    def test_game_creation(self):
        self.assertEqual(len(self.game.players), 1)
        self.assertEqual(self.game.players[0].name, 'TestPlayer')
        self.assertEqual(self.game.players[0].score, 0)

    def test_zero_game(self):
        # Assert game score starts at zero
        self.assertEqual(self.game.players[0].score, 0)
        # Throw 20 gutter balls
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        self.game.players[0].roll(0)
        self.assertEqual(self.game.players[0].score, 0)
        print(self.game.players[0].frames)
        # Twenty first gutter ball should return error
        #self.game.players[0].roll(0)
        #self.assertEqual(self.game.players[0].score, 0)

    def test_perfect_game(self):
        # First Frame
        self.game.players[0].roll(10)
        self.assertEqual(10, self.game.players[0].score)
        # Second Frame
        self.game.players[0].roll(10)
        self.assertEqual(30, self.game.players[0].score)
        # Third Frame
        self.game.players[0].roll(10)
        self.assertEqual(60, self.game.players[0].score)
        # Fourth Frame
        self.game.players[0].roll(10)
        self.assertEqual(90, self.game.players[0].score)
        # Fifth Frame
        self.game.players[0].roll(10)
        self.assertEqual(120, self.game.players[0].score)
        # Sixth Frame
        self.game.players[0].roll(10)
        self.assertEqual(150, self.game.players[0].score)
        # Seventh Frame
        self.game.players[0].roll(10)
        self.assertEqual(180, self.game.players[0].score)
        # Eighth Frame
        self.game.players[0].roll(10)
        self.assertEqual(210, self.game.players[0].score)
        # Ninth Frame
        self.game.players[0].roll(10)
        self.assertEqual(240, self.game.players[0].score)
        # Tenth Frame
        self.game.players[0].roll(10)
        self.game.players[0].roll(10)
        self.game.players[0].roll(10)
        self.assertEqual(300, self.game.players[0].score)
        print(self.game.players[0].frames)


    def test_all_spares_game(self):
        # First Frame
        self.game.players[0].roll(0)
        self.game.players[0].roll(10)
        self.assertEqual(10, self.game.players[0].score)
        # Second Frame
        self.game.players[0].roll(1)
        self.game.players[0].roll(9)
        self.assertEqual(21, self.game.players[0].score)
        # Third Frame
        self.game.players[0].roll(2)
        self.game.players[0].roll(8)
        self.assertEqual(33, self.game.players[0].score)
        # Fourth Frame
        self.game.players[0].roll(3)
        self.game.players[0].roll(7)
        self.assertEqual(46, self.game.players[0].score)
        # Fifth Frame
        self.game.players[0].roll(4)
        self.game.players[0].roll(6)
        self.assertEqual(60, self.game.players[0].score)
        # Sixth Frame
        self.game.players[0].roll(5)
        self.game.players[0].roll(5)
        self.assertEqual(75, self.game.players[0].score)
        # Seventh Frame
        self.game.players[0].roll(6)
        self.game.players[0].roll(4)
        self.assertEqual(91, self.game.players[0].score)
        # Eighth Frame
        self.game.players[0].roll(7)
        self.game.players[0].roll(3)
        self.assertEqual(108, self.game.players[0].score)
        # Ninth Frame
        self.game.players[0].roll(8)
        self.game.players[0].roll(2)
        self.assertEqual(126, self.game.players[0].score)
        # Tenth Frame
        self.game.players[0].roll(9)
        self.game.players[0].roll(1)
        self.game.players[0].roll(10)
        self.assertEqual(155, self.game.players[0].score)
        print(self.game.players[0].frames)

    def test_multiplayer_game(self):
        pass  # TODO, ran out of time
