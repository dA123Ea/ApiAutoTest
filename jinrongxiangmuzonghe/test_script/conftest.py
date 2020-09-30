'''
脚本层的公共方法
'''
import pytest

#读取环境文件，获取url
from jinrongxiangmuzonghe.baw.DbOp import DbOp
from jinrongxiangmuzonghe.baw.Menber import Member
from jinrongxiangmuzonghe.caw.Assert import Assert
from jinrongxiangmuzonghe.caw.BaseRequests import BaseRequests
from jinrongxiangmuzonghe.caw.DataRead import DataRead

ENVPATH=r'data_env\env.ini'

@pytest.fixture(scope='session')
def url():
    return DataRead().read_ini(ENVPATH,'url')

@pytest.fixture(scope='session')
def db():
    return eval(DataRead().read_ini(ENVPATH,'db'))

#BaseRequests 实例化，整个执行过程实例化一次
@pytest.fixture(scope='session')
def base_requests():
    return BaseRequests()


@pytest.fixture(scope="session",params=DataRead().read_yaml(r"data_case\zc_chenggong1.yaml"))
def setup_data(request):
    return request.param


@pytest.fixture(scope="session")
def register(setup_data,db,url,base_requests):   #注册
    r = Member().register(url, base_requests, setup_data['data'])
    Assert().equal(setup_data['expect'], r.json(), "msg,status,code")
    yield   #清理
    DbOp().delete_user(db, setup_data['data']['mobilephone'])



