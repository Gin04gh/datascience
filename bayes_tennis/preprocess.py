import numpy as np
import pandas as pd

def main():

  years = list(range(2005,2018)) # use 2005--2017 data
  df_matches = pd.concat([pd.read_csv('../tennis_atp/atp_matches_'+str(y)+'.csv', usecols=[5,10,20]) for y in years]) # 5: tourney_date, 10: winner_name, 20: loser_name
  df_matches = df_matches.dropna(subset=['tourney_date'])
  df_matches['year'] = df_matches['tourney_date'].apply(lambda x: int(str(x)[0:4]))
  df_matches['date'] = pd.to_datetime(df_matches['tourney_date'].apply(lambda x: str(x)[0:8]))
  df_matches[df_matches['date'] < '2017-03']
  df_matches = df_matches[['year', 'winner_name', 'loser_name']]
  df_matches.to_csv('./df_matches.csv', header=True, index=False)

if __name__ == '__main__':
  main()
