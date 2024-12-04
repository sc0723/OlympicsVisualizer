# import pandas as pd
# import plotly.express as px
# from dash import Dash, dcc, html, Input, Output

# # Load the datasets
# df = pd.read_csv("data/Olympic_Athlete_Event_Details.csv")
# country_df = pd.read_csv("data/Olympic_Country_Profiles.csv")

# # Helper functions
# def extract_year(full_event):
#     return int(full_event[0:4])

# def prepare_data(start_year, end_year, medal_type, event):
#     filtered_df = df[(df['year'] >= start_year) &
#                      (df['year'] <= end_year)]
#     if medal_type != "All":
#         filtered_df = filtered_df[filtered_df['medal'] == medal_type]

#     if event != "All":
#         filtered_df = filtered_df[filtered_df['event'] == event]

#     country_medals = filtered_df.groupby('country').size().reset_index(name='medal_count')
#     return country_medals

# def add_columns():
#     df['year'] = df['edition'].apply(extract_year)
#     country_dict = dict(zip(country_df['noc'], country_df['country']))
#     df['country'] = df['country_noc'].map(country_dict)

# add_columns()

# # Initialize the app
# app = Dash(__name__)

# # App layout with tabs
# app.layout = html.Div([
#     html.H1("Olympic Data Dashboard", style={'textAlign': 'center'}),
    
#     dcc.Tabs([
#         # Tab 1: Choropleth Map
#         dcc.Tab(label='Choropleth Map', children=[
#             html.Div([
#                 html.Label("Select Time Range:"),
#                 dcc.RangeSlider(
#                     id='year-slider',
#                     min=df['year'].min(),
#                     max=df['year'].max(),
#                     step=4,
#                     marks={year: str(year) for year in range(df['year'].min(), df['year'].max() + 1, 20)},
#                     value=[2000, 2020]
#                 ),
#             ], style={'margin': '20px'}),

#             html.Div([
#                 html.Label("Select Medal Type:"),
#                 dcc.Dropdown(
#                     id='medal-dropdown',
#                     options=[
#                         {'label': 'All', 'value': 'All'},
#                         {'label': 'Gold', 'value': 'Gold'},
#                         {'label': 'Silver', 'value': 'Silver'},
#                         {'label': 'Bronze', 'value': 'Bronze'}
#                     ],
#                     value='All'
#                 ),
#             ], style={'margin': '20px'}),

#             html.Div([
#                 html.Label("Select Event:"),
#                 dcc.Dropdown(
#                     id='event-dropdown',
#                     options=[
#                         {'label': 'All', 'value': 'All'}
#                     ] + [{'label': event, 'value': event} for event in sorted(df['event'].unique())],
#                     value='All'
#                 ),
#             ], style={'margin': '20px'}),

#             dcc.Graph(id='choropleth-map')
#         ]),

#         # Tab 2: Example Placeholder Visualization
#         dcc.Tab(label='Placeholder Visualization', children=[
#             html.Div([
#                 html.P("This tab is for another visualization, like a bar chart or line chart."),
#                 dcc.Graph(id='example-chart', figure=px.line(x=[1, 2, 3], y=[1, 4, 9], title="Example Chart"))
#             ], style={'margin': '20px'})
#         ])
#     ])
# ])

# # Callback for updating the choropleth map
# @app.callback(
#     Output('choropleth-map', 'figure'),
#     Input('year-slider', 'value'),
#     Input('medal-dropdown', 'value'),
#     Input('event-dropdown', 'value')
# )
# def update_map(year_range, selected_medal, selected_event):
#     # Prepare the filtered data
#     country_medals = prepare_data(year_range[0], year_range[1], selected_medal, selected_event)
    
#     # Generate the choropleth map
#     fig = px.choropleth(
#         country_medals,
#         locations='country',
#         locationmode='country names',
#         color='medal_count',
#         color_continuous_scale='Viridis',
#         title='Olympic Medal Counts by Country',
#         labels={'medal_count': 'Medals'}
#     )
#     fig.update_geos(showframe=False, projection_type="equirectangular")
#     return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)



