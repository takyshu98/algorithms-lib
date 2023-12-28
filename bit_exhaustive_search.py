def bit_exhaustive_search(candidate_list, target_value):
  digits = len(candidate_list)
  for i in range(1 << digits):
    tmp = 0
    for j in range(digits):
      if i & (1 << j):
        tmp += candidate_list[j]
    if tmp == target_value:
      return True
  return False

def main():
  print('candidate_list = ', end='')
  candidate_list = list(map(int, input().split()))
  
  print('target_value = ', end='')
  target_value = int(input())

  if bit_exhaustive_search(candidate_list, target_value):
    print('Yes')
  else:
    print('No')

if __name__ == '__main__':
  main()