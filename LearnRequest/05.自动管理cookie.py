'''
自动管理cookie
'''
import requests
#新建一个session，通过session 自动管理cookie
s=requests.Session()
#访问之前。打印cookie。为空
# print(s.cookies)# RequestsCookiejar
# print(requests.utils.dict_from_cookiejar(s.cookies))#cookiejar 转为字典

#访问摆个的首页
r=s.get("http://www.bagevent.com")
# print(s.cookies)# RequestsCookiejar
# print(requests.utils.dict_from_cookiejar(s.cookies))#cookiejar 转为字典
param ={
        "access_type":1,
        "loginType":1,
        "emailLoginWay":0,
        "account":"2780487875@qq.com",
        "password":"qq2780487875",
        "remindmeBox":"on",
        "remindme":1
}
r=s.post("http://www.bagevent.com/user/login",data=param)
# print(("登录之后，打印Cookie.Cookie有5条"))
# print(s.cookies)
# print(requests.utils.dict_from_cookiejar(s.cookies))#cookiejar 转为字典

r =s.get("https://www.bagevent.com/vlist/common/surveyList")
print(r.json())
print(r.json()["list"][0]["survey_id"])