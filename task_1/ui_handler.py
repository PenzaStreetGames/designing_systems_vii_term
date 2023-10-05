from data_structures import Task, ParamField, FormButton, ResultField

from PyQt5.QtWidgets import QPushButton, QLabel, QDoubleSpinBox
from PyQt5.QtCore import QObject


def get_interface_stub() -> list[Task]:
    return [
        Task(
            name="task_23",
            param_fields=[
                ParamField(name="x"),
                ParamField(name="y")
            ],
            result_field=ResultField(name="z"),
            button=FormButton(name="button")
        ),
        Task(
            name="task_26",
            param_fields=[
                ParamField(name="x"),
                ParamField(name="y")
            ],
            result_field=ResultField(name="z"),
            button=FormButton(name="button")
        ),
        Task(
            name="task_29",
            param_fields=[
                ParamField(name="x"),
                ParamField(name="k1"),
                ParamField(name="k2"),
            ],
            result_field=ResultField(name="z"),
            button=FormButton(name="button")
        ),
        Task(
            name="task_2",
            param_fields=[
                ParamField(name="x"),
                ParamField(name="y"),
                ParamField(name="z"),
            ],
            result_field=ResultField(name="min"),
            button=FormButton(name="button")
        ),
        Task(
            name="task_5",
            param_fields=[
                ParamField(name="x1"),
                ParamField(name="y1"),
                ParamField(name="x2"),
                ParamField(name="y2"),
                ParamField(name="x3"),
                ParamField(name="y3")
            ],
            result_field=ResultField(name="s"),
            button=FormButton(name="button")
        ),
    ]


def find_interface_elements(
        root_elem: QObject, tasks: list[Task]
) -> list[Task]:
    for task in tasks:
        for param_field in task.param_fields:
            param_field_name = f"{task.name}_{param_field.name}"
            param_field.field = root_elem.findChild(
                QDoubleSpinBox, param_field_name
            )
        result_field_name = f"{task.name}_{task.result_field.name}"
        task.result_field.field = root_elem.findChild(
            QLabel, result_field_name
        )
        form_button_name = f"{task.name}_{task.button.name}"
        task.button.button = root_elem.findChild(QPushButton, form_button_name)
    return tasks
