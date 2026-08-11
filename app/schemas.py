from pydantic import BaseModel


class OperationInput(BaseModel):
    """For operations requiring two operands: a, b"""
    a: float
    b: float

    model_config = {
        "json_schema_extra": {
            "examples": [{"a": 10.5, "b": -3}]
        }
    }


class SingleOperandInput(BaseModel):
    """For operations with one operand (e.g., square root)"""
    value: float

    model_config = {
        "json_schema_extra": {
            "examples": [{"value": 9}]
        }
    }
