import numpy as np

f = open('languages.txt','r',encoding='utf-8')
tekst = f.read()
tekst = [t for t in tekst.split()]

lang = [l for i,l in enumerate(tekst) if i%2==0]
rat = [float(r) for i,r in enumerate(tekst) if i%2!=0]

import matplotlib.pyplot as plt

x = range(len(lang))
plt.figure(figsize=(12,10))
plt.bar(x,rat,color='peru',edgecolor='saddlebrown')
plt.xticks(x,lang,rotation=25)
plt.ylabel('Popularność [%]',fontsize=14)
plt.title('Najpopularniejsze języki programowania',fontsize=23)
plt.show()
