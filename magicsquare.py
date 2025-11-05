def is_magic(square):
    order = len(square)
    magic_sum = sum(square[0])

    # Check rows
    for row in square:
        if sum(row) != magic_sum:
            return False

    # Check columns
    for j in range(order):
        if sum(square[i][j] for i in range(order)) != magic_sum:
            return False

    # Check diagonals
    if sum(square[i][i] for i in range(order)) != magic_sum or sum(square[i][order - i - 1] for i in range(order)) != magic_sum:
        return False

    return True

def check_magic(square):
    order = len(square)

    for i in range(order):
        for j in range(order):
            if square[i][j] == 0:
                for k in range(1, order**2 + 1):
                    square[i][j] = k

                    # Check if the modified square is a magic square
                    if is_magic(square):
                        return square
                    square[i][j] = 0

    return None

def print_square(square):
    for row in square:
        final_row = ""
        for elem in row:
            final_row += str(elem) + " "
        print(final_row.rstrip())

def main():

    start_square = int(input())

    if start_square < 3:
        print("Order must be 3 or greater.")
        return

    square = [list(map(int, input().split())) for _ in range(start_square)]

    final_square = check_magic(square)

    if final_square is not None:
        print("Magic Square:")
        print_square(final_square)
    else:
        print("Can't be magic")

if __name__ == "__main__":
    main()