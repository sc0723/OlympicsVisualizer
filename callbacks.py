from dash import Input, Output
import plotly.express as px
from data import prepare_data

def register_callbacks(app):
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
