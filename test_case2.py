import unittest
from control import login

class Testlogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("开始执行测试用例")

    @classmethod
    def tearDownClass(cls) -> None:
        print("执行测试用例完毕")

    # 初始化方法
    def setUp(self) -> None:
        print("初始化方法")
    # 清空方法
    def tearDown(self) -> None:
        print("执行清空工作")


    def test_login1(self):
        print("执行测试用例1")
        self.assertEqual("登录成功",login('admin','123456'))

    def test_login2(self):
        print("执行测试用例2")
        self.assertEqual("用户名不能为空",login("","123456"))

    def test_login3(self):
        print("执行测试用例3")
        self.assertEqual("密码不能为空",login("adimin",""))

# suite = unittest.TestSuite()
# 方法一
# suite.addTest(Testlogin('test_login2'))
# suite.addTest(Testlogin('test_login3'))
# 方法二
# case_list = [Testlogin('test_login2'),Testlogin('test_login3')]
# suite.addTests(case_list)
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)
# suite_smoke = unittest.TestSuite()
# suite_smoke.addTest(Testlogin('test_login2'))