# 딥러닝과 관련된 모듈 집합
import re
import pandas as pd
import glob
import os
import PY_PKG.SU_FILE_WRITE_READ as psf

# 띄어쓰기 제대로 하기 위한 모듈
# pip install git+https://github.com/haven-jeon/PyKoSpacing.git 설치해야 함
from pykospacing import Spacing

# 한글 맞춤법 바로 잡기. 인터넷에 연결되어 있어야 하고 아래 모듈을 설치한 다음 수정을 해야 만 제대로 돌아간다.
# pip install git+https://github.com/ssut/py-hanspell.git
# 수정 부분
# 1. constants.py 의 base_url = "https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy"로 수정
# 2. spell_checker.py 에서 payload 수정
# payload = {
#         '_callback': 'window.__jindo2_callback._spellingCheck_0',
#         'q': text
#     } 이 부분을 아래처럼
# payload = {
#         '_callback': 'jQuery11240003383472025177525_1680133565087',
#         'q': text,
#         'where': 'nexearch',
#         'color_blindness': 0
#     }
# 3. spell_checker.py 약 61번째줄
# r = r.text[42:-2] 를 r=r.text[44:-2]로 수정
from hanspell import spell_checker

# 영어 불용어 제거(한글은 직접 정의하는게 나을 듯)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

# pip install customized_konlpy
from ckonlpy.tag import Twitter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# 아래는 프로젝트가 시작되면 직접 정의를 해야 한다.
G_H_STOPWORD = ['가가가']
G_H_TWITTER  = ['은경이']

############################################################# 문자열 전처리 함수(하나의 문자열)
# mode : 문자열이 너무 길어버리면 맞춤법 검사 모듈이 안됨. 네이버 맞춤법 api 활용하는데 500자 내외인듯
#        때문에 문자열이 크면 리스트로 쪼개야 한다. 1-문자열, 2-문자열 리스트.
# strSent : 전처리 대상 문자열 또는 문자열 리스트
# splitchar : strSect가 문자열 리스트 일때 문법 검사 후 조인할 문자. 보통 SU_MO_TextFileToStr3 함수에서
#             큰 문자열을 무슨 문자로 분리 했는지. 그 분리문자를 넣어 줌
# alloption : 모든 단계를 다 수행
def SU_DL_PREPROCELLING(mode, strSent, splitchar=".", alloption=0):
    try:
        if mode == 1:   # 하나의 문자열일때
            if alloption == 1:
                strSent = SU_DL_SPELL_CHECKER(strSent)      # 맞춤법을 검사하고(한글만)
            strSent = SU_DL_SPACING(strSent)            # 띄어쓰기를 바로 잡고(한글만)
            strSent = SU_DL_DEL_STOPWORD(strSent,0,1)       # 불용어 제거(영어는 하지 않고 한글 중에서 토큰화 하지 않고 문자열 그대로)
            return strSent

        if mode == 2:   #문자열을 항목으로 가진 리스트일때(한글이 아닌이상 이것을 쓸 이유가 없다. 그냥 통으로. 특히 조달에서)
            strRelist = []
            for strLine in strSent:
                if alloption == 1:
                    strLine = SU_DL_SPELL_CHECKER(strLine)     # 리스트 항목마다 맞줌법 검사(한글만)
                strLine = SU_DL_DEL_STOPWORD(strLine, 0, 1)    # 불용어 제거(영어는 하지 않고 한글 중에서 토큰화 하지 않고 문자열 그대로)
                strRelist.append(strLine)
            strSent = splitchar.join(strRelist)
            if alloption == 1:
                strSent = SU_DL_SPACING(strSent)               # 띄어쓰기를 바로 잡고(한글만)
            return strSent
    except:
        pass
    return


############################################################# 문자열 띄어 쓰기를 제대로 하기 위한 함수
# strSent : 전처리 대상 문자열
# 한글만 가능
# 한계 : 시간이 엄청 많이 걸림
def SU_DL_SPACING(strSent):
    try:
        spacing = Spacing()
        strSent = spacing(strSent) # 여기에서 스페이스 등 다 해결되는 듯. 아래 문장은 할 필요 없을 듯
        # strSent = re.sub(r'\s{2,}','', strSent) # 스페이스2개 이상인것
        return strSent
    except:
        pass
    return

############################################################# 한글 맞춤법 바로 잡기(네이버 맞춤법 활용, 인터넷 연결 필요)
# strSent : 전처리 대상 문자열
# 한글만 가능
def SU_DL_SPELL_CHECKER(strSent):
    try:
        spelled_strSent = spell_checker.check(strSent)
        strSent = spelled_strSent.checked
        return strSent
    except:
        pass
    return


############################################################# 불용어 제거(불용어 : 판단에 저해가 되는 조사 등)
# strSent : 전처리 대상 문자열
# endmod  : 영어를 불용어 처리 할지(0-처리하지 않음, 1-토큰화처리)
# kormid  : 한글를 불용어 처리 할지(0-처리하지 않음, 1-replace 처리)
# 주의 : 영어도 하고 한글도 하고 이렇게 하면 안됨. 영어만 하든지 한글만 하든지.
def SU_DL_DEL_STOPWORD(strSent, engmod, kormod):
    try:
        if engmod == 1:     # 영어를 불용어 처리하기 위해서는 토큰화 해야 함. 그렇치 않으면 엉뚱한 결과 초래
            stop_words_list = stopwords.words('english')
            word_tokens = word_tokenize(strSent)
            result = []
            for word in word_tokens:
                if word not in stop_words_list:
                    result.append(word)
            strSent = " ".join(result)

        if kormod == 1:     # todo 거의 이것만 사용하지 않을까 싶다. 한글에 영어가 포함되어 있도 역시 됨
            strSent = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", strSent)       # 특수문자 등 삭제
            strSent = SU_DL_STRLIST_REPLACE(strSent, G_H_STOPWORD, '')          # 불용어 제거

        return strSent
    except:
        pass
    return


############################################################# 문자열에서 리스트에 있는 문자열을 정해진 문자열 또는 공백으로 대체
# strSent : 전처리 대상 문자열
# strList : 불용어 리스트
# strReplace : 불용어를 대체할 문자열. 널이면 ''로 대체 즉 불용어 삭제와 같은 의미
def SU_DL_STRLIST_REPLACE(strSent,strList,strReplace):
    try:
        strList = "|".join(strList)
        p = re.compile(strList)
        if strReplace:
            strSent = p.sub(strReplace,strSent)
        else:
            strSent = p.sub('', strSent)
        return strSent
    except:
        pass
    return

############################################################# konlpy 활용하여 한글 토큰화
# strSent : 전처리 대상 문자열
# strList : 하나로 인식해야 할 문자열 리스트
# 리턴은 토큰화 된 리스트
def SU_DL_STRLIST_OKT(strSent):
    try:
        okt = Okt()
        strSent = okt.morphs(strSent)               # 토큰화 해서 리턴
        return strSent
    except:
        pass
    return

############################################################# ckonlp 활용, 어떠한 문자열은 하나로 인식하라는 것
# strSent : 전처리 대상 문자열
# strList : 하나로 인식해야 할 문자열 리스트
# 리턴은 토큰화 된 리스트
def SU_DL_STRLIST_TWITTER(strSent,strList):
    try:
        if len(strList):
            twitter = Twitter()
            for item in strList:
                twitter.add_dictionary(item,'Noun')     # 먼저 하나의 문자열로 인식할 단어를 등록해주고
        strSent = twitter.morphs(strSent)               # 토큰화 해서 리턴
        return strSent
    except:
        pass
    return


############################################################# 코사인 유사도
# sourcefolder : 입찰공고 파일을 text파일로 뽑아낸 결과물이 있는 폴더. text파일 경로
# pupusfile : 유사도를 구하고자 하는 해당파일(기준파일)
# selcount : 해당파일과 유사도를 구하고자 하는 파일의 개수. 100개 중에 상위 10개만
# 뷸용어 제거(이미 불용어는 제거 됬는데 다른데 활용하기 위해서). 조달이 아니면 불용어 제거를 하는게 낫다. 조달은 이미 함
def SU_DL_COSINE_SIMILARITY(sourcefolder, pupusfile, selcount):
    df = SU_DL_COSINE_SIMILARITY_DF(sourcefolder)
    
    # 유사도 분석을 컬럼이 Null이면 오류 나지 빈값 적용
    df['fcon'] = df['fcon'].fillna('')
    
    # 일단 영어에 해당하는 불용어 처리(한글로 해야 할 듯. 안해도 상관없을 듯 한데)
    tfidf = TfidfVectorizer(stop_words='english')
    
    # TF-IDF 매트리스 생성
    tfidf_matrix = tfidf.fit_transform(df['fcon'])
    
    # 유사도 매트리스 생성
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    # df = pd.DataFrame(cosine_sim)  # 파일명이 아닌 파일명에 해당하는 인덱스로 유사도가 되어 있는 것을 알수 있다.
    # print(df.head(5))
    
    # 파일명에 해당하는 딕셔너리 생성. 왜냐하면 해당파일명에 내용이 유사한 파일들을 찾기 위해. 인덱스-파일명-파일내용이 하나의 로우값
    file_to_index = dict(zip(df['fname'], df.index))
    
    # 해당파일명에 해당하는 인덱스 구하기. 이 인덱스 유사도 매트릭스의 파일명과 매칭
    idx = file_to_index[pupusfile]
    
    # 유사도 매트리스에서 해당 파일명과 매칭되는 인덱스에 해당되는 유사파일들 리스트
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # 유사도 값으로 소팅
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # 유사한 파일 개수만큼 슬라이싱, 1부터 시작하니 자기건 제외
    sim_scores = sim_scores[1:selcount]

    # 해당되는 파일명을 리턴, sim_scores에는 파일명과 매칭되는 인덱스 번호와 유사도 값만 존재
    simfileindex = [idx[0] for idx in sim_scores]
    
    print(df['fname'][simfileindex])
    
    return

############################################################# 코사인 유사도를 구하기 위해 데이터프레임에 분석자료를 넣는다.
# sourcefolder : 입찰공고 파일을 text파일로 뽑아낸 결과물이 있는 폴더. text파일 경로
# 내용 : 파일명, 파일내용으로 하는 데이터프레임을 만든다. 파일내용이 코사인유사도를 구하는데 활용 됨

def SU_DL_COSINE_SIMILARITY_DF(sourcefolder):
    alist = []
    for file in glob.iglob(sourcefolder + "/**/*", recursive=True):
       if os.path.isfile(file):
            sublist = []
            
            filecontent=psf.SU_MO_TextFileToStr2(file)
            sublist.append(os.path.basename(file))
            sublist.append(filecontent)
           
            alist.append(sublist)           
    df = pd.DataFrame(alist, columns=['fname', 'fcon'])
    return df