class Calculator:
    operations_history = []
    def __init__(self):
        operations_history = []
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        result = self.num1 + self.num2
        self.operations_history.append(f"{self.num1} + {self.num2} = {result}")
        return result
    
    def mul(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        result = self.num1 * self.num2
        self.operations_history.append(f"{self.num1} * {self.num2} = {result}")
        return result
    
    def div(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        result = self.num1 / self.num2
        self.operations_history.append(f"{self.num1} / {self.num2} = {result}")
        return result
    
    def show_operations(self):
        for i in self.operations_history:
            print(i)

    def clear(self):
        self.operations_history = []

calc = Calculator()
calc.add(1, 3)
calc.add(2, 10)
calc.mul(100, 12.2)
calc.show_operations()