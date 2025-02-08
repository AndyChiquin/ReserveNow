import os
import uvicorn
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.routes.configDeleteRoutes import config_router

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
load_dotenv()

app = FastAPI(title="Config Service - Delete")

app.include_router(config_router)

@app.get("/")
def root():
    return {"message": "Config Service DELETE is running"}

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"❌ Error in {request.url}: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "❌ Internal Server Error", "error": str(exc)},
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8004)))
