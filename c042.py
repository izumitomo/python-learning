all_results = []
N = int(input())
score = [['-'] * N for i in range(N)]
for i in range(int(N*(N-1)/2)):
    results = input().split()
    results = [int(s) for s in results]
    all_results += [results]

for i in range(int(N*(N-1)/2)):
    score[all_results[i][0]-1][all_results[i][1]-1] = "W"
    score[all_results[i][1]-1][all_results[i][0]-1] = "L"

for i in score:
    print(*i)
