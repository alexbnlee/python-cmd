# coding=utf-8

from PIL import ImageGrab
from PIL import Image
import pynput, time, os, psutil, pytesseract
from pynput.mouse import Button
from pynput.keyboard import Key
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def autoinput():
	mouse.position=(499, 273)
	mouse.click(Button.left)
	keyboard.press(Key.end)
	keyboard.release(Key.end)
	keyboard.press(Key.shift)
	keyboard.release(Key.shift)
	keyboard.press('.')
	keyboard.press('/')
	keyboard.press('y')
	keyboard.press('l')
	keyboard.press('c')
	keyboard.press('.')
	keyboard.press('s')
	keyboard.press('h')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	keyboard.press(Key.shift)
	keyboard.release(Key.shift)

def autoinput_exit():
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

def savePic():
	pic = ImageGrab.grab(bbox=(175, 299, 719, 701))
	pic.save(r"D:\MODISPRO\Scripts\tmp.jpg")

def getChinese():
	str_chi = ["国", "家" ,"洋" ,"监" ,"测","中", "心"]
	text=pytesseract.image_to_string(Image.open(r'D:\MODISPRO\Scripts\tmp.jpg'),lang='chi_sim')
	for s in str_chi:
		if(text.find(s) > -1):
			return True
	return False

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

time.sleep(240)

for i in range(0, 100):
	savePic()
	if(getChinese()):
		autoinput_exit()
		break
	time.sleep(1)