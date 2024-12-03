import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("Olympic_Athlete_Event_Details.csv")
country_df = pd.read_csv("Olympic_Country_Profiles.csv")

def extract_year(full_event):
    return int(full_event[0:4])

def prepare_data(start_year, end_year, medal_type, event):
    filtered_df = df[(df['year'] >= start_year) &
                     (df['year'] <= end_year) &
                     (df['medal'] == medal_type)]
    if event != "All":
        filtered_df = filtered_df[filtered_df['event'] == event]

    country_medals = filtered_df.groupby('country').size().reset_index(name='medal_count')
    return country_medals

def add_columns():
    df['year'] = df['edition'].apply(extract_year)
    country_dict = dict(zip(country_df['noc'], country_df['country']))
    df['country'] = df['country_noc'].map(country_dict)

add_columns()

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Olympic Medals by Country", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Select Time Range:"),
        dcc.RangeSlider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            step=4,
            marks={year: str(year) for year in range(df['year'].min(), df['year'].max() + 1, 20)},
            value=[2000, 2020]
        ),
    ], style={'margin': '20px'}),

    html.Div([
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
    ], style={'margin': '20px'}),

    html.Div([
        html.Label("Select Event:"),
        dcc.Dropdown(
            id='event-dropdown',
            options=[
                {'label': 'All', 'value': 'All'}
            ] + [{'label': event, 'value': event} for event in sorted(df['event'].unique())],
            value='All'
        ),
    ], style={'margin': '20px'}),

    dcc.Graph(id='choropleth-map')
])

# Callback for updating the map
@app.callback(
    Output('choropleth-map', 'figure'),
    Input('year-slider', 'value'),
    Input('medal-dropdown', 'value'),
    Input('event-dropdown', 'value')
)

def update_map(year_range, selected_medal, selected_event):
    # Prepare the filtered data
    country_medals = prepare_data(year_range[0], year_range[1], selected_medal, selected_event)
    
    # Generate the choropleth map
    fig = px.choropleth(
        country_medals,
        locations='country',
        locationmode='country names',
        color='medal_count',
        color_continuous_scale='Viridis',
        title='Olympic Medal Counts by Country',
        labels={'medal_count': 'Medals'}
    )
    fig.update_geos(showframe=False, projection_type="equirectangular")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

