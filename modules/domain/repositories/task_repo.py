from abc import ABC, abstractmethod
from typing import List

from modules.entities.Task import TaskEntity

class TaskRepo(ABC):
    @abstractmethod
    def get_task(self, task_id: int) -> TaskEntity:
        ...

    @abstractmethod
    def list_tasks(self) -> List[TaskEntity]:
        ...

    @abstractmethod
    def save_task(self, task) -> None:
        ...

    @abstractmethod
    def delete_task(self, task: TaskEntity) -> None:
        ...
