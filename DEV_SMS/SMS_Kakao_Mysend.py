import requests
import json
import platform
import os

G_Platform  = platform.system()			            # 플랫폼
G_ExFilePos = os.getcwd() +"\\SMS\\"				# 현재실행위치

with open(G_ExFilePos + "kakao_code.json","r") as fp:
    tokens = json.load(fp)

# 내자신에게 보내기
url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"Hello, world!!!!",
        "link":{
            "web_url":"www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code