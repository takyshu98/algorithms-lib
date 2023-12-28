import bisect

def binary_search(sorted_list, target_value):
  length = len(sorted_list)
  l = 0
  r = length - 1
  ans = -1
  while l <= r:
    m = (l + r) // 2
    if target_value == sorted_list[m]:
      ans = m
      break
    if target_value < sorted_list[m]:
      r = m - 1
    else:
      l = m + 1
  return ans

def meguru_binary_search(sorted_list, target_value, is_ok):
  l = -1 # 常に条件を満たさない領域（idx=0が条件を満たす場合を考慮）
  r = len(sorted_list) # 常に条件を満たす領域（idx=n-1が条件を満たさない場合を考慮）
  while r - l > 1:
    m = (l + r) // 2
    if is_ok(sorted_list, m, target_value):
      r = m
    else:
      l = m
  return r

def is_ok(sorted_list, index, target_value):
  if sorted_list[index] >= target_value:
    return True
  else:
    return False

def main():
  print('sorted_list = ', end='')
  sorted_list = list(map(int, input().split()))
  
  print('target_value = ', end='')
  target_value = int(input())
  
  print('bisect.bisect_left(sorted_list, target_value) =', bisect.bisect_left(sorted_list, target_value))
  print('bisect.bisect_right(sorted_list, target_value) =', bisect.bisect_right(sorted_list, target_value))
  # binary_searchは値が重複している場合、見つけたところを返却する
  print('binary_search(sorted_list, target_value)      =', binary_search(sorted_list, target_value))
  print('meguru_binary_search(sorted_list, target_value, is_ok)      =', meguru_binary_search(sorted_list, target_value, is_ok))

if __name__ == '__main__':
  main()