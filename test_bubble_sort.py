import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    
    def test_1_len(self):
        inp = [9]
        self.assertEqual(bubble_sort(inp), inp)
        
    def test_2_len(self):
        inp = [1,9]
        self.assertEqual(bubble_sort(inp), inp)   

    def test_2_len_rev(self):
        inp = [9,1]
        self.assertEqual(bubble_sort(inp), [1,9])      
   
    def test_4_len_mixed(self):
        inp = [9,1,10,2]
        self.assertEqual(bubble_sort(inp), [1,2,9,10])           
             
if __name__ == "__main__":
    unittest.main()