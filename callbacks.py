from dash import Input, Output, dash_table
import plotly.express as px
from data import df, prepare_data

def register_callbacks(app):
    @app.callback(
        Output('choropleth-map', 'figure'),
        Input('year-slider', 'value'),
        Input('medal-dropdown', 'value'),
        Input('event-dropdown', 'value')
    )
    def update_map(year_range, selected_medal, selected_event):
        country_medals = prepare_data(year_range[0], year_range[1], selected_medal, selected_event)

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
    
    @app.callback(
        Output('pie-chart', 'figure'),
        Input('year-dropdown', 'value')
    )
    def update_pie_chart(selected_year):
        filtered_df = df[df['year'] == selected_year]
        country_medals = filtered_df.groupby('country').size().reset_index(name='medal_count')

        fig = px.pie(
            country_medals,
            names='country',
            values='medal_count',
            title=f'Medal Distribution by Country in {selected_year}',
        )

        fig.update_traces(
            textinfo='label+percent', 
            textposition='inside', 
            textfont_size=14 
        )

        fig.update_layout(
            height=800,    
            width=1000,         
            margin=dict(t=50, b=50)   
        )

        return fig

    @app.callback(
        Output('winners-table', 'children'),
        Input('pie-chart', 'clickData'),
        Input('year-dropdown', 'value')
    )
    def update_table(click_data, selected_year):
        if click_data:
            country = click_data['points'][0]['label']
            filtered_df = df[(df['year'] == selected_year) & (df['country'] == country) & (df['medal'].notnull())]
            table_data = filtered_df[['athlete', 'sport', 'medal']].to_dict('records')

            return dash_table.DataTable(
                columns=[
                    {'name': 'Athlete', 'id': 'athlete'},
                    {'name': 'Sport', 'id': 'sport'},
                    {'name': 'Medal', 'id': 'medal'}
                ],
                data=table_data,
                sort_action='native',
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left'}
            )
        return "Click on a pie slice to view details."
