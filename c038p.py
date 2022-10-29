M, N = map(int, input().split())
ans_rest = 1000
ans_num_per_cup = 1000
for i in range(M):
  cup = int(input())
  num_per_cup = N // cup
  rest = N % cup
  if ans_rest > rest:
    ans_num_per_cup = num_per_cup
    ans_rest = rest
    machine = i + 1
  elif ans_rest == rest:
    if ans_num_per_cup >= num_per_cup:
      ans_num_per_cup = num_per_cup
      ans_rest = rest
      machine = i + 1
print(machine)
