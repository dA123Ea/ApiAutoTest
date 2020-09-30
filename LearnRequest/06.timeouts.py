'''
两种超时的场景：
1.接口耗时比较久，设置耗时时间
2.接口性能
'''

import requests

for i in range(10):
    try:
        url ="https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18091831234"
        ret =requests.get(url,timeout=0.09)
        print(ret.status_code)
    except Exception as e:
        print(e)
