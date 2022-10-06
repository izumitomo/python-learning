# 多重リストの文字列でもa, b ==b, aができる。
import numpy as np


N = int(input())
all_country_medals = []
for i in range(N):
    country_medals = input().split()
    country_medals = [int(s) for s in country_medals]
    all_country_medals += [country_medals]

sorted_all_country_medals = sorted(all_country_medals, reverse=True)
for i in (sorted_all_country_medals):
    print(*i)
