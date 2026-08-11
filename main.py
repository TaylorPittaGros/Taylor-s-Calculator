from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from app.api import router as calc_router

app = FastAPI(
    title="Taylor's Calculator API",
    description="Simple RESTful math operations with clean error handling.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "✅ Taylor's Calculator is running!",
        "docs": "/docs",
        "status": "ok"
    }

# Exception handler for validation errors
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid input", "errors": exc.errors()},
    )

# Include the calculator router under /calc prefix
app.include_router(calc_router)
