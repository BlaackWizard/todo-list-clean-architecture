from ninja import Schema


class TaskInSchema(Schema):
    id: int # noqa
    title: str
    description: str
    category: str = 'Not category'

class TaskOutSchema(Schema):
    id: int # noqa
    title: str
    description: str
    confirmed: bool
    category: str

class ErrorSchema(Schema):
    error: str
