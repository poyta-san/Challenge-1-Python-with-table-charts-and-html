import base64
import io
import pandas as pd
from flask import Flask
import matplotlib.pyplot as plt

# Carrega e converte o json em dataframe
df = pd.read_json('dados.json')
# print(df)

# Faz o calculo em cima das colunas existentes e retorna em uma nova coluna
df['GGR'] = df['apostas'] - df['ganhos']
df['RTP(%)'] = (df['ganhos'] / df['apostas']) * 100
# print(df)

# Converte o dataframe para impressão da tabela em HTML
html1 = df.to_html()

app = Flask(__name__)

# Geração do gráfico 1
fig = plt.figure(num=1)
df.plot(x="mes", y=["apostas", "ganhos", "GGR"])
plt.xlabel('Datas')
plt.ylabel('Valores')
plt.title('Análise dos jogos')
plt.grid()

# Exportação do gráfico para html
img = io.BytesIO()
plt.savefig(img, format="png")
data2 = base64.b64encode(img.getbuffer()).decode("ascii")
html2 = f"<img src='data:image/png;base64,{data2}'/>"

# Geração do gráfico 2
fig = plt.figure(num=2)
df.plot(x="mes", y=["ativos"])
plt.xlabel('Datas')
plt.ylabel('Valores')
plt.title('Análise ativos')
plt.grid()

# Exportação do gráfico para html
img2 = io.BytesIO()
plt.savefig(img2, format="png")
data3 = base64.b64encode(img2.getbuffer()).decode("ascii")
html3 = f"<img src='data:image/png;base64,{data3}'/>"

# Geração do gráfico 3
fig = plt.figure(num=3)
df.plot(x="mes", y=["RTP(%)"])
plt.xlabel('Datas')
plt.ylabel('Valores')
plt.title('Análise RTP(%)')
plt.grid()

# Exportação do gráfico para html
img3 = io.BytesIO()
plt.savefig(img3, format="png")
data4 = base64.b64encode(img3.getbuffer()).decode("ascii")
html4 = f"<img src='data:image/png;base64,{data4}'/>"

# plt.show()

# Montagem do HTML com as variáveis
page = '''<html>
    <body>
    ''' + html1 + '''
    ''' + html2 + '''
    <p>''' + html3 + '''</p>
    <p>''' + html4 + '''</p>
    </body>
    </html>'''

@app.route("/")
def data_analysis_pandas():
    
    return page

# pip install black
# black data_analysis_pandas.py
# flask --app data_analysis_pandas run