
import unittest
from soccer_league import calculate_score
from soccer_league import rank_score

class Test_Soccer(unittest.TestCase):

    def test_calculate_score(self):
        self.assertAlmostEqual(calculate_score(f, team_points),"1\n1\n3\n0\n2\n1\n6\n1\n5\n0" )


    def test_rank_score(self):
        self.assertEqual(rank_score(data_file=None), "1. Tarantulas, 6 pts\n2. Lions, 5 pts\n3. FC Awesome, 1 pts\n3. Snakes, 1 pts\n5. Grouches, 0 pts")
    

if __name__ == '__main__':
    unittest.main()
