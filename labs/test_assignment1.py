from assignment1 import prime_decomposition
import unittest

class TestPrimeDecomp(unittest.TestCase):
    def test_1(self,):
        self.assertEqual([2], prime_decomposition(2))
    def test_2(self,):
        self.assertEqual([11, 11], prime_decomposition(121))
    def test_3(self,):
        self.assertEqual([2, 2, 5], prime_decomposition(20))
    def test_4(self,):
        self.assertEqual([], prime_decomposition(0))
    def test_5(self,):
        self.assertEqual([2, 3, 5, 7, 11], prime_decomposition(2310))
    

if __name__ =="__main__":
    unittest.main()

