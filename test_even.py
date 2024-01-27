import unittest
from odd_or_even import is_even


class TestEven(unittest.TestCase):
    
    def test_0_is_true(self):
        result = is_even(0)
        self.assertEqual(result, True)

    def test_1_is_false(self):
        result = is_even(1)
        self.assertEqual(result, False) 
        
    def test_2_is_true(self):
        result = is_even(2)
        self.assertEqual(result, True) 
      
    def test_5_is_false(self):
        result = is_even(5)
        self.assertEqual(result, False)   
        
if __name__ == "__main__":
    unittest.main()