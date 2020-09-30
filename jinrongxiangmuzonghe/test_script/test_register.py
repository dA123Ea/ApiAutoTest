'''
注册接口的脚本
'''

#pytest fixture  参数化的功能
#参数的进来


import pytest

from jinrongxiangmuzonghe.baw.DbOp import DbOp
from jinrongxiangmuzonghe.baw.Menber import Member
from jinrongxiangmuzonghe.caw.Assert import Assert
from jinrongxiangmuzonghe.caw.DataRead import DataRead

#list  多组测试数据
#注册失败
@pytest.fixture(params=DataRead().read_yaml(r"data_case\zc_shibai.yaml"))
def fail_data(request):
    return request.param

#注册成功
@pytest.fixture(params=DataRead().read_yaml(r"data_case\zc_chenggong.yaml"))
def seccess_data(request):
    return request.param

#重复注册
@pytest.fixture(params=DataRead().read_yaml(r"data_case\zc_chongfu.yaml"))
def chongfu_data(request):
    return request.param

#注册失败的逻辑
def test_register_fail(fail_data,url,base_requests):
    print(f"执行注册失败的用例，测试数据为：{fail_data}")
    r=Member().register(url,base_requests,fail_data['data'])

    # assert str(fail_data['expect']['msg'])== r.json()['msg']
    # assert int(fail_data['expect']['status']) == r.json()['status']
    # assert str(fail_data['expect']['code']) == r.json()['code']
    Assert().equal(fail_data['expect'],r.json(),"msg,status,code")
#注册成功的逻辑
def test_register_success(seccess_data,url,db,base_requests):
    print(f"执行注册成功的用例，测试数据为：{seccess_data}")

    # 清理环境
    DbOp().delete_user(db, seccess_data['data']['mobilephone'])

    r = Member().register(url, base_requests, seccess_data['data'])
    # assert str(seccess_data['expect']['msg']) == str(r.json()['msg'])
    # assert str(seccess_data['expect']['status']) == str(r.json()['status'])
    # assert str(seccess_data['expect']['code']) == str(r.json()['code'])
    Assert().equal(seccess_data['expect'], r.json(), "msg,status,code")
    #清理环境
    # DbOp().delete_user(db,seccess_data['data']['mobilephone'])
#重复注册的逻辑
def test_register_repeat(chongfu_data,url,db,base_requests):
    print(f"执行已被注册的用例，测试数据为：{chongfu_data}")
    r = Member().register(url, base_requests, chongfu_data['data'])
    # assert str(chongfu_data['expect']['msg']) == str(r.json()['msg'])
    # assert str(chongfu_data['expect']['status']) == str(r.json()['status'])
    # assert str(chongfu_data['expect']['code']) == str(r.json()['code'])
    Assert().equal(chongfu_data['expect'], r.json(), "msg,status,code")
