#!/usr/bin/python3
import unittest
import badminton

class Test(unittest.TestCase):
    
    def setUp(self):
        self.b=badminton.badminton('Katya','Jaime')

    def test_addPoint(self):
        self.b.addPoint(0)
        self.assertEqual(self.b.score[0],1)
        self.b.addPoint(1)    
        self.assertEqual(self.b.score[1],1)

    def test_addSet(self):
        self.b.addSet(0)
        self.assertEqual(self.b.setPlayers[0],1)
        self.b.addSet(1)    
        self.assertEqual(self.b.setPlayers[1],1)

    def test_PrintGame(self):
        self.b.printGame()

    def test_winGame(self):
        self.b.setPlayers[0]=2
        self.b.winGame()
        print()
        self.b.setPlayers[0]=0
        self.b.setPlayers[1]=2
        self.b.winGame()
        self.b.setPlayers[1]=0

    def test_setUno(self):
        self.b.score=[21,0]
        self.b.winSet()
        self.assertEqual(self.b.setPlayers[0],1)
        self.b.score=[0,21]
        self.b.winSet()
        self.assertEqual(self.b.setPlayers[1],1)
        self.b.score=[22,22]
        self.b.winSet()
        self.assertEqual(self.b.setPlayers[1],1)
        self.assertEqual(self.b.setPlayers[0],1)
        self.b.score=[28,30]
        self.b.winSet()
        self.assertEqual(self.b.setPlayers[1],2)
        self.assertEqual(self.b.setPlayers[0],1)


if __name__ == '__main__':
    unittest.main()