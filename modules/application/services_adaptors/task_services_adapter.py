from dataclasses import dataclass

from modules.domain.services.task_services import TaskServices
from modules.domain.repositories.task_repo import TaskRepo
from modules.entities.Task import TaskEntity
from modules.infrastructure.task.models import TaskModel


@dataclass
class TaskServicesAdapter(TaskServices):
    task_repo: TaskRepo

    def create_task(self, id: int, title: str, description: str) -> TaskEntity:
        task = TaskEntity(id=id,title=title, description=description, confirmed=False)
        self.task_repo.save_task(task)
        return task

    def complete_task(self, task_id: int) -> None:
        task_model = self.task_repo.get_task(task_id)
        task_entity = self._to_entity(task_model)
        task_entity.mark_as_completed()
        self.task_repo.save_task(task_entity)

    def delete_task(self, task_id: int) -> None:
        task = self.task_repo.get_task(task_id)
        self.task_repo.delete_task(task)

    def _to_entity(self, task: TaskModel):
        return TaskEntity(id=task.id,
                          title=task.title,
                          description=task.description,
                          confirmed=task.confirmed)

