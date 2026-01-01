import win32api as win
import win32gui as wingui
from win32api import GetSystemMetrics
# from win32api import GetComputerName
# from win32api import GetUserName
import win32clipboard

# 윈도우 beep 구하기
# x : 주파수(hz 단위, 500주면 됨)
# y : 초(ms 단위) 즉 2초는 2000
def su_mo_win32api_beep(x,y):
    if str(x).isdigit() and str(y).isdigit():
        win.Beep(x, y)



# 마우스 커서 위치 알아내기. 문제는 듀얼 모니터일때 주모니터외 왼쪽에 있으면 -로 인식 함
# 모니터 좌측 상단이 0,0 
# 듀얼모니터일때는 생각하지 말자
def su_mo_win32api_getcursorpos():
    return win.GetCursorPos();



# 화면 해상도 얻기
def su_mo_win32api_getsystemmetrics():
    return (GetSystemMetrics(0), GetSystemMetrics(1))



# x, y 지점의 픽셀 정보 얻기
# condition : 0이면 16진수로 리턴, 1이면 rgb값으로 리턴
# 이 함수는 이미지 라이브러리에도 있네.PIL
def su_mo_wingui_getpixel(x,y,condition=1):
    color = wingui.GetPixel(wingui.GetDC(wingui.GetActiveWindow()), x, y)    
    if condition == 0:
        return hex(color)
    if condition == 1:
        blue = color & 255
        green = (color >> 8) & 255
        red = (color >> 16) & 255
        return (red,green,blue)
  
    
    
# 현재 pc명, 로그인 정보가 아님
def su_mo_winapi_getcomputername():
    return win.GetComputerName()

# 현재 pc 유저명
def su_mo_winapi_getusername():
    return win.GetUserName()

# 클립보드 텍스트 넣기
def su_mo_win32clipboard_set(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()
    
# 클립보드에서 가져오기
# 이함수는 위 텍스트 넣기 함수를 실행하지 않고도 윈도우에서 글씨 복사후 수행해되된다.
def su_mo_win32clipboard_get():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data