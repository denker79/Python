import json
from bolha import ordena

ordena(22)
from watson_developer_cloud import LanguageTranslationV2 as LanguageTranslation

lang = LanguageTranslation(username='c045509f-30d3-4708-8459-02a446ba27f2', password='b4EBjQtEIMtr')

def translate():
	translation = lang.translate(text='hello', source='en', target='es')
	print(json.dumps(translation, indent=2, ensure_ascii=False))