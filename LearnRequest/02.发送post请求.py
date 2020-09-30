import requests
'''

'''

url="http://www.httpbin.org/post"
canshu={"username":"root","password":"123456"}
r=requests.post(url,data=canshu)
print(r.text)

r=requests.post(url,json=canshu)
print(r.text)


url="http://192.168.150.52:8089/futureloan/mvc/api/member/login"
canshu={"mobilephone":"18709183931","pwd":"123456"}
r=requests.post(url,data=canshu)
print(r.text)
