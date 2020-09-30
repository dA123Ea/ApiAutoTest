'''
fixture的作用域：
1. 默认是函数级别的。
2. 模块级别的：在模块中首次调用这个fixture的地方调用前置，模块里方法执行完后，调用后置
'''

import pytest

@pytest.fixture(scope="module")
def login():
    print('登录')
    yield
    print("退出登录")

@pytest.fixture(scope="module")
def db():
    print('连接数据库')
    yield
    print("退出数据库")

class TestClass:
    def test_case01(self):
        print("测试用例01")

    def test_case02(self,login):  #这里执行前置
        print("测试用例02")

    def test_case03(self,db):   #这里是执行db的前置
        print("测试用例03")

    def test_case04(self):
        print("测试用例04")

class TestClass2:
    def test_case05(self):
        print("case05")

    def test_case02(self,login):
        print("case02")

    def test_case03(self,login):
        print("case03")

    def test_case04(self,login):#执行后置
        print("case04")