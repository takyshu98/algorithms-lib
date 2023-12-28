import sys
sys.setrecursionlimit(10**6)

class SegmentTree:
  def __init__(self, n):
    self.dat = [None] * 300000
    self.size = 1
    while self.size < n:
      self.size *= 2    # sizeは最下層の要素数
    for i in range(1, self.size * 2):
      self.dat[i] = 0   # i = 1 ~ n x 2 - 1 ... 全体の要素数
  
  def update(self, pos, x):
    pos += self.size - 1
    self.dat[pos] = x
    while pos >= 2:
      pos //= 2 # 直上は左右によらず2の商の切り捨て
      self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])
      
  def query(self, l, r, a, b, u):
    if r <= a or b <= l:    # 半開区間なので等号で重なることはない
      return -10 ** 9
    if l <= a and b <= r:
      return self.dat[u]
    m = (a + b) // 2
    ans_l = self.query(l, r, a, m, u * 2)
    ans_r = self.query(l, r, m, b, u * 2 + 1)
    return max([ans_l, ans_r])
    
def main():
  n, q = map(int, input().split())
  st = SegmentTree(n)
  for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
      st.update(query[1], query[2])
    else:
      print(st.query(query[1], query[2], 1, st.size + 1, 1))    # 半開区間を指定

if __name__ == '__main__':
  main()