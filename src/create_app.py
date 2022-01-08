from fastapi import FastAPI, Response
from src.rest import general_data_resource

def create_app():
    app = FastAPI(
        title="Containerized COVID API",
        description="Api to get information about COIVID update in Indonesia",
        version="1.0.0",
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    @app.get('/')
    def get_general_data(response : Response):
        return general_data_resource.get_general_data(response)
    return app