import pandas as pd

df = pd.read_csv("data/Olympic_Athlete_Event_Details.csv")
country_df = pd.read_csv("data/Olympic_Country_Profiles.csv")

def extract_year(full_event):
    return int(full_event[0:4])

def prepare_data(start_year, end_year, medal_type, event):
    filtered_df = df[(df['year'] >= start_year) &
                     (df['year'] <= end_year)]
    if medal_type != "All":
        filtered_df = filtered_df[filtered_df['medal'] == medal_type]
    if event != "All":
        filtered_df = filtered_df[filtered_df['event'] == event]
    country_medals = filtered_df.groupby('country').size().reset_index(name='medal_count')
    return country_medals

def add_columns():
    df['year'] = df['edition'].apply(extract_year)
    country_dict = dict(zip(country_df['noc'], country_df['country']))
    df['country'] = df['country_noc'].map(country_dict)

add_columns()
