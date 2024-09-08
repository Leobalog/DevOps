import requests

class TestCalculatorAPI():
    def test_calculate_add(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "add" ,
            "operand1": 1,
            "operand2": 1
        }
        response = requests.post(url, json=payload)