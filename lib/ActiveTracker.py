import psutil
import win32gui
import win32process

while 1:  # 死循环，未调整，能够读取系统当前聚焦的窗口所对应的进程
    def active_window_process_name():
        try:
            pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
            return psutil.Process(pid[-1]).name()
        except:
            pass


    print(active_window_process_name())
