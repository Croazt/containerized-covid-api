from fastapi import FastAPI, Response
from src.rest import general_data_resource, yearly_data_resource, monthly_data_resource, daily_data_resource

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

    app.include_router(
        yearly_data_resource.router,
        prefix="/yearly",
        tags=['yearly-data']
    )
    
    app.include_router(
        monthly_data_resource.router,
        prefix="/monthly",
        tags=['monthly-data']
    )
    
    app.include_router(
        daily_data_resource.router,
        prefix="/daily",
        tags=['daily-data']
    )
    
    return app