import uvicorn
from fastapi import FastAPI, Request
from auth.routes import router as auth_router
from users.routes import router as users_router
from websocket.routes import router as websocket_router, websocket_endpoint
from fastapi.responses import HTMLResponse


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(websocket_router, prefix="/websocket", tags=["websocket"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)
