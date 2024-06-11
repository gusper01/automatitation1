import pandas as pd
import plotly.express as px
from jinja2 import Template

# Supongamos que tienes un archivo CSV con los datos procesados
processed_data_path = 'data/processed/financial_data_processed.csv'

# Cargar los datos procesados
df = pd.read_csv(processed_data_path)

# Crear un gráfico con Plotly
fig = px.line(df, x='date', y='returns', title='Financial Data Returns')

# Guardar el gráfico como un archivo HTML
fig.write_html('docs/var_dashboard.html')

# Crear una plantilla HTML básica
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial VaR Dashboard</title>
</head>
<body>
    <h1>Financial VaR Dashboard</h1>
    <div>{{ plot_div }}</div>
</body>
</html>
"""

# Renderizar la plantilla con el gráfico
template = Template(html_template)
html_content = template.render(plot_div=fig.to_html(full_html=False, include_plotlyjs='cdn'))

# Guardar el contenido HTML en el archivo index.html
with open('docs/index.html', 'w') as f:
    f.write(html_content)
