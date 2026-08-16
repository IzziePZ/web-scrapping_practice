import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna({
        'season': 0,
        'team': 'Unknown',
        'wins': 0,
        'losses': 0,
        'win_pct': 0.0,
        'goals_favor': 0,
        'goals_against': 0,
        'goal_diff': 0
    })

    # Convert data typesﬁ
    df['season'] = df['season'].astype(int)
    df['wins'] = df['wins'].astype(int)
    df['losses'] = df['losses'].astype(int)
    df['win_pct'] = df['win_pct'].astype(float)
    df['goals_favor'] = df['goals_favor'].astype(int)
    df['goals_against'] = df['goals_against'].astype(int)
    df['goal_diff'] = df['goal_diff'].astype(int)

    return df

df = pd.read_csv('nhl_teams_data.csv')
df = clean_data(df)

print(df.head())

