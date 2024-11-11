from typing import List

from modules.domain.repositories.task_repo import TaskRepo
from .models import TaskModel
from ...entities.Task import TaskEntity


class TaskRepoWeb(TaskRepo):
    def get_task(self, task_id: int):
        task = TaskModel.object.get(id=task_id)
        return task

    def list_tasks(self):
        tasks = TaskModel.objects.all()
        return tasks

    def save_task(self, task: TaskEntity):
        task_model = self._to_model(task)
        task_model.save()

    def delete_task(self, task: TaskEntity):
        task_model = self._to_model(task)
        task_model.delete()
    def _to_model(self, task: TaskEntity):
        return TaskModel(
            id=task.id,
            title=task.title,
            description=task.description,
            confirmed=task.confirmed,
        )
