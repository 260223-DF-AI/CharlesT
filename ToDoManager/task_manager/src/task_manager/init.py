"""Task Manager package - A simple CLI task management application."""

from ToDoManager.task_manager.src.task_manager.models.task import Task
from ToDoManager.task_manager.src.task_manager.utils.validators import validate_title, ValidationError
from ToDoManager.task_manager.src.task_manager.utils.formatters import format_task_list, format_date

__version__ = "1.0.0"
__all__ = [
    "Task",
    "validate_title",
    "ValidationError",
    "format_task_list",
    "format_date"
]