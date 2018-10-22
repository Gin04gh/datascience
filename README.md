# datascience

データサイエンス関連プログラムを保存・管理するリポジトリ.  

```
datascience 
│
├─samples_python.......................................Pythonによるデータサイエンス関連の実装サンプル集
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─bayesian_modeling_pymc3.ipynb.....................ベイジアンモデル by pymc3
│  ├─bayesian_modeling_pystan.ipynb....................ベイジアンモデル by pystan
│  ├─chi-squared_test.ipynb............................カイ二乗検定
│  ├─facter_analysis.ipynb.............................因子分析
│  ├─fisher_exact_test.ipynb...........................フィッシャーの正確確率検定
│  ├─gaussian_mixture_model.ipynb......................混合ガウスモデル
│  ├─kernel_density_estimation_pandas.ipynb............カーネル密度推定 by pandas
│  ├─kernel_density_estimation_scipy.ipynb.............カーネル密度推定 by scipy
│  ├─kolmogorov-smirnov_test.ipynb.....................コルモゴロフ・スミルノフ検定
│  ├─multiple_linear_regression_analysis.ipynb.........重回帰分析
│  ├─non-correlation_test.ipynb........................無相関検定
│  ├─principal_component_analysis.ipynb................主成分分析
│  ├─random_forest.ipynb...............................ランダムフォレスト
│  ├─shapiro-wilk_test.ipynb...........................シャピロ・ウィルク検定
│  ├─support_vector_machine.ipynb......................サポートベクトルマシン
│  ├─t-stats_confidence_interval.ipynb.................t統計量による母平均の信頼区間
│  ├─two_samples_f_test.ipynb..........................2標本間のF検定
│  ├─two_samples_t_test.ipynb..........................2標本間のt検定
│  ├─two_samples_welch_t_test.ipynb....................2標本間のウェルチのt検定
│  ├─two_samples_wilcoxon_test.ipynb...................2標本間のウィルコクソンの順位和検定
│  ├─t-sne.ipynb.......................................t-SNE
│  ├─plotly.ipynb......................................Plotly
│  ├─decision_tree.ipynb...............................決定木
│  ├─doc2vec_gensim.ipynb..............................doc2vec by gensim
│  ├─multilabel_classifier_mlknn_sklearn.ipynb.........MLkNNによるマルチラベル分類
│  ├─confidence_weighted_learning.ipynb..............................オンライン機械学習 (CW)
│  ├─soft_confidence_weighted_learning_ver1.ipynb....................オンライン機械学習 (SCW ver.1)
│  ├─soft_confidence_weighted_learning_ver2.ipynb....................オンライン機械学習 (SCW ver.2)
│  └─study_201804_plotly.ipynb.......................................勉強会準備 (plotly)
│
├─samples_deeplearning_python........................................Pythonによるディープラーニング関連の実装サンプル集
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─cnn_chainer_ver1.ipynb..........................................CNN by chainer
│  ├─cnn_chainer_ver2.ipynb..........................................CNN by chainer (trainer)
│  ├─cnn_pytorch.ipynb...............................................CNN by pytorch
│  ├─cnn_tensorflow_eager.ipynb......................................CNN by tensorflow eager
│  ├─cnn_tensorflow_ver1.ipynb.......................................CNN by tensorflow (low level)
│  ├─cnn_tensorflow_ver2.ipynb.......................................CNN by tensorflow (high level)
│  ├─seq2seq.ipynb...................................................Seq2Seq
│  ├─attention_seq2seq.ipynb.........................................Attention + Seq2Seq
│  ├─sentence_classifier_cnn.ipynb...................................CNNによる文章分類
│  ├─sentence_classifier_lstm.ipynb..................................LSTMエンコーダによる文章分類
│  ├─nnlm_abs.ipynb..................................................Neural Network Language Model + Attention
│  ├─dropout_bayesian_approximation.ipynb............................ベイジアンドロップアウト
│  ├─dropout_bayesian_approximation_experiment.ipynb.................ベイジアンドロップアウト実験
│  ├─lstm_chainer_ver1.ipynb.........................................LSTM by chainer (F.lstm)
│  ├─lstm_chainer_ver2.ipynb.........................................LSTM by chainer (L.LSTM)
│  ├─mnist_classifier_3d_gradcam_plotly.ipynb........................GradCAMをPlotlyで可視化
│  ├─mnist_classifier_3d_t-sne_plotly.ipynb..........................中間層ベクトルのt-SNEをPlotlyで可視化
│  ├─nn_chainer_ver1.ipynb...........................................ニューラルネットワーク by chainer
│  ├─nn_chainer_ver2.ipynb...........................................ニューラルネットワーク by chainer
│  ├─gradcam.ipynb...................................................GradCAM
│  ├─bayesian_dropout_gradcam_mnist.ipynb............................ベイジアンドロップアウト + GradCAM
│  ├─ssd300_chainercv.ipynb..........................................SSD by chainercv
│  ├─faster_rcnn_chainercv.ipynb.....................................Faster R-CNN by chainercv
│  ├─yolov3_chainercv.ipynb..........................................YOLOv3 by chainercv
│  ├─dcgan.ipynb.....................................................DCGAN by chainer
│  ├─tensorflow_probability_sample.ipynb.............................TensorFlow Probability (Edward2)
│  └─study_201806_tensorflow_eager.ipynb.............................勉強会準備 (tensorflow eager)
│
├─samples_r..........................................................Rによるデータサイエンス関連の実装サンプル集
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─bayesian_statistical_modeling_rstan.ipynb.......................ベイジアンモデル by rstan
│  ├─chi-squared_test.ipynb..........................................カイ二乗検定
│  ├─fisher_exact_test.ipynb.........................................フィッシャーの正確確率検定
│  ├─kernel_density_estimation.ipynb.................................カーネル密度推定
│  ├─kolmogorov-smirnov_test.ipynb...................................コルモゴロフ・スミルノフ検定
│  ├─multiple_linear_regression_analysis.ipynb.......................重回帰分析
│  ├─non-correlation_test.ipynb......................................無相関検定
│  ├─principal_component_analysis.ipynb..............................主成分分析
│  ├─random_forest.ipynb.............................................ランダムフォレスト
│  ├─shapiro-wilk_test.ipynb.........................................シャピロ・ウィルク検定
│  ├─support_vector_machine.ipynb....................................サポートベクトルマシン
│  ├─t-stats_confidence_interval.ipynb...............................t統計量による母平均の信頼区間
│  ├─two_samples_f_test.ipynb........................................2標本間のF検定
│  ├─two_samples_t_test.ipynb........................................2標本間のt検定
│  ├─two_samples_welch_t_test.ipynb..................................2標本間のウェルチのt検定
│  └─two_samples_wilcoxon_test.ipynb.................................2標本間のウィルコクソンの順位和検定
│
├─samples_julia......................................................juliaによるデータサイエンス関連の実装サンプル集
│  ├─README.md
│  ├─docker/Dockerfile
│  └─distributions.ipynb.............................................分布サンプル
│
├─kaggle_compe_house_prices_advanced_regression_techiques............kaggleコンペの分析
│  ├─README.md
│  ├─docker/Dockerfile
│  └─notebook.ipynb..................................................家の価格予測モデル
│
├─kaggle_compe_statoil_c-core_lceberg_classifier_challenge...........kaggleコンペの分析
│  ├─README.md
│  ├─docker/Dockerfile
│  └─notebook.ipynb..................................................衛星画像の氷山予測モデル
│
├─kaggle_compe_titanic_machine_learning_from_disaster................kaggleコンペの分析
│  ├─README.md
│  ├─docker/Dockerfile
│  └─notebook.ipynb..................................................生存者の予測モデル
│
├─kaggle_dataset_flower_color_images.................................kaggleデータセットに対する分析
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─auto_encoder_similarity.ipynb...................................自己符号化器
│  ├─transfer_leaning_vgg16.ipynb....................................転移学習
│  ├─finetuning_vgg16.ipynb..........................................ファインチューニング
│  ├─threshold_color_hist.ipynb......................................色ヒストグラム
│  └─image_histogram.ipynb...........................................画像ヒストグラム
│
├─kaggle_dataset_huge_stock_market_dataset...........................kaggleデータセットに対する分析
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─system_trade_dqn.ipynb..........................................Deep Q-Network (DQN)
│  ├─system_trade_ddqn.ipynb.........................................Double DQN
│  ├─system_trade_dueling_ddqn.ipynb.................................Dueling Double DQN
│  └─system_trade_dueling_ddqn_prioritized_experience_replay.ipynb...Dueling Double DQN + Prioritized Experience Replay
│
├─kaggle_dataset_mushroom_classification.............................kaggleデータセットに対する分析
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─bayesian_neural_network_edward.ipynb............................ベイジアンニューラルネットワークで毒キノコ分類
│  └─study_201712_edward.ipynb.......................................勉強会準備 (Edwardとベイジアンニューラルネットワーク)
│
├─kaggle_dataset_association_of_tennis_professionals_matches.........kaggleデータセットに対する分析
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─player_strong_bayesian_modeling.ipynb...........................ベイジアンモデルで男子プロテニス強さモデリング
│  └─player_strong_time_series_bayesian_modeling.ipynb...............ベイジアンモデルで男子プロテニス強さ時系列モデリング
│
├─kaggle_dataset_credit_card_fraud_detection.........................kaggleデータセットに対する分析
│  ├─README.md
│  ├─docker/Dockerfile
│  └─notebook.ipynb..................................................クレジットカードの不正利用予測モデル
│
├─qiita_transfer_learining_fine_tuning_chainer.......................Qiita投稿記事のソース
│  ├─README.md
│  ├─docker/Dockerfile
│  └─notebook.ipynb..................................................転移学習, ファインチューニング
│
├─open_ai............................................................Open AI Gym に対する強化学習, 深層強化学習の実装
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─check_brakeout.ipynb............................................Breakout環境確認
│  ├─dqn_cnn_frozenlake.ipynb........................................Deep Q-Network (DQN) by chainer
│  ├─dqn_nn_frozenlake.ipynb.........................................Deep Q-Network (DQN) by chainer
│  ├─dqn_pytorch_cartpole.ipynb......................................Deep Q-Network (DQN) by pytorch
│  ├─ddqn_cnn_frozenlake.ipynb.......................................Double DQN by chainer
│  ├─ddqn_nn_frozenlake.ipynb........................................Double DQN by chainer
│  ├─ddqn_pytorch_cartpole.ipynb.....................................Double DQN by pytorch
│  └─q-learning_frozenlake.ipynb.....................................Q-learning
│
├─e-stat.............................................................e-Stat のデータに対する分析
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─using_e-stat_api_sample.ipynb....................................e-Stat APIの使い方サンプル
│  ├─estimate_smr_bayesian_modeling.ipynb.............................ベイジアンモデルでSMR推定
│  └─study_201703_geographic_visualization_and_bayesian.ipynb........勉強会準備 (地理データで階層ベイズモデル)
│
├─stock_price_data_warehouse.........................................株価データに対する分析
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─candle_stick_mpl_finance.ipynb..................................ローソク足
│  ├─moving_average.ipynb............................................移動平均
│  ├─bollinger_band.ipynb............................................ボリンジャーバンド
│  ├─macd.ipynb......................................................MACD
│  ├─rsi.ipynb.......................................................RSI
│  ├─stochastics.ipynb...............................................ストキャスティクス
│  ├─ichimoku.ipynb..................................................一目均衡表
│  └─compare_technical_analysis.ipynb................................テクニカル指標の比較検証
│
├─news_corpus........................................................ニュースコーパスデータに対する分析
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─binary_relevance_multinomial_nb.ipynb...........................Binary Relevance Learning on 自然言語処理
│  ├─binary_relevance_multinomial_nb_ja.ipynb........................Binary Relevance Learning on 自然言語処理 (Japanese)
│  ├─binary_relevance_sgd.ipynb......................................Binary Relevance Learning on 自然言語処理
│  ├─compare_sentence_binary_classification.ipynb....................Binary Relevance Learning の分類器比較
│  ├─co-occurrence_network.ipynb.....................................共起語ネットワーク
│  └─scdv.ipynb......................................................SCDV
│
├─pilotnet_visualbackprop............................................PilotNet + Visual back prop の実装
│  ├─README.md
│  ├─docker/Dockerfile
│  └─notebook.ipynb..................................................PilotNet + Visual back prop
│
├─compare_state_space_model..........................................statsmodels, pystan, PyMC3, Edward の状態空間モデルの実装
│  ├─README.md
│  ├─docker/Dockerfile
│  └─notebook.ipynb .................................................statsmodels, pystan, PyMC3, Edward の状態空間モデル
│
└─zerokara_deeplearning..............................................『ゼロから作るDeep Learning』勉強ノート
   ├─README.md
   ├─docker/Dockerfile
   ├─notebook.ipynb..................................................勉強ノート1
   └─notebook2.ipynb.................................................勉強ノート2
```

***Template***

```
│
├─**********...................
│  ├─README.md
│  ├─docker/Dockerfile
│  ├─**********.ipynb..........
│  └─**********.ipynb..........
```
