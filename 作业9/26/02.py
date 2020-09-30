import requests
#验证用户登录时输入正确的手机号和密码，登陆成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "13227011051", "pwd": "123456"}
r = requests.post(url, data=canshu)
print(r.text)
print("-----------------------------------------------------------------------")
#验证用户登录时服务器异常，登陆失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "13227011051", "pwd": "123456"}
r = requests.post(url, data=canshu)
print(r.text)
print("-----------------------------------------------------------------------")
#验证用户登录时不输入手机号，登陆失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "", "pwd": "123456"}
r = requests.post(url, data=canshu)
print(r.text)
print("-----------------------------------------------------------------------")
#验证用户登录时不输入密码，登陆失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "13227011051", "pwd": ""}
r = requests.post(url, data=canshu)
print(r.text)
print("-----------------------------------------------------------------------")
#验证用户登录时不输入手机号和密码，登陆失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "", "pwd": ""}
r = requests.post(url, data=canshu)
print(r.text)
print("-----------------------------------------------------------------------")
#验证用户登录时输入错误的手机号，登陆失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "13568246798", "pwd": "123456"}
r = requests.post(url, data=canshu)
print(r.text)
print("-----------------------------------------------------------------------")
#验证用户登录时输入错误的密码，登陆失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "13227011051", "pwd": "1234564"}
r = requests.post(url, data=canshu)
print(r.text)
print("-----------------------------------------------------------------------")
#验证用户登录时输入错误的手机号和密码，登陆失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "13568246798", "pwd": "1234564"}
r = requests.post(url, data=canshu)
print(r.text)

print("-----------------------------充值---------------------------------------")
#验证投资人输入手机号，充值金额，充值成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/recharge"
canshu = {"mobilephone": "13227011051", "amount": "500000"}
r = requests.post(url, data=canshu)
print(r.text)



