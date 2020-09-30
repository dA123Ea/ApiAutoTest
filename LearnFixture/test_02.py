'''
fixturn的作用域
1. 默认是函数级别的。
2. 类级别的：在类中首次调用这个fixture的地方调用前置，类里方法执行完后，调用后置
'''

import pytest

@pytest.fixture(scope='class')
def login():
    print("登录系统")
    yield
    print("退出系统")


class TestClass:
    def test_case01(self):
        print("测试用例01")

    def test_case02(self,login):  #这里执行前置
        print("测试用例02")

    def test_case03(self,login):
        print("测试用例03")

    def test_case04(self,login):      #这里执行后置
        print("测试用例04")