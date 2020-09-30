'''
自定义标记
'''
import pytest

@pytest.mark.smoke     #冒烟测试
def test_case01():
    print("test_case01")
@pytest.mark.func      #新功能
def test_case02():
    print("test_case02")

@pytest.mark.func     # 在类上面修饰时，对类里面的方法全都生效
class TestClass:
    @pytest.mark.smoke    # test_case03 既有func的标记，又有smoke的标记
    def test_case03(self):
        print("test_case03")

    def test_case04(self):
        print("test_case04")

    def test_case05(self):
        print("test_case05")