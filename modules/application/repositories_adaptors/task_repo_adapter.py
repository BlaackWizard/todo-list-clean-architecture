from dataclasses import dataclass
from typing import List

from modules.domain.repositories.task_repo import TaskRepo
from modules.entities.Task import TaskEntity


@dataclass
class TaskRepoAdapter:
    task_repo: TaskRepo

    def get_task_by_id(self, task_id: int):
        task = self.task_repo.get_task(task_id)
        if task:
            return TaskEntity(
                id=task.id,
                title=task.title,
                description=task.description,
                confirmed=task.confirmed,
                category=task.category,
            )
        return {'error': 'Task not found'}

    def list_tasks(self) -> List[TaskEntity]:
        tasks = self.task_repo.list_tasks()
        return [self._to_entity(task) for task in tasks]

    def save_task(self, task: TaskEntity):
        return self.task_repo.save_task(task)

    def delete_task(self, task: TaskEntity):
        return self.task_repo.delete_task(task)

    def _to_entity(self, task):
        return TaskEntity(
            id=task.id,
            title=task.title,
            description=task.description,
            confirmed=task.confirmed,
            category=task.category
        )

