'''
1. 测试前置和后置
2. 类级别和方法级别
'''

# 测试类使用TEST开头，里面不能用init法法
import pytest


def test_case1():
    print("用例1")

class TestClass:
    def setup_class(self):
        print("测试前置：类里所有用例开始前执行")

    def teardown_class(self):
        print("测试后置：类里所有用例结束后执行")

    def setup(self):
        print("测试前置，每个方法前置性")

    def teardown(self):
        print("测试后置，每个方法后置性")

    def test_case1(self):
        print("用例1")

    def test_case2(self):
        print("用例2")


if __name__ == "__main__":
    pytest.main(["-v -n 2", "test_03.py"])
