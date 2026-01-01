"""
re(정규식) 모듈을 이용한 문자 등 핸들링 전역함수
윈도우, 리눅스 공통
"""

import re

def SU_RE_WS_SUB01(org_text, sub_text):
    """
    -모든 화이트스페이스를 주어진 문자로 치환
    @rtype: 친환된 문자열
    @param org_text: 바꿀 원본 텍스트
    @type text: 화이트스페이스를 치환할 문자. 보통 스페이스
    """
    if len(org_text) > 0:
        text = re.sub(r'\s+', sub_text, org_text)
        return text
    else:
        return None

def SU_RE_SP_SUB02(sub_pattern, sub_text, org_text):
    """
    -바꿀 원본 텍스트에서 주어진 문자(sub_text)로 치환
    -화이트스페이스는 SU_RE_WS_SUB01함수에서 처리
    @return: 치환된 문자열
    @param sub_pattern:: 패턴, 특수문자 특히 +는 'r\++' 반드시 이렇게 해야 한다. 그렇치 않으면 연산자로 인식
    @param sub_text: 찾은 패턴문자를 치환할 문자. 그리고 여기서는 '+'이렇게 해야한다. 여기도 r'\+'이렇게 하지 않는다.
    @param org_text: 바꿀 원본 텍스트
    """
    if len(org_text) > 0:
        text = re.sub(sub_pattern, sub_text, org_text)
        return text
    else:
        return None

def SU_RE_TURNCHANGE_SUB03(org_text):
    """
    park3 010-1234-5678 이런형태의  이름과 전화번호를 010-1234-5678 park3 이렇게 변경한다.
    todo 이것을 이용하면 다양한 형태도 가능하다
    @param org_text: 항상 park3 010-1234-5678 형태
    @return:
    """
    if len(org_text) > 0:
        p = re.compile(r'(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')
        text = p.sub(r'\g<phone> \g<name>', org_text)
        return text
    else:
        return None

def SU_RE_WS_SPLIT01(org_text):
    """
    -화이트스페이스로 문자열 분리
    @rtype: 주어진 화이트스페이스로 분리된 문자열 리스트
    @param org_text:바꿀 원본 텍스트
    """
    if org_text:
        re_text = re.split(r'\s+',org_text)
        if len(re_text) > 0:
            re_text = [str(x) for x in re_text if len(x) != 0]
        return re_text
    else:
        return None
    
def SU_RE_WS_SPLIT02(sub_pattern, org_text):
    """
    -주어진 패턴으로 문자열 분리
    @rtype: 특수문자로 분리된 문자열 리스트, 빈공백은 삭제 함, 문자열 중 좌우 공백 삭제
    @param sub_pattern: 패턴, 이것은 분리할 문자가 2개이상일때 하나로 만들기 위함
    @param org_text: 바꿀 원본 텍스트
    """
    if org_text:
        re_text = re.split(sub_pattern, org_text)
        if len(re_text) > 0:
            re_text = [str(x).strip() for x in re_text if len(x) != 0]
        return re_text
    else:
        return None