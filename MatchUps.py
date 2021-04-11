print('How many rounds do we want to look at? It must range from 1 to 30')
g = int(input())
round_count = 0
current_score = 0
possible_fin_score = 90
while round_count != g:
    n = input()
    round_count += 1
    if n == 'w':
        current_score += 3
    if n == 'd':
        current_score += 1
        possible_fin_score -= 2
    if n == 'l':
        possible_fin_score -= 3
print('Current score = ', current_score, ' .', sep='')
print('UB of the possible final score is ', possible_fin_score, sep='')
