import cv2

video_file = "../img/big_buck.avi" # 동영상 파일 경로

blue = (255, 0, 0)
font =  cv2.FONT_HERSHEY_PLAIN
cFrame = 1

cap = cv2.VideoCapture(video_file) # 동영상 캡쳐 객체 생성  ---①
if cap.isOpened():                 # 캡쳐 객체 초기화 확인
    
    fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임을 의미. 때문에 영상이 23초 짜리이면 전체 프레임은 24 x 23 = 552 정도 됨
    
    while True:
        ret, img = cap.read()      # 다음 프레임 읽기      --- ②
        if ret:                    # 프레임 읽기 정상
            
            # 이미지에 글자 합성하기
            img = cv2.putText(img, "Total Frame : "+ str(fps) + "     Current Frame : "+str(cFrame), (40, 40), font, 2, blue, 3, cv2.LINE_AA)
            
            cv2.imshow(video_file, img) # 화면에 표시  --- ③
            cv2.waitKey(5)              # 25ms 지연(40fps로 가정)   --- ④
        else:                           # 다음 프레임 읽을 수 없슴,
            break                       # 재생 완료
        
        cFrame = cFrame + 1
else:
    print("can't open video.")      # 캡쳐 객체 초기화 실패
cap.release()                       # 캡쳐 자원 반납
cv2.destroyAllWindows()