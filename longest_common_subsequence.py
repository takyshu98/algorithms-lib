LENGTH = 2000

def main():
  s = [None] + list(input())
  t = [None] + list(input())
  
  dp = [[0] * (LENGTH + 1) for _ in range(LENGTH + 1)]
  for i in range(1, len(t)):
    for j in range(1, len(s)):
      if s[j] == t[i]:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  
  print(dp[len(t) - 1][len(s) - 1])

if __name__ == '__main__':
  main()