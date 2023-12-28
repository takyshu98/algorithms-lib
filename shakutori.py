def shakutori(sorted_list, constraint_value):
  n = len(sorted_list)
  matched_pair_count = 0
  r = 0
  for l in range(n - 1):
    while r + 1 < n and sorted_list[r + 1] - sorted_list[l] <= constraint_value:
      r += 1
    matched_pair_count += (r - l)
  return matched_pair_count

def main():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
    
  print(shakutori(a, k))

if __name__ == '__main__':
  main()