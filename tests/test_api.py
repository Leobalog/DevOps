from tests.base_test_api import BaseTestCalculatorAPI
from tests.calculator_client.models import ResultResponse
import pytest

test_add_values = [ (3, 3, 6), (3, -3, 0)]
test_sub_values = [ (6, 4, 2), (3, -3, 6)]
test_mul_values = [ (6, 2, 12), (-3, -3, 9)]
test_div_values = [ (6, 2, 3), (6, -2, -3)]


class TestCalculatorAPI(BaseTestCalculatorAPI):


    @pytest.mark.parametrize("a, b, expected", test_add_values) 
    def test_add_api(self, a, b, expected):
        
        response = self.do_calculation("add", a , b)
        value = response.result

        assert isinstance(response, ResultResponse)
        assert  value == expected


    @pytest.mark.parametrize("a, b, expected", test_sub_values) 
    def test_subtract_api(self, a, b, expected):
        
        response = self.do_calculation("subtract", a , b)
        value = response.result

        assert isinstance(response, ResultResponse)
        assert  value == expected

    @pytest.mark.parametrize("a, b, expected", test_mul_values) 
    def test_mul_api(self, a, b, expected):
        
        response = self.do_calculation("multiply", a , b)
        value = response.result

        assert isinstance(response, ResultResponse)
        assert  value == expected

    @pytest.mark.parametrize("a, b, expected", test_div_values) 
    def test_divide_api(self, a, b, expected):
        
        response = self.do_calculation("divide", a , b)
        value = response.result

        assert isinstance(response, ResultResponse)
        assert  value == expected