
# 1 : 지도를 만들고
# 2 : 지도위에 마커를 만들고
# 3 : html로 저장함

import folium
import os
import pandas as pd
import json


####################################################################### 다양한 맵스타일
seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12)
seoul_map.save('./E_FILE/seoul1.html')

####################################################################### 약간 산지지형맵
seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12)
seoul_map.save('./E_FILE/PANDAS/seoul2.html')

####################################################################### 도로망 위주
seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Toner', zoom_start=12)
seoul_map.save('../E_FILE/PANDAS/seoul3.html')

####################################################################### 지도 위에 마커로 표시
df = pd.read_excel('../E_FILE/PANDAS/서울지역 대학교 위치.xlsx', index_col=0)
print(df)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat,lng], popup=name).add_to(seoul_map)

seoul_map.save('../E_FILE/PANDAS/seoul_national.html')


####################################################################### 지도 위에 원형마크 표시
# 대학교 리스트를 데이터프레임 변환
df = pd.read_excel('../E_FILE/PANDAS/서울지역 대학교 위치.xlsx', index_col=0)

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)

# 대학교 위치정보를 CircleMarker로 표시
for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius=10,         # 원의 반지름
                        color='brown',         # 원의 둘레 색상
                        fill=True,
                        fill_color='coral',    # 원을 채우는 색
                        fill_opacity=0.7, # 투명도    
                        popup=name
    ).add_to(seoul_map)

# 지도를 HTML 파일로 저장하기
seoul_map.save('../E_FILE/PANDAS/seoul_colleges2.html')



# #######################################################################  지도상에 영역을 지정해 보자
df = pd.read_excel('../E_FILE/PANDAS/경기도인구데이터.xlsx', index_col='구분')
print(df)
df.columns = df.columns.map(str) # map함수는 시리즈에만 적용되고 문자열로 된 컬럼이라는 뜻. 인터넷 참조
print(df.columns)

# 경계정보를 가진 json 파일을 불러오기
try:
    geo_data = json.load(open('../E_FILE/PANDAS/경기도행정구역경계.json', encoding='utf-8'))
except:
    geo_data = json.load(open('../E_FILE/PANDAS/경기도행정구역경계.json', encoding='utf-8-sig'))

# 경기도 지도 만들기
g_map = folium.Map(location=[37.5502,126.982],
                   tiles='Stamen Terrain', zoom_start=9)

# 출력할 연도 선택 (2007 ~ 2017년 중에서 선택)
year = '2017'

# 2007년 전국 인구 데이터
folium.Choropleth(geo_data=geo_data,    # 지도 경계
                 data = df[year],      # 표시하려는 데이터
                 columns = [df.index, df[year]],  # 열 지정
                 fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
                 threshold_scale=[10000, 100000, 300000, 500000, 700000],
                 key_on='feature.properties.name',
                 ).add_to(g_map)
g_map.save('../E_FILE/PANDAS/people.html')