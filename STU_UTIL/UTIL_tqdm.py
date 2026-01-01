"""
진행사항을 표시해주는 유틸
https://skillmemory.tistory.com/entry/tqdm-%EC%82%AC%EC%9A%A9%EB%B2%95-python-%EC%A7%84%ED%96%89%EB%A5%A0-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EB%B0%94
"""

from tqdm import tqdm
import time

# text = ""
# for char in tqdm(['a','b','c','d']):
#     time.sleep(1)
#     text = text + char


for item in tqdm(range(100), desc="진행사항", mininterval=0.01):
    time.sleep(0.1)