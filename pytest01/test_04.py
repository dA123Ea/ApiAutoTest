'''
mark 标记实现参数化
实现跳过
'''

import pytest
import requests
url ="http://192.168.150.52:8089/futureloan/mvc/api/member/register"
case_data =[("18091234567","123456","投资人","手机已被注册","20110",0),
            ("180","8888","借款人","密码长度必须为6~18位","20108",0)]
@pytest.mark.parametrize("mobile,pwd,regname,msg,code,status",case_data)
#测试逻辑
def test_register(mobile,pwd,regname,msg,code,status):

    print(f"测试注册功能：{mobile},{pwd},{regname}")
    param={"mobilephone":mobile,"pwd":pwd,"regname":regname}
    ret=requests.post(url,data=param)
    assert  ret.json()["msg"]==msg
    assert ret.json()["code"] == code
    assert ret.json()["status"] == status


withdraw_data =[("18709183930","10")]

@pytest.mark.skipif(1==1,reason="前面表达式为true时，跳过：表达式为false时，不跳过")
# withdraw_data =[("18709183930","10")]
@pytest.mark.parametrize("mobile,amount",withdraw_data)
def test_withdraw(mobile,amount):
    url ="http://192.168.150.52:8089/futureloan/mvc/api/member/withdtaw"
    print(f"测试取款的功能:{mobile},{amount}")
    param ={"mobilephone":mobile,"amount":amount}
    ret =requests.post(url,data=param)
    assert  ret.json()['msg']!="服务异常"

