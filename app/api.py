# app/api.py
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .operations import add, subtract, multiply, divide, square_root
from .schemas import OperationInput, SingleOperandInput

router = APIRouter(prefix="/calc", tags=["Calculator Operations"])



@router.get("/", include_in_schema=False)
def health():
    return {"status": "ok"}

@router.post("/add")
def calculate_add(data: OperationInput):
    return {"result": add(data.a, data.b)}

@router.post("/subtract")
def calculate_subtract(data: OperationInput):
    return {"result": subtract(data.a, data.b)}

@router.post("/multiply")
def calculate_multiply(data: OperationInput):
    return {"result": multiply(data.a, data.b)}

@router.post("/divide")
def calculate_divide(data: OperationInput):
    try:
        result = divide(data.a, data.b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/sqrt")
def calculate_sqrt(data: SingleOperandInput):
    try:
        result = square_root(data.value)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
