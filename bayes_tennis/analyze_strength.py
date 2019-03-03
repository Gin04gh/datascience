import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pylab as plt
from matplotlib.colors import LinearSegmentedColormap
import pystan
#import imgkit
#import pickle

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
    'Roger Federer', 'Rafael Nadal', 'Novak Djokovic', 'Andy Murray', 'Stanislas Wawrinka', 'Juan Martin Del Potro',
    'Milos Raonic', 'Kei Nishikori', 'Gael Monfils', 'Tomas Berdych', 'Jo Wilfried Tsonga', 'David Ferrer',
    'Richard Gasquet', 'Marin Cilic', 'Grigor Dimitrov', 'Dominic Thiem', 'Nick Kyrgios', 'Alexander Zverev'
  ])

  # read data
  df_matches = pd.read_csv('./df_matches.csv')

  # create data for stan
  """
  df_tmp = df_matches[
    #(df_matches['year'] >= 2015) &
    (df_matches['date'] >= '2015') &
    (df_matches['date'] < '2017-03') & 
    (df_matches['winner_name'].isin(arr_target_player)) &
    (df_matches['loser_name'].isin(arr_target_player))
  ]
  """
  df_target = df_matches[
    (df_matches['date'] >= '2015') &
    (df_matches['date'] < '2017-03') 
  ]

  dic_target_player = {}

  for player in arr_target_player:
    if player not in dic_target_player:
      dic_target_player[player] = len(dic_target_player)+1

  LW = []

  for player_a in arr_target_player:
    for player_b in arr_target_player:
        
      df_tmp = df_target[
        (df_target['winner_name'] == player_a) &
        (df_target['loser_name'] == player_b)
      ]
        
      for _ in range(len(df_tmp)):
    
        LW.append([dic_target_player[player_b], dic_target_player[player_a]])
            
      df_tmp = df_target[
        (df_target['winner_name'] == player_b) &
        (df_target['loser_name'] == player_a)
      ]
      
      for _ in range(len(df_tmp)):
            
        LW.append([dic_target_player[player_a], dic_target_player[player_b]])

  LW = np.array(LW, dtype=np.int32)
  
  # estimate
  model = ''
  with open('./model_strength.stan') as f:
    model = f.read()

  fit = pystan.stan(model_code=model, data={'N': len(dic_target_player), 'G': len(LW), 'LW': LW}, iter=1000, chains=4)
  la = fit.extract()
  
  # output graphs

  # violinplot strength mu chains

  plt.figure(figsize=(10,5))

  colors = ['red', 'yellow', 'green', 'blue']

  for i, player in enumerate(arr_target_player):
    for j in range(4):
      g = plt.violinplot(la['mu'][j*500:(j+1)*500, i], positions=[i], showmeans=False, showextrema=False, showmedians=False)
    
      for pc in g['bodies']:
        pc.set_facecolor(colors[j])
    
  plt.legend(['chain 1', 'chain 2', 'chain 3', 'chain 4'])

  plt.xticks(list(range(len(arr_target_player))), arr_target_player)
  plt.xticks(rotation=45)

  plt.xlabel('player')
  plt.ylabel('mu')
  plt.savefig('./graphs/strength_mu_chains.png', bbox_inches='tight')

  # violinplot strength s_pf chains

  plt.figure(figsize=(10,5))

  colors = ['red', 'yellow', 'green', 'blue']

  for i, player in enumerate(arr_target_player):
    for j in range(4):
    
      g = plt.violinplot(la['s_pf'][j*500:(j+1)*500, i], positions=[i], showmeans=False, showextrema=False, showmedians=False)
    
      for pc in g['bodies']:
        
        pc.set_facecolor(colors[j])
    
  plt.legend(['chain 1', 'chain 2', 'chain 3', 'chain 4'])

  plt.xticks(list(range(len(arr_target_player))), arr_target_player)
  plt.xticks(rotation=45)

  plt.xlabel('player')
  plt.ylabel('s_pf')
  plt.savefig('./graphs/strength_s_pf_chains.png', bbox_inches='tight')

  # violinplot strength mu

  plt.figure(figsize=(10,5))
  cmap = matplotlib.cm.get_cmap('tab10')

  for i, player in enumerate(arr_target_player):

    g = plt.violinplot(la['mu'][:, i], positions=[i], showmeans=False, showextrema=True, showmedians=True)
    c = cmap(i%10)
    
    for pc in g['bodies']:
        
      pc.set_facecolor(c)
        
    g['cbars'].set_edgecolor(c)
    g['cmaxes'].set_edgecolor(c)
    g['cmedians'].set_edgecolor(c)
    g['cmins'].set_edgecolor(c)
    
  plt.xticks(list(range(len(arr_target_player))), arr_target_player)
  plt.xticks(rotation=45)

  plt.xlabel('player')
  plt.ylabel('latent strength')
  plt.savefig('./graphs/strength_mu.png', bbox_inches='tight')

  # table strength mu
  """
  cm = generate_cmap(['white', 'violet'])

  summary = np.zeros((len(arr_target_player), 4))

  for i, player in enumerate(arr_target_player):
    
    samples = la['mu'][:, i]

    median = np.median(samples, axis=0)
    std = np.std(samples, ddof=1)
    lower, upper = np.percentile(samples, q=[25.0, 75.0], axis=0)
    
    summary[i] = [median, std, lower, upper]
    
  summary = pd.DataFrame(summary, index=arr_target_player, columns=['median', 'std', '25%', '75%'])
  summary.style.background_gradient(cmap=cm, axis=0)
  with open('./graphs/strength_mu_tb.pickle', mode='wb') as f:
    pickle.dump(summary, f)
  #html = summary.render()
  #imgkit.from_string(html, './graphs/strength_mu_tb.png')
  """

  # violinplot strength s_pf

  plt.figure(figsize=(10,5))
  cmap = matplotlib.cm.get_cmap('tab10')

  for i, player in enumerate(arr_target_player):
    
    g = plt.violinplot(la['s_pf'][:, i], positions=[i], showmeans=False, showextrema=True, showmedians=True)
    c = cmap(i%10)
    
    for pc in g['bodies']:
        
      pc.set_facecolor(c)
        
    g['cbars'].set_edgecolor(c)
    g['cmaxes'].set_edgecolor(c)
    g['cmedians'].set_edgecolor(c)
    g['cmins'].set_edgecolor(c)
    
  plt.xticks(list(range(len(arr_target_player))), arr_target_player)
  plt.xticks(rotation=45)

  plt.xlabel('player')
  plt.ylabel('uneven performance')
  plt.savefig('./graphs/strength_s_pf.png', bbox_inches='tight')

  # table strength s_pf

  cm = generate_cmap(['white', 'violet'])

  summary = np.zeros((len(arr_target_player), 4))

  for i, player in enumerate(arr_target_player):
    
    samples = la['s_pf'][:, i]

    median = np.median(samples, axis=0)
    std = np.std(samples, ddof=1)
    lower, upper = np.percentile(samples, q=[25.0, 75.0], axis=0)
    
    summary[i] = [median, std, lower, upper]
    
  summary = pd.DataFrame(summary, index=arr_target_player, columns=['median', 'std', '25%', '75%'])
  summary.style.background_gradient(cmap=cm, axis=0)
  with open('./graphs/strength_s_pf_tb.pickle', mode='wb') as f:
    pickle.dump(summary, f)
  #html = summary.render()
  #imgkit.from_string(html, './graphs/strength_s_pf_tb.png')

  # crostab win-lose

  cm = generate_cmap(['white', 'violet'])

  df_tmp = df_target[
    (df_matches['winner_name'].isin(arr_target_player)) &
    (df_matches['loser_name'].isin(arr_target_player))
  ]

  summary = np.zeros((len(arr_target_player), len(arr_target_player)), dtype=np.int32)

  for i in range(len(arr_target_player)):
    for j in range(i+1, len(arr_target_player)):
        
      summary[i, j] = len(df_tmp[
        (df_tmp['winner_name'] == arr_target_player[i]) &
        (df_tmp['loser_name'] == arr_target_player[j])
      ])
        
      summary[j, i] = len(df_tmp[
        (df_tmp['loser_name'] == arr_target_player[i]) &
        (df_tmp['winner_name'] == arr_target_player[j])
      ])
    
  fig, axs = plt.subplots(figsize=(9, 9))
  im = axs.imshow(summary, cmap=cm, interpolation='nearest')

  axs.grid(False)
  axs.set_xticks(list(range(len(arr_target_player))))
  axs.set_yticks(list(range(len(arr_target_player))))
  axs.set_xticklabels(arr_target_player)
  axs.set_yticklabels(arr_target_player)
  axs.set_ylabel('winner')
  axs.set_xlabel('loser')

  for tick in axs.get_xticklabels():
    tick.set_rotation(75)
    
  for i in range(len(arr_target_player)):
    for j in range(len(arr_target_player)):

      text = axs.text(j, i, summary[i, j], ha='center', va='center', color='black')
        
  fig.tight_layout()
  plt.savefig('./graphs/strength_winlose_crosstab.png', bbox_inches='tight')

if __name__ == '__main__':
  main()
