'''
1.爬虫之类的场景

'''
import requests
proxy={
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
r=requests.get("http://www.baidu.com/s?wd=擦汗拿过奖",proxies=proxy)
print("扎气球拿奖品,老板都擦汗了:大哥给我留条活路吧_腾讯视频" in r.text)
# requests.put()
# requests.delete()