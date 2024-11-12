from ninja import Schema

class TaskInSchema(Schema):
    id: int
    title: str
    description: str

class TaskOutSchema(Schema):
    id: int
    title: str
    description: str
    confirmed: bool = False

class ErrorSchema(Schema):
    error: str