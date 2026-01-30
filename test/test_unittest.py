import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)
from src import calculator

class TestCalculator(unittest.TestCase):
    
    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)
        self.assertEqual(calculator.fun1(2.5, 3.5), 6.0)
    
    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)
        self.assertEqual(calculator.fun2(10, 3), 7)
    
    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)
        self.assertEqual(calculator.fun3(2.5, 4), 10.0)
    
    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)
        self.assertEqual(calculator.fun4(1, 2, 3), 6)
    
    def test_fun5(self):
        self.assertEqual(calculator.fun5(10, 2), 5.0)
        self.assertEqual(calculator.fun5(15, 3), 5.0)
        self.assertEqual(calculator.fun5(-10, 2), -5.0)
        self.assertEqual(calculator.fun5(7, 2), 3.5)
        self.assertEqual(calculator.fun5(0, 5), 0.0)
        self.assertEqual(calculator.fun5(20, 4), 5.0)
    
    def test_fun6(self):
        self.assertEqual(calculator.fun6(2, 3), 8)
        self.assertEqual(calculator.fun6(5, 2), 25)
        self.assertEqual(calculator.fun6(2, 0), 1)
        self.assertEqual(calculator.fun6(4, -1), 0.25)
        self.assertEqual(calculator.fun6(9, 0.5), 3.0)
        self.assertEqual(calculator.fun6(3, 3), 27)
    
    def test_fun7(self):
        self.assertEqual(calculator.fun7(0), 1)
        self.assertEqual(calculator.fun7(1), 1)
        self.assertEqual(calculator.fun7(3), 6)
        self.assertEqual(calculator.fun7(4), 24)
        self.assertEqual(calculator.fun7(5), 120)
        self.assertEqual(calculator.fun7(6), 720)
    
    def test_fun8(self):
        result1 = calculator.fun8([1, 2, 3, 4, 5])
        self.assertEqual(result1['mean'], 3.0)
        self.assertEqual(result1['median'], 3.0)
        self.assertEqual(result1['count'], 5)
        
        result2 = calculator.fun8([1, 2, 3, 4])
        self.assertEqual(result2['median'], 2.5)
        self.assertEqual(result2['mean'], 2.5)
        
        result3 = calculator.fun8([1, 2, 2, 3])
        self.assertEqual(result3['mode'], 2)
        self.assertEqual(result3['count'], 4)
        
        result4 = calculator.fun8([5])
        self.assertEqual(result4['mean'], 5)
        self.assertEqual(result4['median'], 5)
    
    def test_fun9(self):
        self.assertEqual(calculator.fun9(1), [0])
        self.assertEqual(calculator.fun9(2), [0, 1])
        self.assertEqual(calculator.fun9(5), [0, 1, 1, 2, 3])
        self.assertEqual(calculator.fun9(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(calculator.fun9(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(calculator.fun9(3), [0, 1, 1])
    
    def test_fun10(self):
        self.assertEqual(calculator.fun10([1, 2], 3), 7)  # 1 + 2*3
        self.assertEqual(calculator.fun10([1, 2, 1], 2), 9)  # 1 + 2*2 + 1*4
        self.assertEqual(calculator.fun10([5], 10), 5)  # constant polynomial
        self.assertEqual(calculator.fun10([3, 2, 1], 0), 3)  # at x=0
        self.assertEqual(calculator.fun10([1, 1, 1], 1), 3)  # 1 + 1 + 1
        self.assertEqual(calculator.fun10([2, 3], 1), 5)  # 2 + 3*1
    
    def test_fun11(self):
        roots1 = calculator.fun11(1, -5, 6)
        self.assertEqual(len(roots1), 2)
        self.assertIn(2.0, roots1)
        self.assertIn(3.0, roots1)
        
        roots2 = calculator.fun11(1, -4, 4)
        self.assertEqual(len(roots2), 1)
        self.assertEqual(roots2[0], 2.0)
        
        roots3 = calculator.fun11(1, 0, 1)
        self.assertIsNone(roots3)
        
        roots4 = calculator.fun11(1, -3, 2)
        self.assertEqual(len(roots4), 2)
        self.assertIn(1.0, roots4)
        self.assertIn(2.0, roots4)
    
    def test_fun12(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        result1 = calculator.fun12(mat1, mat2)
        self.assertEqual(result1, [[19, 22], [43, 50]])
        
        identity = [[1, 0], [0, 1]]
        result2 = calculator.fun12(mat1, identity)
        self.assertEqual(result2, [[1, 2], [3, 4]])
        
        mat3 = [[1, 2, 3]]
        mat4 = [[4], [5], [6]]
        result3 = calculator.fun12(mat3, mat4)
        self.assertEqual(result3, [[32]])
        
        mat5 = [[2, 1], [1, 2]]
        mat6 = [[1, 1], [2, 1]]
        result4 = calculator.fun12(mat5, mat6)
        self.assertEqual(result4, [[4, 3], [5, 3]])
        
        mat7 = [[1, 2], [3, 4], [5, 6]]
        mat8 = [[1, 2], [3, 4]]
        result5 = calculator.fun12(mat7, mat8)
        self.assertEqual(result5, [[7, 10], [15, 22], [23, 34]])

if __name__ == '__main__':
    unittest.main()