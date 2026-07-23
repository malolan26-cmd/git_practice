import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('gitPractice/fifa_world_cup_2026_player_performance.csv')

df.info()

df_goals_assists_analysis = df[['player_name', 'minutes_played', 'goals', 'assists']]

df_goals_assists_analysis = df_goals_assists_analysis.set_index('player_name')

df_goals_assists_analysis.columns = 'Mins', 'Goals', 'Assists'

df_goals_assists_analysis['Goal Involvements'] = df_goals_assists_analysis['Goals'] + df_goals_assists_analysis['Assists']

print(df_goals_assists_analysis)



