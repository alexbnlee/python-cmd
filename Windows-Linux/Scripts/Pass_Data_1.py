# coding=utf-8

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

for i in range(0, 100):
	# 获取进程id
	ps = psutil.pids()
	# 判断是否有putty进程，默认只有一个putty
	for pi in ps:
		p = psutil.Process(pi)
		if p.name().find("putty") == 0:
			autoinput()
			# 数据从 Linux机器 → 服务器
			time.sleep(15+i)
			autoinput2()
			exit()
	time.sleep(1)

