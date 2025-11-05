import math
class Fraction:
    def __init__(self, numerator, denominator):
        common = math.gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def add(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def sub(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def mul(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def div(self, other):
        if other.numerator == 0:
            return None
        else:
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __repr__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f'{self.numerator}/{self.denominator}'

def evaluate_expression(expression):
    operator = None
    for op in ['+', '-', '*', '\\']:
        if op in expression:
            operator = op
            break

    if operator is None:
        # If no operator is found, assume it's a single number
        if '/' in expression:
            fraction_parts = list(map(int, expression.split('/')))
            return Fraction(fraction_parts)
        else:
            return Fraction(int(expression), 1)

    left, right = map(str.strip, expression.split(operator))

    # Try to create Fraction for left side
    if '/' in left:
        fraction_left = Fraction(*map(int, left.split('/')))
    else:
        fraction_left = Fraction(int(left), 1)

    # Try to create Fraction for right side
    if '/' in right:
        fraction_right = Fraction(*map(int, right.split('/')))
    else:
        fraction_right = Fraction(int(right), 1)

    if operator == '+':
        return fraction_left.add(fraction_right)
    elif operator == '-':
        return fraction_left.sub(fraction_right)
    elif operator == '*':
        return fraction_left.mul(fraction_right)
    elif operator == '\\':
       if fraction_left.div(fraction_right) == None:
           return 'invalid'
       else:
           return fraction_left.div(fraction_right)


def main():
    while True:
        try:
            expression = input()
            result = evaluate_expression(expression)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()