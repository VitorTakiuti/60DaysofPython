# pip install plotly

import plotly.graph_objects as go

# 1 first Example:
dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado' ]
acessos = [100, 50, 40, 70, 80, 90, 200]

fig = go.Figure()

# Build a interative graphic using the data above
fig.add_trace(go.Scatter(x=dias, y=acessos, mode='lines+markers', name='Número de Acessos por dia na Semana'))
fig.show()

# 2 Second Example:
paginas =['Home', 'Contato', 'Blog', 'Sobre']
acessos2 = [100, 200, 40, 70]

fig2 = go.Figure([go.Bar(x=paginas, y=acessos2)])

fig2.update_layout(title='Número de Acessos em cada Página', xaxis_title='Páginas', yaxis_title='Número de Acessos')
fig2.show()