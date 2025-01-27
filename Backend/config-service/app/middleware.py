from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

def create_error_middleware(app: FastAPI):
    @app.middleware("http")
    async def db_exception_handler(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except SQLAlchemyError as e:
            return JSONResponse(
                status_code=500,
                content={"error": "Database error", "details": str(e)}
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"error": "Internal server error", "details": str(e)}
            )
