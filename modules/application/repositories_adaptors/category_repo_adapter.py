from dataclasses import dataclass
from typing import List

from modules.domain.repositories.category_repo import BaseCategoryRepo
from modules.entities.Task import CategoryEntity


@dataclass
class CategoryRepoAdapter:
    category_repo: BaseCategoryRepo

    def get_category_by_id(self, category_id: int):
        category = self.category_repo.get_category(category_id=category_id)
        if category:
            return CategoryEntity(
                id=category.id,
                title=category.title
            )
        return {'error': 'Category not found'}

    def list_category(self) -> List[CategoryEntity]:
        categories = self.category_repo.list_category()
        return [self._to_entity(category) for category in categories]

    def save_category(self, category: CategoryEntity):
        return self.category_repo.save_category(category)

    def delete_category(self, category: CategoryEntity):
        return self.category_repo.delete_category(category)

    def _to_entity(self, category):
        return CategoryEntity(
            id=category.id,
            title=category.title
        )
