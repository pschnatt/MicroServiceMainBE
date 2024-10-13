from fastapi import FastAPI
from apiGateway.src.routes.restaurant import router as restaurantrouter
from apiGateway.src.routes.user import router as userrouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(restaurantrouter, prefix="/api/restaurant")
app.include_router(userrouter, prefix="/api/user")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)


