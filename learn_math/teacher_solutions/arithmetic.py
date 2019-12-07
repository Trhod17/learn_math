"""Methods for computing arithmetic calculations"""
from typing import List, SupportsFloat

addition_list = [1.1, 2, 3, -4, 5]
subtraction_list = [100, 99, -123.123, 0]
multiplication_list = [2, 3, 5.5, -1]
division_list = [100, 2.5, -3]


def main():
    print(
        f"Answers:"
        f"\n\tAddition: {addition(x=addition_list)}"
        f"\n\tSubtraction: {subtraction(x=subtraction_list)}"
        f"\n\tMultiplcation: {multiplication(x=multiplication_list)}"
        f"\n\tDivision: {division(x=division_list)}"
    )


def addition(x: List[SupportsFloat]) -> SupportsFloat:
    return sum(x)


def subtraction(x: List[SupportsFloat]) -> SupportsFloat:
    value: SupportsFloat = x[0]
    for num in x[1:]:
        value -= num
    return value


def multiplication(x: List[SupportsFloat]) -> SupportsFloat:
    value: SupportsFloat = x[0]
    for num in x[1:]:
        value *= num
    return value


def division(x: List[SupportsFloat]) -> SupportsFloat:
    value: SupportsFloat = x[0]
    for num in x[1:]:
        value /= num
    return value


if __name__ == "__main__":
    main()
