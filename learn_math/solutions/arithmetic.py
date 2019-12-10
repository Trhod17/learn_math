"""Methods for computing arithmetic calculations"""
from typing import List, TypeVar

addition_list = [1.1, 2, 3, -4, 5]
subtraction_list = [100, 99, -123.123, 0]
multiplication_list = [2, 3, 5.5, -1]
division_list = [100, 2.5, -3]

TNum = TypeVar('TNum', int, float)


def main() -> None:
    print(
        f"Answers:"
        f"\n\tAddition: {addition(x=addition_list)}"
        f"\n\tSubtraction: {subtraction(x=subtraction_list)}"
        f"\n\tMultiplcation: {multiplication(x=multiplication_list)}"
        f"\n\tDivision: {division(x=division_list)}"
    )


def addition(x: List[TNum]) -> TNum:
    pass


def subtraction(x: List[TNum]) -> TNum:
    pass


def multiplication(x: List[TNum]) -> TNum:
    pass


def division(x: List[TNum]) -> TNum:
    pass


if __name__ == "__main__":
    main()
