import dataclasses
from typing import Optional

from PyQt5.QtWidgets import QPushButton, QLabel, QDoubleSpinBox


@dataclasses.dataclass
class Task:
    name: str
    param_fields: list['ParamField']
    result_field: 'ResultField'
    button: 'FormButton'


@dataclasses.dataclass
class ParamField:
    name: str
    field: Optional[QDoubleSpinBox] = None


@dataclasses.dataclass
class ResultField:
    name: str
    field: Optional[QLabel] = None


@dataclasses.dataclass
class FormButton:
    name: str
    button: Optional[QPushButton] = None
