import sys

def count_tile_positions(N, M, board):
    positions_count = 0

    for row in board:
        consecutive_empty = 0

        for square in row:
            if square == 0:
                consecutive_empty += 1
            else:
                positions_count += max(0, consecutive_empty - N + 1)
                consecutive_empty = 0

        positions_count += max(0, consecutive_empty - N + 1)

    for col in range(M):
        consecutive_empty = 0

        for row in board:
            if row[col] == 0:
                consecutive_empty += 1
            else:
                positions_count += max(0, consecutive_empty - N + 1)
                consecutive_empty = 0

        positions_count += max(0, consecutive_empty - N + 1)

    return positions_count


def main():
    for line in sys.stdin:
        N = int(line.strip())
        if N == 0:
            break

        M = int(sys.stdin.readline().strip())
        board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

        result = count_tile_positions(N, M, board)
        print(result)


if __name__ == "__main__":
    main()
