from dataclasses import dataclass

@dataclass
class TaskEntity:
    id: int  # noqa
    title: str
    description: str
    confirmed: bool
    category: str

    def mark_as_completed(self):
        self.confirmed = True

