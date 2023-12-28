def main():
  a, b = map(int, input().split())
  print(a ** b)
  
  p = a
  ans = 1
  for i in range(b):
    if b & (1 << i):
      ans *= p
    p *= p  

  print(ans)

if __name__ == '__main__':
  main()