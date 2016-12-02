import io
import subprocess
import os

def reads(src):
	file = io.open(src, mode='r', encoding='utf-8', closefd=True);
	text = file.read()
	file.close()
	return text

def writes(src, text):
	try:
		file = io.open(src, mode='w', encoding='utf-8', closefd=True)
		fle.writelines(text);
		file.close()
		return true
	except IOError:
		return False

def appent_write(src, text):
	txt = reads(src)
	txt.append(txt)
	return writes(src,txt)
