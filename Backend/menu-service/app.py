from fastapi import FastAPI
from api.create.route import router as create_router
from api.read.route import router as read_router
from api.update.route import router as update_router
from api.delete.route import router as delete_router

app = FastAPI()

app.include_router(create_router)
app.include_router(read_router)
app.include_router(update_router)
app.include_router(delete_router)

@app.get("/")
def root():
    return {"message": "Menu Service API Running!"}
