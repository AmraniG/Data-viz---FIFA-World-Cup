from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('C:\\Users\\Ghisl\\Python\\Kaggle\\Fifa Wold cup\\WorldCupMatches.csv')
players = pd.read_csv('C:\\Users\\Ghisl\\Python\\Kaggle\\Fifa Wold cup\\WorldCupPlayers.csv')
cups = pd.read_csv('C:\\Users\\Ghisl\\Python\\Kaggle\\Fifa Wold cup\\WorldCups.csv')


#print(df.head())
#print(players.head())
#print(cups.head())

df['Total_Goals'] = df['Home Team Goals'] + df['Away Team Goals']
goals = df.groupby('Year').Total_Goals.sum().reset_index()
print(goals)

#Bar plot
plt.figure(figsize = (12,7))
sns.set_style('darkgrid')
sns.set_context('poster', font_scale=0.5)
ax = sns.barplot(data = goals, x = 'Year', y = 'Total_Goals')
ax.set_title('Number of goals per year during the World cups')
plt.show()


#Boxplot
plt.figure(figsize = (12,7))
sns.set_style('darkgrid')
ax2 = sns.boxplot(data = df, x = 'Year', y='Total_Goals')
ax.set_title('Number of goals per year during the World cups')
plt.show()
