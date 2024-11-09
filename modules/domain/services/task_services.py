from abc import ABC, abstractmethod

from modules.entities.Task import TaskEntity


class TaskServices(ABC):
    @abstractmethod
    def create_task(self, title: str, description: str) -> TaskEntity:
        ...

    @abstractmethod
    def complete_task(self, task_id: int) -> None:
        ...

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        ...