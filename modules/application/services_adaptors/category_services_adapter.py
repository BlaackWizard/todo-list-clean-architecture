from dataclasses import dataclass
from modules.domain.services.category_services import BaseCategoryServices
from modules.domain.repositories.category_repo import BaseCategoryRepo
from modules.entities.Task import CategoryEntity


@dataclass
class CategoryServicesAdapter(BaseCategoryServices):
    category_repo: BaseCategoryRepo

    def create_category(self, category_id: int, title: str) -> CategoryEntity:
        category = CategoryEntity(id=category_id, title=title)
        self.category_repo.save_category(category)
        return category

    def update_category(self, category_id: int, title: str) -> None:
        category = CategoryEntity(id=category_id, title=title)
        return self.category_repo.save_category(category)

    def delete_category(self, category_id: int) -> None:
        category = self.category_repo.get_category(category_id=category_id)
        return self.category_repo.delete_category(category)

