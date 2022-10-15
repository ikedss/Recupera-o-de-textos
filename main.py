#Aluno: Leonardo Ikeda

from bs4 import BeautifulSoup
import requests
import spacy

nlp = spacy.load("en_core_web_sm")

html1 = requests.get("https://en.wikipedia.org/wiki/Natural_language_processing")
html2 = requests.get("https://www.ibm.com/cloud/learn/natural-language-processing")
html3 = requests.get("https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html")
html4 = requests.get("https://builtin.com/data-science/high-level-guide-natural-language-processing-techniques")
html5 = requests.get("https://deepsense.ai/a-business-guide-to-natural-language-processing-nlp/")
soup1 = BeautifulSoup(html1.text, "html.parser")
soup2 = BeautifulSoup(html2.text, "html.parser")
soup3 = BeautifulSoup(html3.text, "html.parser")
soup4 = BeautifulSoup(html4.text, "html.parser")
soup5 = BeautifulSoup(html5.text, "html.parser")
#print(soup1.get_text(), soup2.get_text(), soup3.get_text(), soup4.get_text(), soup5.get_text())

doc1 = nlp(soup1.text)
doc2 = nlp(soup2.text)
doc3 = nlp(soup3.text)
doc4 = nlp(soup4.text)
doc5 = nlp(soup5.text)

sentencas1 = []
sentencas2 = []
sentencas3 = []
sentencas4 = []
sentencas5 = []

def get_sentencas(lsentencas, doc):
    contador = 0
    for sentenca in doc.sents:
      lsentencas.append(sentenca.text)
      contador += 1
    return lsentencas

sentencas1 = get_sentencas(sentencas1, doc1)
sentencas2 = get_sentencas(sentencas2, doc2)
sentencas3 = get_sentencas(sentencas3, doc3)
sentencas4 = get_sentencas(sentencas4, doc4)
sentencas5 = get_sentencas(sentencas5, doc5)

print(sentencas1, sentencas2, sentencas3, sentencas4, sentencas5)
