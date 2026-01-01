# 친구에게 보내기 위해서는 보낼친구가 팀원 초대, 개발자사이트에 가입까지 해야 한다.

import requests
import json
import platform
import os

G_Platform  = platform.system()			            # 플랫폼
G_ExFilePos = os.getcwd() +"\\SMS\\"				# 현재실행위치

with open(G_ExFilePos + "kakao_code.json","r") as fp:
    tokens = json.load(fp)

# 친구 목록가져오기
friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

headers={"Authorization" : "Bearer " + tokens["access_token"]}
result = json.loads(requests.get(friend_url, headers=headers).text)
friends_list = result.get("elements")
friend_id = friends_list[0].get("uuid")
print(friend_id)

send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"성공입니다!",
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        },
        "button_title": "바로 확인"
    })
}
response = requests.post(send_url, headers=headers, data=data)
response.status_code