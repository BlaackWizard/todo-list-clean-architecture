from dataclasses import dataclass


@dataclass
class CategoryEntity:
    title: str


@dataclass
class TaskEntity:
    id: int  # noqa
    title: str
    description: str
    confirmed: bool
    category: CategoryEntity

    def mark_as_completed(self):
        self.confirmed = True

