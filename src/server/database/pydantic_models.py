from pydantic import BaseModel

class ModifyBaseModel(BaseModel):
    id: int = 0

class LoginData(BaseModel):
    password: str
    login: str

class ChangePassword(BaseModel):
    password: str

class User(ModifyBaseModel):
    position: str = ''
    login: str = ''
    password: str = ''
    power_level: int = 0

class Projects(ModifyBaseModel):
    name: str = ''
    description: str = ''
    start_date: str = ''
    end_date: str = ''

class Clients(ModifyBaseModel):
    name: str = ''
    contact: str = ''

class Employees(ModifyBaseModel):
    name: str = ''
    position: str = ''
    contact: str = ''

class Materials(ModifyBaseModel):
    name: str = ''
    quantity: int = 0

class Tasks(ModifyBaseModel):
    project_id: int = 0
    employee_id: int = 0
    description: str = ''
    status: str = ''