from typing import Union

def pin_parse(value: str) -> Union[str, int]:
    prefix, pin = value.split("-")
    return prefix, int(pin)