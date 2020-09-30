'''
上传头像
'''

import  requests

url="http://www.httpbin.org/post"
file_path="C:/111.png"
with open(file_path,mode='rb') as f:
    # file={"111.png":(file_path,f)}
    file = {"111.png": (file_path,f,"image/png")}
    r = requests.post(url,files=file)
    print(r.text)
print("-----------------------------------------------")
#上传多个文件
url="http://www.httpbin.org/post"
file_path1="C:/111.png"
file_path2="d:/22.txt"
with open(file_path1,mode='rb') as f1:
    with open(file_path2, mode='r',encoding='utf-8') as f2:
        files={"111.png": (file_path1,f1,"image/png"),
               "222.png": (file_path2, f2, "text/plain")}
        r = requests.post(url, files=files)
        print(r.text)
print("-----------------------------------------------")
# #使用data上传文件，一次只能上传一个文件
with open (file_path2,mode='rb')as f3:
    r = requests.post(url,data=f3)
    print(r.text)
