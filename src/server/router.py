from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/users', tags=['Users']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Clients, database_model=database_models.Clients, prefix='/client', tags=['Clients']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Employees, database_model=database_models.Employees, prefix='/employee', tags=['Employees']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Materials, database_model=database_models.Materials, prefix='/material', tags=['Materials']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Projects, database_model=database_models.Projects, prefix='/project', tags=['Projects']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Tasks, database_model=database_models.Tasks, prefix='/task', tags=['Tasks']).fastapi_router
)
