import heapq

def main():
  n, m = map(int, input().split())
  g = [[] for _ in range(n + 1)]
  for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
    
  DEFAULT_COST = 2 * (10 ** 9)
  dist = [DEFAULT_COST] * (n + 1)
  fixed = [False] * (n + 1)
  
  q = []
  dist[1] = 0
  heapq.heappush(q, (dist[1], 1))
  
  while len(q) != 0:
    pos = heapq.heappop(q)[1]
    if fixed[pos]:
      continue
    fixed[pos] = True
    
    for i in range(len(g[pos])):
      next_pos = g[pos][i][0]
      cost = g[pos][i][1]
      if dist[next_pos] > dist[pos] + cost:
        dist[next_pos] = dist[pos] + cost
        heapq.heappush(q, (dist[next_pos], next_pos))
        
  for i in range(1, n + 1):
    if dist[i] == DEFAULT_COST:
      print(-1)
    else:
      print(dist[i])

if __name__ == '__main__':
  main()