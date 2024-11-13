from abc import ABC, abstractmethod
from typing import List

from modules.entities.Task import CategoryEntity


class BaseCategoryRepo(ABC):

    @abstractmethod
    def get_category(self, category_id: int) -> CategoryEntity:
        ...

    @abstractmethod
    def list_category(self) -> List[CategoryEntity]:
        ...

    @abstractmethod
    def save_category(self, category: CategoryEntity) -> None:
        ...

    @abstractmethod
    def delete_category(self, category_id: int) -> None:
        ...
