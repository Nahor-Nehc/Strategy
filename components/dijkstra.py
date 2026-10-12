import heapq as hq
import math

def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  weights = [math.inf]*n
  path = [None]*n
  queue = []
  weights[s] = 0
  hq.heappush(queue, (0, s))
  while len(queue) > 0:
    g, u = hq.heappop(queue)
    visited[u] = True
    for v, w in G[u]:
      if not visited[v]:
        f = g + w
        if f < weights[v]:
          weights[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))
  return path, weights

G = [[(1, 6), (3, 7)],
    [(2, 5), (3, 8), (4, -4)],
    [(1, -2), (4, 7)],
    [(2, -3), (4, 9)],
    [(0, 2)]]

print(dijkstra(G, 0))