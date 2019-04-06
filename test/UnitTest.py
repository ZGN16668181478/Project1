import unittest
from UnitForTest import Add,Sum

class Test(unittest.TestCase):
    def setUp(self):
        print('The UnitTest is running!')
    def tearDown(self):
        print('The UnitTest is shutdowning!')

    # 进行测试
    def test_Add(self):
        self.assertEqual(Add(1,2),3,'你个智障，这你都能算错！')
    def test_Sum(self):
        self.assertEqual(Sum(1,2),2,'oh shit mother fucker!')

if __name__=='__main__':
    unittest.main()