from fastapi import FastAPI
from app.domain.delete.delete import router as delete_router

app = FastAPI(title="Delete Service", description="Handles table deletion operations")

app.include_router(delete_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
