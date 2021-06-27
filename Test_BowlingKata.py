import unittest
from BowlingKata import Game

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.g = Game()
    
    def rollMany(self, rolls, pinsPerRoll):
        for i in range(rolls):
            self.g.roll(pinsPerRoll)

    def rollStrike(self):
        self.g.roll(10)
    
    def rollSpare(self):
        self.g.roll(9)
        self.g.roll(1)

    def testGutterGame(self):
        self.rollMany(20, 0)
        self.assertEqual(0, self.g.score(), "Score is not 0")

    def testAllOnes(self):
        self.rollMany(20,1)
        self.assertEqual(20, self.g.score(), "Score is not 20")

    def testOneSpare(self):
        self.rollSpare()
        self.g.roll(3)
        self.rollMany(17,0)
        self.assertEqual(
            16,
            self.g.score(), 
            "Spare calculated incorrectly, should be 16"
            )

    def testOneStrike(self):
        self.rollStrike()
        self.g.roll(3)
        self.g.roll(4)
        self.rollMany(16,0)
        self.assertEqual(
            24,
            self.g.score(), 
            "Strike calculated incorrectly, should be 24"
            )

    def testPerfectGame(self):
        self.rollMany(12,10)
        self.assertEqual(
            300,
            self.g.score(), 
            "perfect game calculated incorrectly, should be 300"
            )

if __name__ == '__main__':
    unittest.main()