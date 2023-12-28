class UnionFind:
  def __init__(self):
    self.parent = [-1] * (10 ** 5 + 9)
    self.size = [1] * (10 ** 5 + 9)
  
  def root(self, x):
    while True:
      if self.parent[x] == -1:
        break
      x = self.parent[x]
    return x
  
  def unite(self, u, v):
    root_u = self.root(u)
    root_v = self.root(v)
    if root_u == root_v:
      return
    if self.size[root_u] < self.size[root_v]:
      self.parent[root_u] = root_v
      self.size[root_v] = self.size[root_v] + self.size[root_u]
    else:
      self.parent[root_v] = root_u
      self.size[root_u] = self.size[root_u] + self.size[root_v]
      
  def is_same(self, u, v):
    return self.root(u) == self.root(v)

def main():
  n, m = map(int, input().split())
  p = [(0, 0) for _ in range(m + 1)]
  e = [(0, 0) for _ in range(m + 1)]
  
  for i in range(1, m + 1):
    a, b, c = map(int, input().split())
    p[i] = (a, b)
    e[i] = (c, i)
    
  sorted_e = sorted(e)
  uf = UnionFind()
  
  ans = 0
  for i in range(1, m + 1):
    cost, idx = sorted_e[i]
    a, b = p[idx]
    if uf.is_same(a, b):
      continue
    uf.unite(a, b)
    ans += cost
  
  print(ans)

if __name__ == '__main__':
  main()