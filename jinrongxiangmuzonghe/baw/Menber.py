'''
业务AW：按模块划分
'''

from jinrongxiangmuzonghe.caw.BaseRequests import BaseRequests
REGISTER = "/futureloan/mvc/api/member/register"
LOGIN="/futureloan/mvc/api/member/login"
class Member:
    def register(self,url,base_requests,data):
        real_url=url +REGISTER
        r=base_requests.post(real_url,data=data)
        return r
    def login(self,url,base_login,data):
        real_url = url + LOGIN
        r = base_login.post(real_url, data=data)
        return r


if __name__ == '__main__':

    r=Member().register("http://192.168.150.222:8081",BaseRequests(),{"mobilephone":"123456"})
    print(r.text)




