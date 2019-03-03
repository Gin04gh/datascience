import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pylab as plt
from matplotlib.colors import LinearSegmentedColormap
import pystan
#import imgkit
import pickle

"""
def generate_cmap(colors):
    
    values = range(len(colors))
    vmax = np.ceil(np.max(values))
    color_list = []
    
    for v, c in zip(values, colors):
        
        color_list.append(( v/ vmax, c))
        
    return LinearSegmentedColormap.from_list('custom_cmap', color_list)
"""

def main():

  # target player
  arr_target_player = np.array([
    'Roger Federer', 'Rafael Nadal', 'Novak Djokovic',
    'Andy Murray', 'Stanislas Wawrinka', 'Juan Martin Del Potro',
    'Kei Nishikori', 'Tomas Berdych', 'David Ferrer'
  ])

  # target year
  arr_target_year = np.array(list(range(2005, 2017))) # 2005--2016

  # read data
  df_matches = pd.read_csv('./df_matches.csv')

  # create data for stan
  """
  df_tmp = df_matches[
    (df_matches['winner_name'].isin(arr_target_player)) &
    (df_matches['loser_name'].isin(arr_target_player))
  ]
  """
  df_target = df_matches[
    (df_matches['date'] < '2017-03') 
  ]

  dic_target_year = {}

  for year in arr_target_year:
    if year not in dic_target_year:
      dic_target_year[year] = len(dic_target_year)+1

  dic_target_player = {}

  for player in arr_target_player:
    if player not in dic_target_player:
      dic_target_player[player] = len(dic_target_player)+1

  LW = []
  GY = []

  for year in arr_target_year:
    for player_a in arr_target_player:
      for player_b in arr_target_player:
        
        df_tmp = df_target[
          (df_target['winner_name'] == player_a) &
          (df_target['loser_name'] == player_b)
        ]
        
        for _ in range(len(df_tmp)):
            
          LW.append([dic_target_player[player_b], dic_target_player[player_a]])
          GY.append(dic_target_year[year])
            
        df_tmp = df_target[
          (df_target['winner_name'] == player_b) &
          (df_target['loser_name'] == player_a)
        ]
        
        for _ in range(len(df_tmp)):
            
          LW.append([dic_target_player[player_a], dic_target_player[player_b]])
          GY.append(dic_target_year[year])

  LW = np.array(LW, dtype=np.int32)
  GY = np.array(GY, dtype=np.int32)

  # estimate
  model = ''
  with open('./model_strength_ts.stan') as f:
    model = f.read()
  data = {
    'N': len(dic_target_player),
    'G': len(LW),
    'Y': len(dic_target_year),
    'GY': GY,
    'LW': LW,
  }
  fit = pystan.stan(model_code=model, data=data, iter=5000, chains=4)
  la = fit.extract()

  with open('./ts_result.pickle', mode='wb') as f:
    pickle.dump(la, f)

  # output graphs

  # violinplot strength mu chains


if __name__ == '__main__':
  main()
