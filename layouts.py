from dash import dcc, html
import pandas as pd
from data import df 

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
    dcc.Graph(
        id='choropleth-map',
        style={'width': '100%', 'height': '800px'})
])

pie_chart_tab = html.Div([
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': year, 'value': year} for year in sorted(df['year'].unique())],
            value=df['year'].max()
        ),
    ], style={'margin': '20px'}),

    # Pie Chart
    html.Div(
        dcc.Graph(
            id='pie-chart',
            style={
                'height': '800px',
                'width': '800px',  
            }
        ),
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center', 
            'width': '100%',        
            'margin-bottom': '10px'  
        }
    ),

    # Table for Winners' Details
    html.Div([
        html.H4("Winners' Details:", style={'margin-top': '10px'}), 
        html.Div(id='winners-table')
    ], style={'margin': '0 20px'}) 
])
