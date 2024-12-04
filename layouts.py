from dash import dcc, html
import pandas as pd
from data import df  # Import the dataset

# Layout for the choropleth map tab
choropleth_tab = html.Div([
    html.Label("Select Time Range:"),
    dcc.RangeSlider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        step=4,
        marks={year: str(year) for year in range(df['year'].min(), df['year'].max() + 1, 20)},
        value=[2000, 2020]
    ),
    html.Label("Select Medal Type:"),
    dcc.Dropdown(
        id='medal-dropdown',
        options=[
            {'label': 'All', 'value': 'All'},
            {'label': 'Gold', 'value': 'Gold'},
            {'label': 'Silver', 'value': 'Silver'},
            {'label': 'Bronze', 'value': 'Bronze'}
        ],
        value='All'
    ),
    html.Label("Select Event:"),
    dcc.Dropdown(
        id='event-dropdown',
        options=[
            {'label': 'All', 'value': 'All'}
        ] + [{'label': event, 'value': event} for event in sorted(df['event'].unique())],
        value='All'
    ),
    dcc.Graph(id='choropleth-map')
])

# Layout for example tab
example_tab = html.Div([
    html.P("This tab is for another visualization, like a bar chart or line chart."),
    dcc.Graph(id='example-chart')
])
