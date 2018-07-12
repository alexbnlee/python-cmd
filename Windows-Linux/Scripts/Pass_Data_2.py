# coding=utf-8
# 屏幕复制

import pynput, time, os, psutil
from pynput.mouse import Button
from pynput.keyboard import Key
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def autoinput():
	mouse.position=(499, 273)
	mouse.click(Button.left)
	# 用来切换输入法，我电脑默认中文
	keyboard.press(Key.shift)
	keyboard.release(Key.shift)
	keyboard.press('p')
	keyboard.press('a')
	keyboard.press('s')	
	# 一样的按键不用release会显示一个按键
	keyboard.release('s')
	keyboard.press('s')
	keyboard.press('.')
	keyboard.press('s')
	keyboard.press('h')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	# 再把输入法切换回来
	keyboard.press(Key.shift)
	keyboard.release(Key.shift)

def autoinput2():
	mouse.position=(499, 273)
	mouse.click(Button.left)
	# 用来切换输入法，我电脑默认中文
	keyboard.press(Key.shift)
	keyboard.release(Key.shift)
	keyboard.press('e')
	keyboard.press('x')
	keyboard.press('i')	
	keyboard.press('t')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	# 再把输入法切换回来
	keyboard.press(Key.shift)
	keyboard.release(Key.shift)

def copynode():
	mouse.position=(499, 273)
	mouse.press(Button.left)
	mouse.position=(499,573)
	with keyboard.pressed(Key.ctrl):
		keyboard.press('x')
		keyboard.release('x')
	mouse.release(Button.left)

def getClipboard():
	"返回剪贴板上的内容"
	from tkinter import Tk
	r = Tk()
	r.withdraw()
	tmp = r.clipboard_get()
	r.destroy()
	return tmp

flag = 0
for i in range(0, 100):
	# 获取进程id
	ps = psutil.pids()
	# 判断是否有putty进程，默认只有一个putty
	for pi in ps:
		p = psutil.Process(pi)
		if p.name().find("putty") == 0:
			autoinput()
			flag = 1
			break
	if(flag):
		break
	time.sleep(1)

time.sleep(8)

for i in range(0, 10):
	copynode()
	str_clip = getClipboard()
	if(str_clip.find("数据复制完成") > -1):
		autoinput2()
		break
	time.sleep(2)

