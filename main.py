from fastapi import FastAPI
from apiGateway.src.routes.restaurant import router as restaurantrouter
app = FastAPI()

app.include_router(restaurantrouter, prefix="/api/restaurant")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)