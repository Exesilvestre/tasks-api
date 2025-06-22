class InvalidPriorityException(Exception):
    def __init__(self, value: str):
        self.message = f"Invalid priority: '{value}'. Must be one of ['low', 'medium', 'high']."
        super().__init__(self.message)


class InvalidStatusException(Exception):
    def __init__(self, value: str):
        self.message = f"Invalid status: '{value}'. Must be one of ['pending', 'in_progress', 'done']."
        super().__init__(self.message)


class InvalidPercentageException(Exception):
    def __init__(self, value):
        self.message = f"Invalid percentage_finalized: '{value}'. Must be a float between 0.0 and 1.0."
        super().__init__(self.message)


class TaskAlreadyExistsException(Exception):
    def __init__(self, name: str):
        self.message = f"Task with name '{name}' already exists."
        super().__init__(self.message)


class TaskNotFoundException(Exception):
    def __init__(self, task_id: int):
        self.message = f"Task with ID '{task_id}' not found."
        super().__init__(self.message)
