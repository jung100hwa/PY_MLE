# 두문장의 차이를 알게 해주는 라이브러리
# 조달쪽에 활용해 보는 것도 괜찮을 듯 함
from diff_match_patch import diff_match_patch

before = "Life is too short, you need python."
after = "Life is short, you need python language."

dmp = diff_match_patch()
diff = dmp.diff_main(before, after)
dmp.diff_cleanupSemantic(diff)

for item in diff:
    print(item)

# 튜플로 리턴, 0-변경없음, -1-삭제, 1-추가됨