from dash import Dash, dcc, html
from layouts import choropleth_tab, pie_chart_tab
from callbacks import register_callbacks

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Olympic Data Dashboard", style={'textAlign': 'center'}),
    dcc.Tabs([
        dcc.Tab(label='Choropleth Map', children=choropleth_tab),
        dcc.Tab(label='Pie Chart & Winners Table', children=pie_chart_tab)
    ])
])

# Register callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
