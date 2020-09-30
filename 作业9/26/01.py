import requests
#验证有昵称注册成功
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "18709183930", "pwd": "1234567", "regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证无昵称注册成功
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "1234568"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证注册用户时输入合理的手机号、用户名、6位密码，注册成功
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "123456","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证注册用户时输入合理的手机号、用户名、8位密码，注册成功
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "12345678","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证注册用户时输入合理的手机号、用户名、18位密码，注册成功
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "123456789987654321","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证服务器异常注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "123456789987654321","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证mobilephone为空时,注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "", "pwd": "123456","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证password为空时注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证参数为空时注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "", "pwd": "","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证pwd长度为5时注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "12345","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证pwd长度为19时注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "1234567891234567890","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证mobilephone小于11位时注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "1322701105", "pwd": "123456","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证mobilephone大于11位时注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "132270110512", "pwd": "123456","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证mobilephone含特殊字符时注册失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "_&*227011", "pwd": "123456","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------------------------------------------------------------------------")
#验证手机号码已被注册时登录失败
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "123456","regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)