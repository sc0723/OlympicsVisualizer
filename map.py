import pandas as pd

df = pd.read_csv("Olympic_Athlete_Event_Details.csv")

## Create a new 'Year' column to make it easier to filter range
def extract_year(full_event):
    return int(full_event[0:4])

def prepare_data(start_year, end_year, medal_type, event):
    filtered_df = df[(df['year'] >= start_year) &
                     (df['year'] <= end_year) &
                     (df['medal'] == medal_type) &
                     (df['event'] == event)]
    
    


df['year'] = df['edition'].apply(extract_year)



print(df)

