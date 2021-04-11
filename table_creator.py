import pandas as pd


def two_teams_points(team1, team2, year):
    # функция определяет разницу в очках и выводит команду-победителя, либо "tie"
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


'''def two_teams_wins(team1, team2, year):
    # функция определяет разницу в очках и выводит команду-победителя, либо "tie"
    sum_team1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                       & (df[str('Гости')] == str(team2)) & (df['Голы хозяев']) > (df['Голы гостей'])].shape()[0] \
                 + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                          & (df[str('Хозяева')] == str(team2)) & (df['Голы гостей']) > (df['Голы хозяев'])].shape()[0]
    sum_team2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                       & (df[str('Гости')] == str(team1)) & (df['Голы хозяев']) > (df['Голы гостей'])].shape()[0] \
                 + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                          & (df[str('Хозяева')] == str(team1)) & (df['Голы гостей']) > (df['Голы хозяев'])].shape()[0]
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2'''



def two_teams_comparative_goals(team1, team2, year):
    # функция считает разницу между забитыми и пропущенными мячами и выводит команду-победителя, либо "tie"
    sum_team1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                  & (df[str('Гости')] == str(team2)), 'Голы хозяев'].sum() \
                 + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                  & (df[str('Хозяева')] == str(team2)), 'Голы гостей'].sum() \
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                  & (df[str('Гости')] == str(team2)), 'Голы гостей'].sum() \
                 + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                  & (df[str('Хозяева')] == str(team2)), 'Голы хозяев'].sum()
    sum_team2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                       & (df[str('Гости')] == str(team1)), 'Голы хозяев'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                         & (df[str('Хозяева')] == str(team1)), 'Голы гостей'].sum()\
                - df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                       & (df[str('Гости')] == str(team1)), 'Голы гостей'].sum() \
                + df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                         & (df[str('Хозяева')] == str(team1)), 'Голы хозяев'].sum()
    if sum_team1 == sum_team2:
        return 'tie'
    if sum_team1 > sum_team2:
        return team1
    if sum_team1 < sum_team2:
        return team2



'''def number_of_goals(team1, year):
    # функция определяет кол-во забитых мячей во всех матчах данной командой
    sum1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1)), 'Голы хозяев'].sum()
    sum2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1)), 'Голы гостей'].sum()
    return sum1 + sum2'''


def max_goals(team1, team2, year):
    # функция сравнивает максимальное количество голов для обеих команд и выводит победителя, либо 'tie'
    max1_team1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team1))
                       & (df[str('Гости')] == str(team2)), 'Голы хозяев'].max()
    max2_team1 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team1))
                        & (df[str('Хозяева')] == str(team2)), 'Голы гостей'].max()
    max1_team2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Хозяева')] == str(team2))
                       & (df[str('Гости')] == str(team1)), 'Голы хозяев'].max()
    max2_team2 = df.loc[(df[str('Сезон')] == str(year)) & (df[str('Гости')] == str(team2))
                         & (df[str('Хозяева')] == str(team1)), 'Голы гостей'].max()
    max_team1 = max(max1_team1, max2_team1)

    max_team2 = max(max1_team2, max2_team2)
    if max_team1 == max_team2:
        return 'tie'
    if max_team1 > max_team2:
        return team1
    if max_team1 < max_team2:
        return team2



df = pd.read_csv(r'F:\rpl_hist\rpl_2010_to_2019.csv', sep=';')
print(max_goals('ЦСКА', "Спартак", '2013/2014'))
