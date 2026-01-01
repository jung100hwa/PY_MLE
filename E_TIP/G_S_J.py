import unicodedata
 
def hhj_unicodeaccentToAscii(line):
    """_summary_
    유니코드 형식의 말(이탈리아, 불어) 등에는 악센트가 있는데 이것을 제거하고 가져온다.
     'NFD'와 'NFC'는 각각 윈도우와 맥의 파일 이름 저장 방식

    :param line: 악센트가 있는 유니코드 문장
    :return: 정규화된 문장
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', line)
        if unicodedata.category(c) != 'Mn'
    )