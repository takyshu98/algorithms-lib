def main():
  n, q = map(int, input().split())
  a = [None] + list(map(int, input().split()))
  x = [None] * (q + 1)
  y = [None] * (q + 1)
  for i in range(1, q + 1):
    x[i], y[i] = map(int, input().split())
    
  dp = [[None] * (n + 1) for _ in range(30)]
  for i in range(1, n + 1):
    dp[0][i] = a[i]
  for d in range(1, 30):
    for i in range(1, n + 1):
      dp[d][i] = dp[d - 1][dp[d - 1][i]]
      
  for j in range(1, q + 1):
    tmp = x[j]
    for d in range(29, -1, -1):
      if ((y[j] // (1 << d)) % 2) != 0:
        tmp = dp[d][tmp]
    print(tmp)

if __name__ == '__main__':
  main()