import sys
import win32api
import win32gui
import win32con
import win32com.client
from threading import Timer


MAIN_HWND = 0
count_label = 0

def is_win_ok(hwnd, starttext):
    s = win32gui.GetWindowText(hwnd)
    if s.startswith(starttext):
        print(s)
        global MAIN_HWND
        MAIN_HWND = hwnd
        return None
    return 1

def find_main_window(starttxt):
    global MAIN_HWND
    win32gui.EnumChildWindows(0, is_win_ok, starttxt)
    return MAIN_HWND

def winfun(hwnd, lparam):
    s = win32gui.GetWindowText(hwnd)
    global count_label
    if len(s) < 4 and s != 'ОК':
        print("winfun, child_hwnd: %d   txt: %s" % (hwnd, s))
        if count_label == 0:
            win32api.SendMessage(hwnd, win32con.WM_SETTEXT, 0, "user")
            count_label = 1
        else:
            win32api.SendMessage(hwnd, win32con.WM_SETTEXT, 0, "11111111")
            count_label = 0
    if  s == 'ОК':
        print(s,hwnd)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)

    return 1

def main():
    main_app = 'Система безопасности'
    hwnd = win32gui.FindWindow(None, main_app)
    hwnd1 = win32gui.FindWindow(None,'C:\Windows\py.exe')
    win32gui.ShowWindow(hwnd1, win32con.SW_MINIMIZE)
    print(hwnd1)
    print(hwnd)
    if hwnd < 1:
        hwnd = find_main_window(main_app)
    print(hwnd)
    if hwnd:
        win32gui.EnumChildWindows(hwnd, winfun, None)
    Timer(3, main).start()

main()






    

