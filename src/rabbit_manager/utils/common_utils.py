from typing import Any, Type, Tuple


def validate_type(
        value: Any,
        expected_type: Type,
        nullable: bool = False,
) -> None:
    if nullable and value is None:
        return
    if not isinstance(value, expected_type):
        raise TypeError(f"Expecting #{expected_type.__name__} but got #{type(value).__name__}")


def validate_type_list(
        value: Any,
        expected_type_list: Tuple[Type, ...],
        nullable: bool = False,
) -> None:
    if nullable and value is None:
        return
    if not isinstance(value, expected_type_list):
        raise TypeError("Expecting {} but got {}".format(
            ", ".join([
                expected_type.__name__
                for expected_type in expected_type_list
            ]),
            type(value).__name__,
        ))
