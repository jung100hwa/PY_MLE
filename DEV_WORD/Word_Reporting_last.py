'''
:word 파일 기본템플릿에 값을 적어 넣기
:활용 : 대장출력, 조달제안서 작성 등
'''

import sys
sys.path.append("c:\\work\\PLangVim")

from PY_PKG.SU_WORD_WRITE import WordReplace

def main():
    replace_hdict = {
        "[H01]":"김철수",
        "[H02]":"chemp",
        "[H03]" : "2022.12.31"
        }
    replace_idict = {
        "[I01]": "서명파일.jpg",
    }

    replace_tdict = {
        "[T01]": "01",
        "[T02]": "AAA",
        "[T03]": "BBB",
        "[T04]": "CCC",
        "[T05]": "DDD",
    }

    replace_tdict2 = [
        {
        "[T01]": "01",
        "[T02]": "AAA",
        "[T03]": "BBB",
        "[T04]": "CCC",
        "[T05]": "DDD"
        },
        {
        "[T001]": "001",
        "[T002]": "AAAA",
        "[T003]": "BBBB",
        "[T004]": "CCCC",
        "[T005]": "DDDD"
        }
    ]
    
    
    g_sourcedir = "C:\\work\\PLangVim\\DEV_WORD\\"
    g_tagetdir  = "c:\\work\\PLangVim\\DEV_WORD\\result\\"

    # Call processing section
    for i, file in enumerate(WordReplace.docx_list(g_sourcedir),start=1):
        wordreplace = WordReplace(file)
        # wordreplace.header_content(replace_dict)
        # wordreplace.header_tables(replace_dict)
        # wordreplace.body_content(replace_hdict)
        # wordreplace.body_tables(replace_tdict)
        # wordreplace.body_tables_list(replace_tdict2)
        wordreplace.body_tables(replace_idict,1,3,2)
        # wordreplace.footer_content(replace_dict)
        # wordreplace.footer_tables(replace_dict)
        
        # target 디렉토리에 동일명으로 저장
        file = g_tagetdir + file.replace(g_sourcedir,'')
        wordreplace.save(file)


if __name__ == "__main__":
    main()
    print("리포팅 완료")