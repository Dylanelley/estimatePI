import unittest
import math
import  randomly_estimate_pi



class TestEstimatePi(unittest.TestCase):

    def test_vector_length(self):
        vector = [3, 4]
        length = 5
        self.assertEqual(randomly_estimate_pi.vector2_length(vector), length, "Vector length not correct")

    def test_estimate_pi(self):
        n = 1000000
        decimal_places = 2
        self.assertAlmostEqual(randomly_estimate_pi.estimate_pi(n), math.pi, msg="Pi estimate not correct", places=decimal_places)



if __name__ == "__main__":
    unittest.main()