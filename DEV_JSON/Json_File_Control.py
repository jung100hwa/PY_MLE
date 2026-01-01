import json
import SU_Init as SU_Init

# 데이터베이스 연결하지 않음
SU_Init.SU_MO_VarInit(1)


with open(SU_Init.G_SU_ExFilePosIn + "stone.json", "r", encoding="UTF-8") as f:
    json_data = json.load(f)

# ensure_ascii = False가 없으면 한글이 제대로 출력되지 않음
# indent="\t" 이것은 제이슨 형식에 맞게 보기 좋게 출력
print(json.dumps(json_data, indent="\t", ensure_ascii=False))

# 키별도 출력
# for onekey in json_data.keys():
#     if type(json_data[onekey]) is list:
#         for twoitem in json_data[onekey]:
#             print(twoitem)
