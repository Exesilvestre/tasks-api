# create exceptions
class TaskListAlreadyExistsException(Exception):
    def __init__(self, name: str):
        self.message = f"Task list with name '{name}' already exists."
        super().__init__(self.message)


class TaskListNameEmptyException(Exception):
    def __init__(self):
        self.message = "Task list name cannot be empty."
        super().__init__(self.message)


# Get by id exceptions
class TaskListNotFoundException(Exception):
    def __init__(self, list_id: int):
        self.message = f"Task list with ID '{list_id}' not found."
        super().__init__(self.message)
