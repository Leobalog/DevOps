import pytest
import requests
import json
from tests.calculator_client.client import Client
from tests.calculator_client.api.actions import calculate
from tests.calculator_client.models.calculation import Calculation
from tests.calculator_client.models.calculation import Opertions

class BaseTestCalculatorAPI():

    def setup_method(self):
        self.client = Client(base_url="http://localhost:5000")

    def teardown_method(self):
        self.client = None
    
    def do_calculation(self, operation, operand1, operand2):

        self.operand1 = operand1
        self.operand2 = operand2
        operation_enum = getattr(Opertions, operation.upper(), None)
        calculation = Calculation(operation=operation_enum, operand1=self.operand1, operand2=self.operand2)
        response = calculate.sync(client=self.client, body=calculation)

        return response