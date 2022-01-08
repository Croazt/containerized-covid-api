from fastapi import FastAPI, Response, status
import json
import uvicorn

app = FastAPI()

@app.get('/')
def index(response : Response):
    return {'ok':True, 'data':[], 'message' : 'Api is on!'}

if __name__ == "__main__":
    uvicorn.run('app:app', host='127.0.0.1', port=8080, log_level="info",reload=True)