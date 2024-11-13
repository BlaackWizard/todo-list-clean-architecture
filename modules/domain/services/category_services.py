from abc import ABC, abstractmethod
from modules.entities.Task import CategoryEntity


class BaseCategoryServices(ABC):
    @abstractmethod
    def create_category(self, category_id: int, title: str) -> CategoryEntity:
        ...

    @abstractmethod
    def update_category(self, title: str, category_id: int) -> None:
        ...

    @abstractmethod
    def delete_category(self, category_id: int) -> None:
        ...
