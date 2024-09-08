from BE.calculator_helper import CalculatorHelper
import pytest

class baseclass():
    def setup_method(self, method):
        self.calculator = CalculatorHelper()

    def teardown_method(self, method):
        del self.calculator

class Testcalculator(baseclass):
    @pytest.mark.parametrize("a, b, expected", 
    [
        (2, 3, 5),   # Test case 1
        (0, 0, 0),   # Test case 2
        (-1, -1, -2),# Test case 3
        (100, 200, 300), # Test case 4
    ])

    def test_add(self, a, b, expected):
        result = self.calculator.add(a, b)
        assert result == expected
    
    def test_add_with_negative_number(self):
        value = self.calculator.add(1,-1)
        assert value == 0

    def test_subtract(self):
        value = self.calculator.subtract(1,1)
        assert value == 0

    def test_multiply(self):
        value = self.calculator.multiply(1,1)
        assert value == 1

    def test_divide(self):
        value = self.calculator.divide(1,1)
        assert value == 1

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError) as exinfo:
            value = self.calculator.divide(4,0)
        assert "division by zero" in str(exinfo.value), "Expected exception"