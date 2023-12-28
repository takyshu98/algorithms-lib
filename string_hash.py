MOD = 2147483647

def generate_hash(l, r, h, pow100):
  val = h[r] - (h[l - 1] * pow100[r - l + 1] % MOD)
  if val < 0:
    val += MOD
  return val

def main():
  n, q = map(int, input().split())
  s = list(input())
  a = [None] * (q + 1)
  b = [None] * (q + 1)
  c = [None] * (q + 1)
  d = [None] * (q + 1)
  for i in range(1, q + 1):
    a[i], b[i], c[i], d[i] = map(int, input().split())
  
  t = [None] * (n + 1)
  for i in range(1, n + 1):
    # a = 1, b = 2, ..., z = 26
    t[i] = ord(s[i - 1]) - ord('a') + 1
    
  pow100 = [None] * (n + 1)
  pow100[0] = 1
  for i in range(1, n + 1):
    pow100[i] = 100 * pow100[i - 1] % MOD
    
  h = [None] * (n + 1)
  h[0] = 0
  for i in range(1, n + 1):
    h[i] = (100 * h[i - 1] + t[i]) % MOD
    
  for i in range(1, q + 1):
    hash1 = generate_hash(a[i], b[i], h, pow100)
    hash2 = generate_hash(c[i], d[i], h, pow100)
    if hash1 == hash2:
      print('Yes')
    else:
      print('No')

if __name__ == '__main__':
  main()