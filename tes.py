from control_file import *
from tone_analyze import *
import json

print("Welcome to txt sentiment analyze. \n")
print("This project read a txt file and send to watson to generate a sentimental insight,\n")
print("basically you need to inform the way to txt file and we return to you the percent for each sentiment.\n\n\n\n")

src = input("Please inform txt source: ")

txt = reads(src)

print(txt)

print("\n")

jtxt = json.loads(analyze(txt))

for text in jtxt['document_tone']['tone_categories']:
	for tone in text['tones']:
		print(tone['tone_name'], '=', tone['score']*100,'%\n' )


