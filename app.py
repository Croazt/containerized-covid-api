from fastapi import FastAPI, Response, status
import json
import uvicorn
from src.create_app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run('app:app', host='127.0.0.1', port=8080, log_level="info",reload=True)