from typing import List
from collections import deque
from functools import lru_cache

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        # Build positions list: positions_list[0] is the knight's initial position
        positions_list = [(kx, ky)] + [tuple(pos) for pos in positions]

        n = len(positions_list)
        # Build a mapping from positions to indices
        pos_to_index = {pos: idx for idx, pos in enumerate(positions_list)}
        # Precompute distances between all positions in positions_list
        dist = [[-1]*n for _ in range(n)]
        board_size = 50

        # Possible knight moves
        moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2),
                 (2, -1), (1, -2), (2, 1), (1, 2)]

        for i in range(n):
            # Perform BFS from positions_list[i]
            sx, sy = positions_list[i]
            visited = [[-1]*board_size for _ in range(board_size)]
            queue = deque()
            queue.append((sx, sy))
            visited[sx][sy] = 0

            while queue:
                x, y = queue.popleft()
                # If this position is in positions_list, record the distance
                if (x, y) in pos_to_index:
                    j = pos_to_index[(x, y)]
                    dist[i][j] = visited[x][y]
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < board_size and 0 <= ny < board_size and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

        total_pawns = n - 1  # Exclude the knight's initial position

        @lru_cache(None)
        def dfs(position_index, remaining_pawns_bitmask, is_alice_turn):
            if remaining_pawns_bitmask == 0:
                return 0
            if is_alice_turn:
                max_total_moves = float('-inf')
                for i in range(1, n):
                    if remaining_pawns_bitmask & (1 << (i - 1)):
                        distance = dist[position_index][i]
                        new_remaining_pawns_bitmask = remaining_pawns_bitmask & ~(1 << (i - 1))
                        total_moves = distance + dfs(i, new_remaining_pawns_bitmask, False)
                        if total_moves > max_total_moves:
                            max_total_moves = total_moves
                return max_total_moves
            else:
                min_total_moves = float('inf')
                for i in range(1, n):
                    if remaining_pawns_bitmask & (1 << (i - 1)):
                        distance = dist[position_index][i]
                        new_remaining_pawns_bitmask = remaining_pawns_bitmask & ~(1 << (i - 1))
                        total_moves = distance + dfs(i, new_remaining_pawns_bitmask, True)
                        if total_moves < min_total_moves:
                            min_total_moves = total_moves
                return min_total_moves

        # Initial call
        remaining_pawns_bitmask = (1 << total_pawns) - 1  # All pawns are remaining
        result = dfs(0, remaining_pawns_bitmask, True)
        return result