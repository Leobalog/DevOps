import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse


class TestCalculatorAPI():
    def test_calculate_add(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "add" ,
            "operand1": 1,
            "operand2": 1
        }
        response = requests.post(url, json=payload)

    def test_generated_code_add(self):
        client = Client(base_url="http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=1,operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 2

    def test_calculate_subtract(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "subtract" ,
            "operand1": 1,
            "operand2": 1
        }
        response = requests.post(url, json=payload)

    def test_generated_code_subtract(self):
        client = Client(base_url="http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.SUBTRACT, operand1=1,operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 0

    def test_calculate_divide(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "divide" ,
            "operand1": 1,
            "operand2": 1
        }
        response = requests.post(url, json=payload)

    def test_generated_code_divide(self):
        client = Client(base_url="http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.DIVIDE, operand1=1,operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 1

    def test_calculate_multiply(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "multiply" ,
            "operand1": 1,
            "operand2": 1
        }
        response = requests.post(url, json=payload)

    def test_generated_code_multiply(self):
        client = Client(base_url="http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.MULTIPLY, operand1=1,operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 1

