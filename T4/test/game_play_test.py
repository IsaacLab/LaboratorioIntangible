import unittest

from pydilemma.game_play import *
from pydilemma.strategy import TitForTwoTats, Naive, Alternate, TitForTat

class Test(unittest.TestCase):


    def testRuleResolver(self):
        matrix = BOARDS.get('PrisonerMatrix')
        self.assertEqual(Game.resolve(matrix, (0, 1)), [(3, 1), (0, 0)])
        self.assertEqual(Game.resolve(matrix, (1, 1)), [(2, 1), (2, 1)])
        self.assertEqual(Game.resolve(matrix, (1, 0)), [(0, 0), (3, 1)])
        self.assertEqual(Game.resolve(matrix, (0, 0)), [(-2, 0), (-2, 0)])
        

    def testGame(self):
        alice = Player('Alice', Naive())
        bob = Player('Bob', TitForTwoTats())
        game = Game([alice, bob], 'PrisonerMatrix', 20)        
        game.play()
        self.assertEqual(alice.score, 0)
        self.assertEqual(bob.score, 3)
        game.play()
        self.assertEqual(alice.score, -2)
        self.assertEqual(bob.score, 1)
        game.play()
        self.assertEqual(alice.score, -2)
        self.assertEqual(bob.score, 4)
        game.play()
        self.assertEqual(alice.score, -4)
        self.assertEqual(bob.score, 2)


    def testGameIterative(self):
        alice = Player('Alice', Alternate())
        bob = Player('Bob', TitForTat())
        
        game = Game([alice, bob], 'ChickenMatrix', 11)        
        game.start()
        self.assertEqual(alice.score, 1)
        self.assertEqual(bob.score, 1)
        
        game2 = Game([alice, bob], 'ChickenMatrix', 101)        
        game2.start()
        self.assertEqual(alice.score, 4)
        self.assertEqual(bob.score, -2)
        


if __name__ == "__main__":
    unittest.main()