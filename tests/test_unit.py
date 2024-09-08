from BE.BE.calculator_helper import CalculatorHelper

class Testcalculator():
    def test_first(self):
        # Arrange
        calculator = CalculatorHelper()
        # Action
        value = calculator.add(1,1)
        # Assert
        assert value == 2
