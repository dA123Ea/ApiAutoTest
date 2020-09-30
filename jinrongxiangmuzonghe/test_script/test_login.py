
import pytest
from jinrongxiangmuzonghe.baw.DbOp import DbOp
from jinrongxiangmuzonghe.baw.Menber import Member
from jinrongxiangmuzonghe.caw.Assert import Assert
from jinrongxiangmuzonghe.caw.DataRead import DataRead


@pytest.fixture(params=DataRead().read_yaml(r"data_case\dl_shibai.yaml"))
def login_data(request):
    return request.param

def test_login(register,url,base_requests,login_data):
    r = Member().login(url, base_requests, login_data['data'])
    Assert().equal(login_data['expect'], r.json(), "msg,status,code")














# #登录失败
# @pytest.fixture(params=DataRead().read_yaml(r"data_case\dl_shibai.yaml"))
# def fail_data(request):
#     return request.param
#
# #登录成功
# @pytest.fixture(params=DataRead().read_yaml(r"data_case\dl_chenggong.yaml"))
# def success_data(request):
#     return request.param
#
#
# def test_login_fail(fail_data,url,base_requests):
#     print(f"执行登录失败的用例，测试数据为：{fail_data}")
#     r=Member().login(url,base_requests,fail_data['data'])
#     Assert().equal(fail_data['expect'],r.json(),"msg,status,code")
#
# def test_login_seccess(success_data,url,base_requests):
#     print(f"执行登录成功的用例，测试数据为：{success_data}")
#     #清理环境
#     r = Member().login(url, base_requests, success_data['data'])
#     Assert().equal(success_data['expect'], r.json(), "msg,status,code")
