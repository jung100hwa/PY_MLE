"""
1. 사용키를 환경설정 파일에 저장해서 불러온다.
2. 키를 바로 삽입 할 수 있지만 openAPI, chatGPT 등에서 노출되었다며 비활성화 시켜 버린다.
3. 특히 git에 올리는 순간 거의 기존 키는 쓸 수가 없다.

먼저 현재디렉토리 또는 상위디렉토리에 .env파일을 만들고 정의한다.
"""

from dotenv import load_dotenv
import os

#.env 파일 로드(현재 디덱토리 -> 상위디렉토리..탐색)
load_dotenv()

api_key = os.getenv('api_key')

print(api_key)