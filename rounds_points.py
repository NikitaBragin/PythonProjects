import pandas as pd
import numpy as np


def team_points(team1, tour, year):
    # функция определяет количество очков у команды за весь сезон
    sum_team1 = (np.shape(df.loc[(df['Сезон'] == str(year)) & (df['Хозяева'] == str(team1))
                                 & (df['Тур'] <= int(tour)) & ((df['Голы хозяев']) > (df['Голы гостей']))])[0] \
                 + np.shape(df.loc[(df['Сезон'] == str(year)) & (df['Гости'] == str(team1))
                                   & (df['Тур'] <= int(tour)) & ((df['Голы гостей']) > (df['Голы хозяев']))])[0]) * 3 \
                + np.shape(df.loc[(df['Сезон'] == str(year)) & (df['Хозяева'] == str(team1))
                                  & (df['Тур'] <= int(tour)) & ((df['Голы хозяев']) == (df['Голы гостей']))])[0] \
                + np.shape(df.loc[(df['Сезон'] == str(year)) & (df['Гости'] == str(team1))
                                  & (df['Тур'] <= int(tour)) & ((df['Голы хозяев']) == (df['Голы гостей']))])[0]
    return sum_team1


df = pd.read_csv(r'F:\rpl_hist\rpl_2010_to_2019.csv', sep=';')
bt = pd.DataFrame(columns=['Команда', 'Очки'], dtype=str)
year = str(input('Input season:\n'))
tf = df[df[str('Сезон')] == str(year)]
teams_list = sorted(tf.Хозяева.unique())
tour = 30 - int(input('How many tours before the end of the tournament?\n'))
k = 0
for i in teams_list:
    k += 1
    new_row = pd.Series(data={'Команда': str(i), 'Очки': team_points(i, tour, year)}, name=str(k))
    bt = bt.append(new_row, ignore_index=False)
bt.sort_values(by=['Очки'], inplace=True, ascending=False)
new_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
bt = bt.set_index([new_index])
print(bt)
