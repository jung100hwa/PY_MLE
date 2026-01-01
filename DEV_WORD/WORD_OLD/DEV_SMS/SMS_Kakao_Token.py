
# 카카오톡은 프로그램으로 보낸다는 것은 큰 의미가 없을 것 같다.
# 친구들이 모드 개발자사이트에 가입되어야 한다는 것. 이게 문제내
# kakao 를 위한 것
# 일반적으로 한번만 수행. 이미 토큰을 가져왔기 때문

# REST KEY는 일정시간이 지나면 갱신회야 된다고 한다.
# REST KEY : 0d6d11a876fd009ba917c5d36599ef92

# 반드시 추가동의 키 talk_message를 넣어서 토큰을 얻어야 한다. 다만 이때는 내 자신에게만
# https://kauth.kakao.com/oauth/authorize?client_id=0d6d11a876fd009ba917c5d36599ef92&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message

# 카카오 개발자 사이트에 등록된 친구에게 보낼려고 하며는 추가동의 friends 뒤에 추가. 대부분 이렇게 사용함
# https://kauth.kakao.com/oauth/authorize?client_id=0d6d11a876fd009ba917c5d36599ef92&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message, friends

# 아래 사이트를 참조한다.
# https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#additional-consent

# 추가동의까지 해서 얻은 토큰
# GM9WBbeF1fqA_sO-08Vjz9dxhtRskbt-Ehy7Z5Z1UxAbjf6Gdy7WNo0_l10z2GAs9QUFwAopyNkAAAF9i0geYQ

import requests
import json
import platform
import os

G_Platform  = platform.system()			            # 플랫폼
G_ExFilePos = os.getcwd() +"\\SMS\\"				# 현재실행위치

url             = "https://kauth.kakao.com/oauth/token"
rest_api_key    = "0d6d11a876fd009ba917c5d36599ef92"
redirect_uri    = "https://example.com/oauth"

# 아래코든 매번 업데이트 해야 한다.
authorize_code  = "9ry0yTbK-MMA9Y-sFY8vuzmcb3r3eXb3xPNppk6S903BSjYQs4VZ_42c-BS8rC7AQZBzZQo9cusAAAF9lM2elQ"

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
with open(G_ExFilePos + "kakao_code.json","w") as fp:
    json.dump(tokens, fp)