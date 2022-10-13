#Aluno: Leonardo Ikeda

from bs4 import BeautifulSoup
import requests

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
print(soup1.get_text(), soup2.get_text(), soup3.get_text(), soup4.get_text(), soup5.get_text())

sentenca = ""

sentencas1 = []
sentencas2 = []
sentencas3 = []
sentencas4 = []
sentencas5 = []


def get_sentencas(lsentencas, soup):
    contador = 0
    for sentenca in soup.find_all("p"):
        lsentencas.append(sentenca.get_text())
        print(sentenca.get_text())
        contador += 1
    return lsentencas


sentencas1 = get_sentencas(sentencas1, soup1)
sentencas2 = get_sentencas(sentencas2, soup2)
sentencas3 = get_sentencas(sentencas3, soup3)
sentencas4 = get_sentencas(sentencas4, soup4)
sentencas5 = get_sentencas(sentencas5, soup5)

print(sentencas1, sentencas2, sentencas3, sentencas4, sentencas5)
