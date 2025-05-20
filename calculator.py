class Calculator:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
    print("Multiplication: 5 * 3 =", calc.multiply(5, 3))
