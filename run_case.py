import unittest
from HTMLTestRunner import  HTMLTestRunner
#创建套件

suite = unittest.TestLoader().discover(r'E:\project\demo28_unittest',pattern='test_unittest.py')
#创建运行器
report_path = 'test_report.html'
with open(report_path,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='v1.0')
    runner.run(suite)
