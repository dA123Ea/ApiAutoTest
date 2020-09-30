'''
conftest.py: 存放session级别的fixture的文件
'''
import pytest


@pytest.fixture(scope='session')
def login():
    print("登录")
    yield
    print("退出登录")

@pytest.fixture(scope='session')
def db():
    print("登录数据库")
    yield
    print("退出数据库")