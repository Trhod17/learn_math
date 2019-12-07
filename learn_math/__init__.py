from .teacher_solutions.arithmetic import addition as teacher_addition
from .teacher_solutions.arithmetic import subtraction as teacher_subtraction
from .teacher_solutions.arithmetic import multiplication as teacher_multiplication
from .teacher_solutions.arithmetic import division as teacher_division
from .solutions.arithmetic import addition
from .solutions.arithmetic import subtraction
from .solutions.arithmetic import multiplication
from .solutions.arithmetic import division

__all__ = [
    "teacher_addition",
    "teacher_subtraction",
    "teacher_division",
    "teacher_multiplication",
    "addition",
    "subtraction",
    "multiplication",
    "division",
]