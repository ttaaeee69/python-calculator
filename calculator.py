class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if (a < 0 and b < 0):
            a = -a
            b = -b
        if (b < 0):
            a , b = b , a
            print(a,b)
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        if (b == 0):
            return "Undefined"
        elif (a < 0 and b < 0):
            a = -a
            b = -b
        elif (a < 0):
            a = -a
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
        
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("The divisor b cannot be zero.")
        
        positive_a, positive_b = abs(a), abs(b)
        remainder = positive_a

        # Calculate the positive remainder
        while remainder >= positive_b:
            remainder = self.subtract(remainder, positive_b)

        # Adjust remainder based on the sign of a and b
        if a < 0:
            remainder = self.subtract(positive_b, remainder)  # Make remainder positive for negative dividends
        
        # If the divisor is negative, the remainder should be negative
        if b < 0:
            remainder = -remainder

        return remainder

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))