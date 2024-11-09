from dataclasses import dataclass


@dataclass
class TaskEntity:
    id: int
    title: str
    description: str
    confirmed: bool

    def mark_as_completed(self):
        self.confirmed = True
        