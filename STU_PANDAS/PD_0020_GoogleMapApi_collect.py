# -*- coding: utf-8 -*-

# 라이브러리 가져오기. 
import googlemaps
import pandas as pd

# 현재 나는 구글 글라우드 서비스의 빌링 시스템이 삭제해서 키가 안먹힘..ㅋㅋ
my_key = "AIzaSyBhMXAVJnM7hblfOH1CHvmD3qrI5uHA6J0"

# 구글맵스 객체 생성하기
maps = googlemaps.Client(key=my_key)  # my key값 입력

lat = []  #위도
lng = []  #경도

# 장소(또는 주소) 리스트
places = ["서울시청", "국립국악원", "해운대해수욕장"]

i=0
for place in places:   
    i = i + 1
    try:
        # 지오코딩 API 결과값 호출하여 geo_location 변수에 저장
        # gl = maps.geocode('서울시청',language='ko') # 이렇게 하면 모든 정보를 다가직 옴
        geo_location = maps.geocode(place,language='ko')[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
    except:
        lat.append('')
        lng.append('')

# 데이터프레임으로 변환하기
df = pd.DataFrame({'위도':lat, '경도':lng}, index=places)
print('\n')
print(df)

