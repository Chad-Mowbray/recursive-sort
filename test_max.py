import unittest
from get_max import get_max


class TestMax(unittest.TestCase):
    
    def test_max_1(self):
        inp = [9]
        self.assertEqual(get_max(inp), 9)
        
    def test_max_2(self):
        inp = [1,9]
        self.assertEqual(get_max(inp), 9)   
        
    def test_max_2_descending(self):
        inp = [9,1]
        self.assertEqual(get_max(inp), 9)

    def test_max_4_ascending(self):
        inp = [1,2,3,9]
        self.assertEqual(get_max(inp), 9)   

    def test_max_4_mixed(self):
        inp = [1,9,3,4]
        self.assertEqual(get_max(inp), 9)  

    def test_max_4_dup(self):
        inp = [1,9,9,4]
        self.assertEqual(get_max(inp), 9)  
       
    def test_max_2_dup(self):
        inp = [9,9]
        self.assertEqual(get_max(inp), 9)   
        
if __name__ == "__main__":
    unittest.main()