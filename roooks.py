from collections import deque

def min_moves(chessboard):
    def is_valid(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            while is_valid(nx, ny) and chessboard[nx][ny] != 'x':
                neighbors.append((nx, ny))
                nx += dx
                ny += dy
        return neighbors

    start_pos, end_pos = None, None
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'v':
                start_pos = (i, j)
            elif chessboard[i][j] == 'c':
                end_pos = (i, j)

    if start_pos is None or end_pos is None:
        return -1

    visited = set()
    queue = deque([(start_pos, 0)])
    visited.add(start_pos)

    while queue:
        current_pos, moves = queue.popleft()

        if current_pos == end_pos:
            return moves
        
        for neighbor in get_neighbors(*current_pos):
            if neighbor not in visited:
                queue.append((neighbor, moves + 1))
                visited.add(neighbor)

    return -1


chess_board = []
for _ in range(8):
    sample_input=input()
    chess_board.append(sample_input)


result = min_moves(chess_board)
print(result)
