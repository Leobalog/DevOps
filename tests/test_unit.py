from BE.BE.calculator_helper import CalculatorHelper
import pytest


class Testcalculator():
    def test_add(self):
        # Arrange
        calculator = CalculatorHelper()
        # Action
        value = calculator.add(1,1)
        # Assert
        assert value == 2

    def test_add_with_negative_number(self):
        # Arrange
        calculator = CalculatorHelper()
        # Action
        value = calculator.add(1,-1)
        # Assert
        assert value == 0

    def test_subtract(self):
        # Arrange
        calculator = CalculatorHelper()
        # Action
        value = calculator.subtract(1,1)
        # Assert
        assert value == 0

    def test_multiply(self):
        # Arrange
        calculator = CalculatorHelper()
        # Action
        value = calculator.multiply(1,1)
        # Assert
        assert value == 1
    
    def setup_method(self, method):
        self.calculator = CalculatorHelper()


    def teardown_method(self, method):
        del self.calculator
    

    def test_divide(self):
        # Arrange
        calculator = CalculatorHelper()
        # Action
        value = calculator.divide(1,1)
        # Assert
        assert value == 1

    def test_division_by_zero(self):
        # Arrange
        calculator = CalculatorHelper()
        # Action
        with pytest.raises(ZeroDivisionError) as exinfo:
            value = calculator.divide(4,0)
        # Assert
        assert "division by zero" in str(exinfo.value), "Expected exception"