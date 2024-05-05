class Fraction():
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        tempNumerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        tempDenominator = self.denominator * other.denominator
        return Fraction(tempNumerator, tempDenominator)

    def __sub__(self, other):
        tempNumerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        tempDenominator = self.denominator * other.denominator
        return Fraction(tempNumerator, tempDenominator)

    def __mul__(self, other):
        tempNumerator = self.numerator * other.numerator
        tempDenominator = self.denominator * other.denominator
        return Fraction(tempNumerator, tempDenominator)

    def __truediv__(self, other):
        tempNumerator = self.numerator * other.denominator
        tempDenominator = self.denominator * other.numerator
        return Fraction(tempNumerator, tempDenominator)
     
def getFraction():
    while True:
        try:
            n = int(input("Enter the numerator: "))
            d = int(input("Enter the denominator: "))
            if d == 0:
                raise ValueError("The denominator can't be zero")
            return Fraction(n, d)
        except ValueError as Error:
            print(Error)

def main():
    print("Enter Fraction 1:")
    fraction1 = getFraction()
    print()
    print("Enter Fraction 2:")
    fraction2 = getFraction()
    print()

    while True:
        operation = input("Enter operation (+, -, *, /) or b to exit: ")

        if operation == 'b':
            print("Thank You \n")
            break
        elif operation in ('+', '-', '*', '/'):
            if operation == '+':
                result = fraction1 + fraction2
            elif operation == '-':
                result = fraction1 - fraction2
            elif operation == '*':
                result = fraction1 * fraction2
            elif operation == '/':
                result = fraction1 / fraction2

            print("Result:", result)
        else:
            print("Invalid operation is entered")
main()