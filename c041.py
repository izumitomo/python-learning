# 多重リストの文字列でもa, b ==b, aができる。
N = int(input())
all_country_medals = []
for i in range(N):
    country_medals = input().split()
    country_medals = [int(s) for s in country_medals]
    all_country_medals += [country_medals]
    for j in range(0, i):
        if all_country_medals[i][0] > all_country_medals[j][0]:
            all_country_medals[j], all_country_medals[i] = all_country_medals[i], all_country_medals[j]
        elif all_country_medals[i][0] == all_country_medals[j][0] and all_country_medals[i][1] > all_country_medals[j][1]:
            all_country_medals[j], all_country_medals[i] = all_country_medals[i], all_country_medals[j]
        elif all_country_medals[i][0] == all_country_medals[j][0] and all_country_medals[i][1] == all_country_medals[j][1] and all_country_medals[i][2] > all_country_medals[j][2]:
            all_country_medals[j], all_country_medals[i] = all_country_medals[i], all_country_medals[j]
for i in (all_country_medals):
    print(*i)
