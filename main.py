# Aluno: Leonardo Ikeda

"""
Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de 
linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função 
que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta 
url. Duas condições são importantes:  
a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
1000 palavras.  
b) O texto desta página deverá ser transformado em um array de senteças.  
 
Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca 
Spacy. 
"""

from bs4 import BeautifulSoup
import requests
import spacy

nlp = spacy.load("en_core_web_sm")

def adiciona_site(site, lsentencas):
    html = requests.get(site)
    soap = BeautifulSoup(html.content, 'html.parser')

    for doc in soap.find_all('p'):
        documento = nlp(doc.text)
        for sentenca in documento.sents:
            lsentencas.append(sentenca)
    return lsentencas

lsentencas1 = []
lsentencas2 = []
lsentencas3 = []
lsentencas4 = []
lsentencas5 = []
sentencas1 = adiciona_site("https://en.wikipedia.org/wiki/Natural_language_processing", lsentencas1)
sentencas2 = adiciona_site("https://www.ibm.com/cloud/learn/natural-language-processing", lsentencas2)
sentencas3 = adiciona_site("https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html", lsentencas3)
sentencas4 = adiciona_site("https://builtin.com/data-science/high-level-guide-natural-language-processing-techniques", lsentencas4)
sentencas5 = adiciona_site("https://deepsense.ai/a-business-guide-to-natural-language-processing-nlp/", lsentencas5)

print(lsentencas1, lsentencas2, lsentencas3, lsentencas4, lsentencas5)
