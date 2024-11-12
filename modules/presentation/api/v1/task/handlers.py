from ninja import Router

from modules.application.services_adaptors.task_services_adapter import TaskServicesAdapter
from modules.infrastructure.task.models import TaskModel
from modules.infrastructure.task.task_repo_web import TaskRepoWeb
from .schemas import TaskInSchema, TaskOutSchema
from modules.application.repositories_adaptors.task_repo_adapter import TaskRepoAdapter

router = Router(tags=['Tasks'])

@router.get("get_task_by_id")
def get_task_by_id(request, task_id: int) -> 'TaskOutSchema':
    task_repo_web = TaskRepoWeb()
    services = TaskRepoAdapter(task_repo_web)
    task = services.get_task_by_id(task_id=task_id)
    return TaskOutSchema(id=task.id,
                         title=task.title,
                         description=task.description,
                         confirmed=task.confirmed)
@router.post("create_task")
def create_task(request, schema: TaskInSchema) -> 'TaskOutSchema':
    task_repo_web = TaskRepoWeb()
    services = TaskServicesAdapter(task_repo_web)
    task = services.create_task(id=schema.id,
                                title=schema.title,
                                description=schema.description)
    return TaskOutSchema(id=task.id,
                         title=task.title,
                         description=task.description,
                         confirmed=task.confirmed)

@router.get("mark_as_completed")
def mark_as_completed_task(request, task_id: int):
    task_repo_web = TaskRepoWeb()
    services = TaskServicesAdapter(task_repo_web)
    services.complete_task(task_id)
    return "Succesed"