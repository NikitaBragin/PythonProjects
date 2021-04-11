import pandas as pd
import numpy as np
import time


def team_points(team1, year):
    # функция определяет количество очков у команды за весь сезон
    sum_team1 = (np.shape(df.loc[(df['Сезон'] == str(year)) & (df['Хозяева'] == str(team1))
                                 & ((df['Голы хозяев']) > (df['Голы гостей']))])[0] \
                 + np.shape(df.loc[(df['Сезон'] == str(year)) & (df['Гости'] == str(team1))
                                   & ((df['Голы гостей']) > (df['Голы хозяев']))])[0]) * 3 \
                + np.shape(df.loc[(df['Сезон'] == str(year)) & (df['Хозяева'] == str(team1))
                                  & ((df['Голы хозяев']) == (df['Голы гостей']))])[0] \
                + np.shape(df.loc[(df['Сезон'] == str(year)) & (df['Гости'] == str(team1))
                                  & ((df['Голы хозяев']) == (df['Голы гостей']))])[0]
    return sum_team1


def two_teams_points(team1, team2, year):
    # функция определяет разницу в очках и выводит команду-победителя, либо "tie"
    sum_team1 = (np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                                 & (df[str('Гости')] == str(team2)) & (df['Голы хозяев']) > (df['Голы гостей'])])
                 + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                                   & (df[str('Хозяева')] == str(team2)) & (df['Голы гостей']) > (
                                   df['Голы хозяев'])])) * 3 \
                + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                                  & (df[str('Гости')] == str(team2)) & (df['Голы хозяев']) == (df['Голы гостей'])]) \
                + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                                  & (df[str('Хозяева')] == str(team2)) & (df['Голы хозяев']) == (df['Голы гостей'])])
    sum_team2 = (np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                                 & (df[str('Гости')] == str(team1)) & (df['Голы хозяев']) > (df['Голы гостей'])])
                 + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                                   & (df[str('Хозяева')] == str(team1)) & (df['Голы гостей']) > (
                                   df['Голы хозяев'])])) * 3 \
                + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                                  & (df[str('Гости')] == str(team1)) & (df['Голы хозяев']) == (df['Голы гостей'])]) \
                + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                                  & (df[str('Хозяева')] == str(team1)) & (df['Голы хозяев']) == (df['Голы гостей'])])
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2


def two_teams_wins(team1, team2, year):
    # функция определяет разницу в очках и выводит команду-победителя, либо "tie"
    sum_team1 = np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                                & (df[str('Гости')] == str(team2)) & (df['Голы хозяев']) > (df['Голы гостей'])])[0] \
                + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1)) \
                                  & (df[str('Хозяева')] == str(team2)) & (df['Голы гостей']) > (df['Голы хозяев'])])[0]
    sum_team2 = np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                                & (df[str('Гости')] == str(team1)) & (df['Голы хозяев']) > (df['Голы гостей'])])[0] \
                + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2)) \
                                  & (df[str('Хозяева')] == str(team1)) & (df['Голы гостей']) > (df['Голы хозяев'])])[0]
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2


def two_teams_comparative_goals(team1, team2, year):
    # функция считает разницу между забитыми и пропущенными мячами и выводит команду-победителя, либо "tie"
    sum_team1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                       & (df[str('Гости')] == str(team2)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                         & (df[str('Хозяева')] == str(team2)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                         & (df[str('Гости')] == str(team2)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                         & (df[str('Хозяева')] == str(team2)), 'Голы хозяев'].sum()
    sum_team2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                       & (df[str('Гости')] == str(team1)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                         & (df[str('Хозяева')] == str(team1)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                         & (df[str('Гости')] == str(team1)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                         & (df[str('Хозяева')] == str(team1)), 'Голы хозяев'].sum()
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2


def two_teams_absolute_goals(team1, team2, year):
    # функция считает голы в матчах между двумя командами и выводит команду-победителя, либо "tie"
    sum_team1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                       & (df[str('Гости')] == str(team2)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                         & (df[str('Хозяева')] == str(team2)), 'Голы гостей'].sum()
    sum_team2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                       & (df[str('Гости')] == str(team1)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                         & (df[str('Хозяева')] == str(team1)), 'Голы гостей'].sum()
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2


def all_two_teams_wins(team1, team2, year):
    # функция определяет разницу в победах и выводит команду-победителя, либо "tie"
    sum_team1 = np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                                & (df['Голы хозяев']) > (df['Голы гостей'])])[0] \
                + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1)) \
                                  & (df['Голы гостей']) > (df['Голы хозяев'])])[0]
    sum_team2 = np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                                & (df['Голы хозяев']) > (df['Голы гостей'])])[0] \
                + np.shape(df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2)) \
                                  & (df['Голы гостей']) > (df['Голы хозяев'])])[0]
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2


def all_two_teams_comparative_goals(team1, team2, year):
    # функция считает разницу между забитыми и пропущенными мячами и выводит команду-победителя, либо "tie"
    sum_team1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1)), 'Голы хозяев'].sum()
    sum_team2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2)), 'Голы хозяев'].sum()
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2


def all_two_teams_goals(team1, team2, year):
    # функция определяет кол-во забитых мячей во всех матчах данной командой
    sum_team1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1)), 'Голы гостей'].sum()
    sum_team2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2)), 'Голы гостей'].sum()
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2

year = str(input("Enter season:\n"))
df = pd.read_csv(r'F:\rpl_hist\rpl_2010_to_2019.csv', sep=';')
tf = df[df[str('Сезон')] == str(year)]
team_list = sorted(tf.Хозяева.unique())
bt = pd.DataFrame(1, index=team_list, columns=team_list, dtype=str)
for ni, i in enumerate(team_list):
    for nj, j in enumerate(team_list):
        if ni == nj:
            bt.at[i, j] = 0
        if ni < nj:
            if team_points(i, year) != team_points(j, year):
                if team_points(i, year) > team_points(j, year):
                    bt.at[i, j] = i
                else:
                    bt.at[i, j] = j
            elif two_teams_points(i, j, year) != 'tie':
                bt.at[i, j] = two_teams_points(i, j, year)
            elif two_teams_wins(i, j, year) != 'tie':
                bt.at[i, j] = two_teams_wins(i, j, year)
            elif two_teams_comparative_goals(i, j, year) != 'tie':
                bt.at[i, j] = two_teams_comparative_goals(i, j, year)
            elif two_teams_absolute_goals(i, j, year) != 'tie':
                bt.at[i, j] = two_teams_absolute_goals(i, j, year)
            elif all_two_teams_wins(i, j, year) != 'tie':
                bt.at[i, j] = all_two_teams_wins(i, j, year)
            elif all_two_teams_comparative_goals(i, j, year) != 'tie':
                bt.at[i, j] = all_two_teams_comparative_goals(i, j, year)
            elif all_two_teams_goals(i, j, year) != 'tie':
                bt.at[i, j] = all_two_teams_goals(i, j, year)
            else:
                bt.at[i, j] = 'alp'
        else:
            bt.at[i, j] = bt.at[j, i]
print(bt)