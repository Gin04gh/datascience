#import os
#import contextlib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
from matplotlib.colors import LinearSegmentedColormap
import pystan
import pickle

SEED = 2019

def generate_cmap(colors):
    
  values = range(len(colors))
  vmax = np.ceil(np.max(values))
  color_list = []  
  for v, c in zip(values, colors):
    color_list.append((v/vmax,c))
        
  return LinearSegmentedColormap.from_list('custom_cmap', color_list)

cm = generate_cmap(['white', 'gray'])

def main():

  # read data
  
  df_matches = pd.read_csv('./df_matches.csv')

  # target player

  arr_target_player = np.array([
    'Roger Federer', 'Rafael Nadal', 'Novak Djokovic', 'Andy Murray', 'Stanislas Wawrinka', 'Juan Martin Del Potro',
    'Milos Raonic', 'Kei Nishikori', 'Gael Monfils', 'Tomas Berdych', 'Jo Wilfried Tsonga', 'David Ferrer',
    'Richard Gasquet', 'Marin Cilic', 'Grigor Dimitrov', 'Dominic Thiem', 'Nick Kyrgios', 'Alexander Zverev'
  ])
  arr_target_player_ja = np.array([
    'R・フェデラー', 'R・ナダル', 'N・ジョコビッチ', 'A・マレー', 'S・ワウリンカ', 'J・M・デル=ポトロ',
    'M・ラオニッチ', '錦織圭', 'G・モンフィス', 'T・ベルディヒ', 'JW・ツォンガ', 'D・フェレール',
    'R・ガスケ', 'M・チリッチ', 'G・ディミトロフ', 'D・ティーム', 'N・キリオス', 'A・ズベレフ'    
  ])

  # create data for modeling

  dic_target_player = {}

  for player in arr_target_player:
    if player not in dic_target_player:
      dic_target_player[player] = len(dic_target_player)+1

  LW = []

  for player_a in arr_target_player:
    for player_b in arr_target_player:
        
      df_tmp = df_matches[
        (df_matches['year'] >= 2015) &
        (df_matches['winner_name'] == player_a) &
        (df_matches['loser_name'] == player_b)
      ]
        
      for _ in range(len(df_tmp)):     
        LW.append([dic_target_player[player_b], dic_target_player[player_a]])
            
      df_tmp = df_matches[
        (df_matches['year'] >= 2015) &
        (df_matches['winner_name'] == player_b) &
        (df_matches['loser_name'] == player_a)
      ]
        
      for _ in range(len(df_tmp)):      
        LW.append([dic_target_player[player_a], dic_target_player[player_b]])

  LW = np.array(LW, dtype=np.int32)

  # estimate

  sm = pystan.StanModel(file='./model_strength.stan')
  fit = sm.sampling(data={'N': len(dic_target_player), 'G': len(LW), 'LW': LW}, iter=1000, chains=4, seed=SEED)
  la = fit.extract()

  with open('./result_strength.pickle', mode='wb') as f:
    pickle.dump(la, f)

  # output graphs

  with open('./result_strength.pickle', mode='rb') as f:
    la = pickle.load(f)

  # violinplot strength mu

  #plt.figure(figsize=(10,5))

  for i, player in enumerate(arr_target_player):

    g = plt.violinplot(la['mu'][:, i], positions=[i], showmeans=False, showextrema=True, showmedians=True)
    
    for pc in g['bodies']:
        pc.set_facecolor('black')

    g['cbars'].set_edgecolor('gray')
    g['cmaxes'].set_edgecolor('black')
    g['cmedians'].set_edgecolor('black')
    g['cmins'].set_edgecolor('black')

  plt.xticks(list(range(len(arr_target_player_ja))), arr_target_player_ja)
  plt.xticks(rotation=75)

  plt.xlabel('プレイヤー')
  plt.ylabel('強さ')
  plt.savefig('./graphs/strength_mu.png', bbox_inches='tight')

  # table strength mu

  summary = np.zeros((len(arr_target_player), 4))

  for i, player in enumerate(arr_target_player):
    
    samples = la['mu'][:, i]
    
    median = np.median(samples, axis=0)
    std = np.std(samples, ddof=1)
    lower, upper = np.percentile(samples, q=[25.0, 75.0], axis=0)
    
    summary[i] = [median, std, lower, upper]
    
  fig, axs = plt.subplots(ncols=4, figsize=(4,8))
  plt.subplots_adjust(wspace=0)

  for i, stat in enumerate(['Median', 'STD', '25%', '75%']):
    
    axs[i].imshow(summary[:, i].reshape(len(arr_target_player), 1), cmap=cm, interpolation='nearest', aspect='auto')

    axs[i].xaxis.tick_top()
    axs[i].set_xticks([0])
    axs[i].set_yticks(list(range(len(arr_target_player))))
    axs[i].set_xticklabels([stat])
    axs[i].tick_params(bottom=False, left=False, right=False, top=False)
    
    if i == 0:
      axs[i].set_yticklabels(arr_target_player_ja)
      axs[i].set_ylabel('プレイヤー')
    else:
      axs[i].set_yticklabels([])
        
    for j in range(len(arr_target_player)):
      axs[i].text(0, j, str(round(summary[j, i], 3)), ha='center', va='center', color='black')
    
  plt.savefig('./graphs/strength_mu_tb.png', bbox_inches='tight')

  # violinplot strength s_pf

  plt.figure(figsize=(10,5))

  for i, player in enumerate(arr_target_player):
    
    g = plt.violinplot(la['s_pf'][:, i], positions=[i], showmeans=False, showextrema=True, showmedians=True)

    for pc in g['bodies']:
      pc.set_facecolor('gray')

    g['cbars'].set_edgecolor('gray')
    g['cmaxes'].set_edgecolor('black')
    g['cmedians'].set_edgecolor('black')
    g['cmins'].set_edgecolor('black')

  plt.xticks(list(range(len(arr_target_player_ja))), arr_target_player_ja)
  plt.xticks(rotation=75)

  plt.xlabel('プレイヤー')
  plt.ylabel('勝負ムラ')
  plt.savefig('./graphs/strength_s_pf.png', bbox_inches='tight')

  # table strength s_pf

  summary = np.zeros((len(arr_target_player), 4))

  for i, player in enumerate(arr_target_player):
    
    samples = la['s_pf'][:, i]
    
    median = np.median(samples, axis=0)
    std = np.std(samples, ddof=1)
    lower, upper = np.percentile(samples, q=[25.0, 75.0], axis=0)

    summary[i] = [median, std, lower, upper]
    
  fig, axs = plt.subplots(ncols=4, figsize=(4,8))
  plt.subplots_adjust(wspace=0)

  for i, stat in enumerate(['Median', 'STD', '25%', '75%']):
    
    axs[i].imshow(summary[:, i].reshape(len(arr_target_player), 1), cmap=cm, interpolation='nearest', aspect='auto')

    axs[i].xaxis.tick_top()
    axs[i].set_xticks([0])
    axs[i].set_yticks(list(range(len(arr_target_player))))
    axs[i].set_xticklabels([stat])
    axs[i].tick_params(bottom=False, left=False, right=False, top=False)
    
    if i == 0:
      axs[i].set_yticklabels(arr_target_player_ja)
      axs[i].set_ylabel('プレイヤー')
    else:
      axs[i].set_yticklabels([])
        
    for j in range(len(arr_target_player)):
      axs[i].text(0, j, str(round(summary[j, i], 3)), ha='center', va='center', color='black')
    
  plt.savefig('./graphs/strength_s_pf_tb.png', bbox_inches='tight')

  # crostab win-lose

  df_tmp = df_matches[
    (df_matches['year'] >= 2015) &
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
  axs.set_xticklabels(arr_target_player_ja)
  axs.set_yticklabels(arr_target_player_ja)
  axs.set_ylabel('勝ちプレイヤー')
  axs.set_xlabel('負けプレイヤー')

  for tick in axs.get_xticklabels():
    tick.set_rotation(75)

  for i in range(len(arr_target_player)):
    for j in range(len(arr_target_player)):
      text = axs.text(j, i, summary[i, j], ha='center', va='center', color='black')

  fig.tight_layout()
  plt.savefig('./graphs/strength_winlose_crosstab.png', bbox_inches='tight')

if __name__ == '__main__':
  main()
