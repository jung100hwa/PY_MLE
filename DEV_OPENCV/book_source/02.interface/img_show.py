
import cv2

img_file = "../img/girl.jpg" # 표시할 이미지 경로            ---①
img = cv2.imread(img_file, cv2.IMREAD_COLOR)  # 이미지를 읽어서 img 변수에 할당 ---②
# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
  cv2.imshow('winodw title - IMG', img)   # 읽은 이미지를 화면에 표시      --- ③
  cv2.waitKey()           # 키가 입력될 때 까지 대기      --- ④
  cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤
else:
    print('No image file.')
    