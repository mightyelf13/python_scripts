def modular_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % 100
        exponent = exponent >> 1
        base = (base * base) % 100
    return result


if __name__ == "__main__":
    A = int(input())
    B = input().strip()
    A_two_digits = A % 100
    exponent_decimal = int(B, 2)
    result = modular_exponentiation(A_two_digits, exponent_decimal)
    print(f"{result:02d}")
