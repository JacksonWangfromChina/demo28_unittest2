import unittest
from control import age
from parameterized import parameterized

class Testlogin(unittest.TestCase):

    # def setUp(self):
    #     print("初始化方法")
    #
    # def tearDown(self):
    #     print("执行清空工作")
    #
    # def test_age1(self):
    #     print("执行测试用例1")
    #     self.assertEqual("baby",age(1))
    #
    # def test_age2(self):
    #     print("执行测试用例2")
    #     self.assertEqual("learning walk", age(3))
    # def test_age3(self):
    #     print("执行测试用例3")
    #     self.assertEqual("child",age(5))

#参数化
    x = str
    y = int
    age = int
    @parameterized.expand([("child",age(5)),("learning walk", age(3)),("baby",age(1))])
    def test_add(self,x,y):
        self.assertEqual(x,age(y))
        #参数化

# if __name__ == '__main__':
#     unittest.main()

# suite = unittest.TestSuite()  #引用TestSuite类
# suite.addTest(Testlogin('test_age1'))  #使用TestSuite的方法
# suite.addTest(Testlogin("test_age3"))
#
# runner = unittest.TextTestRunner() #引用TextTestRunner类
# runner.run(suite)

