import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())


knicks_pts_10 = nba_2010.pts[nba.fran_id =='Knicks']
nets_pts_10 = nba_2010.pts[nba.fran_id =="Nets"]
print(knicks_pts_10)
print(nets_pts_10)
knicks_mean_score2010 = knicks_pts_10.mean()
nets_mean_score2010 = nets_pts_10.mean()
print(knicks_mean_score2010)
print(nets_mean_score2010)
diff_means_2010 = knicks_mean_score2010 - nets_mean_score2010
print(diff_means_2010)

plt.hist(knicks_pts_10, alpha = 0.4, normed = True, label='knicks2010')
plt.hist(nets_pts_10, alpha = 0.4, normed = True, label='nets2010')
plt.legend()
plt.title("2010 Nba Season")
plt.show()


knicks_pts_14 = nba_2014.pts[nba.fran_id =='Knicks']
nets_pts_14 = nba_2014.pts[nba.fran_id =="Nets"]
print(knicks_pts_14)
print(nets_pts_14)
knicks_mean_score2014 = knicks_pts_14.mean()
nets_mean_score2014 = nets_pts_14.mean()
print(knicks_mean_score2014)
print(nets_mean_score2014)

plt.hist(knicks_pts_14, alpha = 0.4, normed = True, label='knicks2014')
plt.hist(nets_pts_14, alpha = 0.4, normed = True, label='nets2014')
plt.legend()
plt.title("2014 Nba Season")
plt.show()
plt.clf()
plt.hist(knicks_pts_14, alpha = 0.4, normed = True, label='knicks2014')
plt.hist(nets_pts_14, alpha = 0.4, normed = True, label='nets2014')
plt.legend()
plt.title("2014 Nba Season")
plt.show()

plt.clf()
sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts')
plt.legend
plt.show()

location_result_freq = pd.crosstab(nba_2010.game_location, nba_2010.game_location)
print(location_result_freq)
location_result_proportions = location_result_freq/len(nba_2010.game_location)
print(location_result_proportions)
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

