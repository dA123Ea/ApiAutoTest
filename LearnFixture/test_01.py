'''
fixture:灵活的前置|后置
'''

import pytest

@pytest.fixture(autouse=True)   # 测试用例会自动使用，不用作为参数传递
def data():
    print("准备测试用例")

@pytest.fixture()   # 测试预置，需要执行该预置的地方，将函数名作为参数传入即可。
def login():
    print("登录功能")   #yield之前是测试前置
    yield
    print("退出登录")   #yield之后是测试后置
    print("用例执行完毕")

def test_register():
    print("注册，不用登录")

def test_recharge(login):   # 作为参数传进来
    print("充值，先登录")
@pytest.mark.usefixtures("login")    #也可以使用usefixtures
def test_withdraw():
    print("取现，先登录")