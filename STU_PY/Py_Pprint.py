
# 출력을 이쁘게 출력한다.
# json파일이나 이렇때 주로 사용할 듯

import pprint
from decimal import *
import datetime

pain = {'job': '청소원', 'company': '주식회사 고', 'ssn': '780820-1284721', 'residence': '강원도 성남시 삼성가 (은정이동)', 'current_location': (Decimal('68.576801'), Decimal('67.848311')), 'blood_group': 'B-', 'website': ['https://www.igimgim.com/', 'https://www.noryubag.com/'], 'username': 'hyeonsugmun', 'name': '오정남', 'sex': 'M', 'address': '광주광역시 관악 구 역삼283길 (은경노이리)', 'mail': 'ci@daum.net', 'birthdate': datetime.date(1939, 2, 28)}, {'job': '패션 디자이너', 'company': '(유) 곽', 'ssn': '790726-2477976', 'residence': '서울특별시 강남구 테헤란로 (우진김김동)', 'current_location': (Decimal('3.4377915'), Decimal('-86.946072')), 'blood_group': 'B+', 'website': ['http://www.ju.kr/', 'http://www.jusighoesa.kr/', 'http://www.igim.com/', 'http://www.baggimgim.com/'], 'username': 'jangyeongceol', 'name': '이지훈', 'sex': 'M', 'address': '강원도 안산시 상록구 언주길 (수민김김읍)', 'mail': 'sanghun69@nate.com', 'birthdate': datetime.date(1948, 5, 19)}, {'job': '미용사', 'company': '최박', 'ssn': '040125-1449947', 'residence': '인천광역시 관악구 백제고분길 (성 호백김리)', 'current_location': (Decimal('51.603972'), Decimal('-107.817835')), 'blood_group': 'AB+', 'website': ['https://www.yuhanhoesa.kr/', 'https://gimhani.com/', 'https://www.imun.net/'], 'username': 'hyeonjeonghan', 'name': '이춘자', 'sex': 'F', 'address': '충청북도 양주시 반포대4길', 'mail': 'kgweon@hanmail.net', 'birthdate': datetime.date(1940, 12, 6)}
print(pain)

print('=' * 50)
pprint.pprint(pain)