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
  n, q = map(int, input().split())
  query = [list(map(int, input().split())) for _ in range(q)]
  
  union_find = UnionFind()
  for i in range(q):
    ops, u, v = query[i]
    if ops == 1:
      union_find.unite(u, v)
    else:
      if union_find.is_same(u, v):
        print('Yes')
      else:
        print('No')

if __name__ == '__main__':
  main()