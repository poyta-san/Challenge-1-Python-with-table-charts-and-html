import base64
from io import BytesIO
import json
from flask import Flask
import matplotlib.pyplot as plt

with open("dados.json") as f:
    data = json.load(f)
# print(df)

print(data)

for item in data:
    item["GGR"] = item["apostas"] - item["ganhos"]
# print(data)
table_row = ""
for item in data:

    table_row = (
        table_row
        + """<tr><td>"""
        + item["mes"]
        + """</td><td>"""
        + str(item["ativos"])
        + """</td><td>"""
        + str(item["apostas"])
        + """</td><td>"""
        + str(item["ganhos"])
        + """</td><td>"""
        + str(item["GGR"])
        + """</td></tr>"""
    )

print(table_row)

# print([item["mes"] for item in data])

xAxis = []
for item in data:
    xAxis.append(item["mes"])
yAxis = []
for item in data:
    yAxis.append(item["ativos"])
    yAxis2 = []
for item in data:
    yAxis2.append(item["apostas"])
yAxis3 = []
for item in data:
    yAxis3.append(item["ganhos"])
yAxis4 = []
for item in data:
    yAxis4.append(item["GGR"])
    
plt.grid(True)

## LINE GRAPH ##
fig = plt.figure()

plt.plot(xAxis, yAxis, color="maroon", marker="o", label="ativos")
plt.plot(xAxis, yAxis2, color="blue", marker="o", label="apostas")
plt.plot(xAxis, yAxis3, color="green", marker="o", label="ganhos")
plt.plot(xAxis, yAxis4, color="yellow", marker="o", label="GGR")
plt.legend(loc="upper left")
plt.xlabel("Datas")
plt.ylabel("Valores")
plt.title("Análise dos jogos")
plt.grid()

tmpfile = BytesIO()
fig.savefig(tmpfile, format="png")
encoded = base64.b64encode(tmpfile.getvalue()).decode("utf-8")

html = "<img src='data:image/png;base64,{}'>".format(encoded)

# plt.show()

buf = BytesIO()
fig.savefig(buf, format="png")
# Embed the result in the html output.
imagedata = base64.b64encode(buf.getbuffer()).decode("ascii")

app = Flask(__name__)

t = (
    """<html>
    <style>
    table, th, td {
      border:1px solid black;
    }
    </style>
    <body>
    <table>
    <tr>
    <th>mes</th>
    <th>ativos</th>
    <th>apostas</th>
    <th>ganhos</th>
    <th>GGR</th>
    </tr>"""
    + table_row
    + """
    </table>
    """
    + html
    + """
    </body>
    </html>"""
)

@app.route("/")
def data_analysis_normal():
    return t

# pip install black
# black data_analysis_normal.py
# flask --app data_analysis_normal run