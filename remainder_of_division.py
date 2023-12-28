MOD = 1000000007

def power(a, b):
  p = a
  ans = 1
  for i in range(30):
    if b & (1 << i):
      ans = (ans * p) % MOD
    p = (p * p) % MOD
  return ans

def main():
  n, r = map(int, input().split())
  top, bottom = 1, 1
  for i in range(1, n + 1):
    top = (top * i) % MOD
  for i in range(1, r + 1):
    bottom = (bottom * i) % MOD
  for i in range(1, n - r + 1):
    bottom = (bottom * i) % MOD
  ans = (top * power(bottom, MOD - 2)) % MOD
  print(ans)

if __name__ == '__main__':
  main()