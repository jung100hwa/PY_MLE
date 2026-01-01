"""
unicodedata 유니코드 워드를 정규화해서 사용하기 위한 모듈
여기서 정규화라는 것은 특정 포맷을 말함. 어려워 할 것 없음
유니코드는 여러 형태가 있음. 단어 뒤에 발음기호, 악센트 등등
https://velog.io/@qsdcfd/%EC%A0%9C%EB%8C%80%EB%A1%9C-%EB%B9%84%EA%B5%90%ED%95%98%EA%B8%B0-%EC%9C%84%ED%95%B4-%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C-%EC%A0%95%EA%B7%9C%ED%99%94%ED%95%98%EA%B8%B0
https://sweepover.tistory.com/7
https://sweepover.tistory.com/7
""" 
import unicodedata
from unicodedata import normalize
import string

# 이런것도 되네. 
all_letters = string.ascii_letters + " .,;'"
print(all_letters)
print()

n_letters = len(all_letters)
 

def unicodeToAscii(word):
    return ''.join(
        char for char in unicodedata.normalize('NFD', word)
        if unicodedata.category(char) != 'Mn' and char in all_letters
    )
    
print(unicodeToAscii('Ślusàrski'))