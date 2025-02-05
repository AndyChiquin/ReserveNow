from fastapi import FastAPI
from app.domain.create.create import router as create_router

app = FastAPI(title="Create Service", description="Handles table creation and assignment")

app.include_router(create_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
