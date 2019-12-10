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
        f"\n\tMultiplication: {multiplication(x=multiplication_list)}"
        f"\n\tDivision: {division(x=division_list)}"
    )


def addition(x: List[TNum]) -> TNum:
    return sum(x)


def subtraction(x: List[TNum]) -> TNum:
    value: TNum = x[0]
    for num in x[1:]:
        value -= num
    return value


def multiplication(x: List[TNum]) -> TNum:
    value: TNum = x[0]
    for num in x[1:]:
        value *= num
    return value


def division(x: List[TNum]) -> TNum:
    value: TNum = x[0]
    for num in x[1:]:
        value /= num
    return value


if __name__ == "__main__":
    main()
