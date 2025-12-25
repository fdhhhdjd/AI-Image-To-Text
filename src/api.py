from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import ollama_router, openai_router, default_router

app = FastAPI(
    title="AI Image API Service",
    description="OpenAI/Ollama-compatible API Service",
    version="1.0.0",
)

# Thêm CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả domain
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Cho phép tất cả headers
    expose_headers=["*"],  # Hiển thị tất cả headers
)

app.include_router(openai_router, prefix="/v1")
app.include_router(ollama_router, prefix="")
app.include_router(default_router, prefix="")