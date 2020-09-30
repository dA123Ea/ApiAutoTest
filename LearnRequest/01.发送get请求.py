
import requests


url ="http://www.baidu.com"
r=requests.get(url)   #发送get请求，变量r接收相应
print(r.text)  #文本类型
print(r.status_code)   #状态吗  200
print(r.reason)  #状态原应 ok
print("r.cookies=",r.cookies) #相应信息的cookies
print(r.headers)#相应的头部信息
print(r.raw)#原始格式的
print(r.raw.read())

print("--------------------------------------------------------------")

#金融项目注册
#？后面是参数，参数之间用&拼接。  参数=值
# url ="http://192.168.150.52:8089/futureloan/mvc/api/member/register?mobilephone=18709183930&pwd=123456&regname=auto"
# r=requests.get(url)
# print(r.text)
# print(r.json())
# print(type(r.json()))
print("--------------------------------------------------------------")
# #方法2：使用params传参
# url ="http://192.168.150.52:8089/futureloan/mvc/api/member/register"
# canshu ={"mobilephone":"18709183931","pwd":"123456","regname":"text"}
# r=requests.get(url,params=canshu)
# print(r.json())
print("--------------------------------------------------------------")
#httpbin，一个测试网站，有get、post等接口，参数任意构造，服务器将发送的请求转成json格式的返回
r=requests.get("http://www.httpbin.org/get?username=123&pwd=456&email=12345@qq.com")
print(r.text)
print("--------------------------------------------------------------")
url ="https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18709183930"
r=requests.get(url)
print(r.text)
# print(r.json())
print("--------------------------------------------------------------")
#发送的请求带请求头
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
r=requests.get("http://www.httpbin.org/get?username=123&pwd=456&email=12345@qq.com",headers=headers)
print(r.text)

#即带参数，又带请求头



