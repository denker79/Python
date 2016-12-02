import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(username='f497a852-8f06-4add-a6c8-97c3c5e77f37',password='tQJd2JgF8Nsk', version='2016-05-19')

def analyze(txt):
	return json.dumps(tone_analyzer.tone(text=txt, tones='emotion'), indent=2)
