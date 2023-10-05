import copy
import dataclasses
from typing import Callable

from data_structures import Task
import logic


def bind_logic_to_interface(tasks: list[Task]) -> list[Task]:

    def create_calculate(task: Task) -> Callable[[None], None]:
        def calculate():
            params = {
                param_field.name: param_field.field.value()
                for param_field in task.param_fields
            }
            result = logic.calculate(task.name, params)
            task.result_field.field.setText(result)
        return calculate

    for task in tasks:
        task.button.button.clicked.connect(create_calculate(task))
    return tasks
