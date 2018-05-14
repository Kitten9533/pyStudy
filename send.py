import json
import requests

KEY = '7e4a79e3e5fc4f63b7d87d68e5802bc8'    # change to your API KEY
url = 'http://www.tuling123.com/openapi/api'

req_info = ('%s' % 'haha').encode('utf-8')

query = {'key': KEY, 'info': req_info}
headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

# 方法一、用requests模块已get方式获取内容
r = requests.get(url, params=query, headers=headers)
res = r.text
print(json.loads(res).get('text').replace('<br>', '\n'))