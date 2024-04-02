from .calculator_4 import Calculator4
from typing import Dict, List
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockAverageHandler:
    def average(self, numbers: List[float]) -> float:
        return 3


def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4(MockAverageHandler)

    response = calculator_4.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "average" in response["data"]

    assert response["data"]["Calculator"] == 4
    assert response["data"]["average"] == 3.0
    
    assert response == {'data': {'Calculator': 4, 'average': 3.0}}

