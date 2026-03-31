class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        heap = [(grid[0][0], 0, 0)]
        t = grid[0][0]
        visit = set()

        while heap:
            time, r, c = heapq.heappop(heap)
            t = max(t, time)
            visit.add((r,c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return t
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr, nc) < 0 or nc >= COLS or nr >= ROWS or (nr, nc) in visit:
                    continue
                heapq.heappush(heap, (grid[nr][nc], nr, nc))
        return t