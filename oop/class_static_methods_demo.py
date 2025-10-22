class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a: int, b: int):
        return a + b
    @classmethod
    def multiply(cls, a: int, b: int):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b