import unittest
from models import Game


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

    def test_perfect_game(self):
        # First Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 10)
        # Second Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 30)
        # Third Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 60)
        # Fourth Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 90)
        # Fifth Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 120)
        # Sixth Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 150)
        # Seventh Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 180)
        # Eighth Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 210)
        # Ninth Frame
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 240)
        # Tenth Frame
        self.game.players[0].roll(10)
        self.game.players[0].roll(10)
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 300)

    def test_all_spares_game(self):
        # First Frame
        self.game.players[0].roll(0)
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 10)
        # Second Frame
        self.game.players[0].roll(1)
        self.game.players[0].roll(9)
        self.assertEqual(self.game.players[0].score, 21)
        # Third Frame
        self.game.players[0].roll(2)
        self.game.players[0].roll(8)
        self.assertEqual(self.game.players[0].score, 33)
        # Fourth Frame
        self.game.players[0].roll(3)
        self.game.players[0].roll(7)
        self.assertEqual(self.game.players[0].score, 46)
        # Fifth Frame
        self.game.players[0].roll(4)
        self.game.players[0].roll(6)
        self.assertEqual(self.game.players[0].score, 60)
        # Sixth Frame
        self.game.players[0].roll(5)
        self.game.players[0].roll(5)
        self.assertEqual(self.game.players[0].score, 75)
        # Seventh Frame
        self.game.players[0].roll(6)
        self.game.players[0].roll(4)
        self.assertEqual(self.game.players[0].score, 91)
        # Eighth Frame
        self.game.players[0].roll(7)
        self.game.players[0].roll(3)
        self.assertEqual(self.game.players[0].score, 108)
        # Ninth Frame
        self.game.players[0].roll(8)
        self.game.players[0].roll(2)
        self.assertEqual(self.game.players[0].score, 126)
        # Tenth Frame
        self.game.players[0].roll(9)
        self.game.players[0].roll(1)
        self.game.players[0].roll(10)
        self.assertEqual(self.game.players[0].score, 155)

    # TODO: Ran out of time
    # def test_multiplayer_game(self):
    #     pass
