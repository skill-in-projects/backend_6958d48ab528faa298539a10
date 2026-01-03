from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Controllers.TestController import router as test_router

app = FastAPI(title="Backend API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router)

@app.get("/")
async def root():
    return {{"message": "Backend API is running"}}
