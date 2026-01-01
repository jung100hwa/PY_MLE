# 폴터 모니터링 테스트
import sys
sys.path.append("c:\\work\\PLangVim")

import PY_PKG.SU_WINDOW_API_MO as win

# win.su_mo_win32api_beep(500,1000)
# print(win.su_mo_win32api_getcursorpos())
# print(win.su_mo_win32api_getsystemmetrics())

# aa = 0x2b2b2c
# bb = 255
# cc = aa & bb
# print(cc)

# print(win.su_mo_wingue_getpixel(500, 500))
# print(win.su_mo_wingue_getpixel(500, 500))
# print(win.su_mo_winapi_getcomputername())
# print(win.su_mo_winapi_getusername())

win.su_mo_win32clipboard_set("I Love Min")
print(win.su_mo_win32clipboard_get())
