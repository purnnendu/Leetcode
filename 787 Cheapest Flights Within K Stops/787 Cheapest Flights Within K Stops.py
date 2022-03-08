"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst: return 0
        d, seen = collections.defaultdict(list), collections.defaultdict(lambda: float('inf'))
        for u, v, p in flights:
            d[u] += [(v, p)]

        q = [(src, -1, 0)]

        while q:
            pos, k, cost = q.pop(0)
            if pos == dst or k == K: continue
            for nei, p in d[pos]:
                if cost + p >= seen[nei]:
                    continue
                else:
                    seen[nei] = cost+p
                    q += [(nei, k+1, cost+p)]

        return seen[dst] if seen[dst] < float('inf') else -1
