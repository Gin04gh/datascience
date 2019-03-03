import numpy as np
import pandas as pd

def main():

  #years = list(map(str, list(range(2000, 2017+1, 1)))) # use data 2000--2017
  years = list(range(2005,2018)) # use data 2005--2017
  df_matches = pd.concat([pd.read_csv('../tennis_atp/atp_matches_'+str(y)+'.csv', usecols=[5,10,20]) for y in years]) # 5: tourney_date, 10: winner_name, 20: loser_name
  df_matches = df_matches.dropna(subset=['tourney_date'])
  df_matches['date'] = pd.to_datetime(df_matches['tourney_date'].apply(lambda x: str(x)[0:8]))
  #df_matches['year'] = df_matches['tourney_date'].apply(lambda x: int(str(x)[0:4]))
  #df_matches['month'] = df_matches['tourney_date'].apply(lambda x: int(str(x)[4:6]))
  #df_matches['day'] = df_matches['tourney_date'].apply(lambda x: int(str(x)[6:8]))
  #df_matches = df_matches[['year', 'month', 'day', 'winner_name', 'loser_name']]
  df_matches = df_matches[['date', 'winner_name', 'loser_name']]
  df_matches.to_csv('./df_matches.csv', header=True, index=False)

if __name__ == '__main__':
  main()
