"""Provides functions to format numbers in various ways."""
import itertools as it


def commafy_number(number: str) -> str:
    """Adds commas to a number.

    :param number: The number to add commas to.
    :rtype: str
    :returns: String representation of number with commas inserted.

    >>> commafy_number("0")
    '0'

    >>> commafy_number("-0")
    '-0'

    >>> commafy_number("1")
    '1'

   >>> commafy_number("-1")
   '-1'

    >>> commafy_number("123")
    '123'

    >>> commafy_number("-123")
    '-123'

    >>> commafy_number("1234")
    '1,234'

    >>> commafy_number("-1234")
    '-1,234'

    >>> commafy_number("12345")
    '12,345'

    >>> commafy_number("-12345")
    '-12,345'

    >>> commafy_number("1234567")
    '1,234,567'

    >>> commafy_number("-1234567")
    '-1,234,567'

    """

    import time

    if not isinstance(number, str):
        raise TypeError("The input must be a string.")

    try:
        int(number)
    except ValueError:
        raise ValueError("The input can not be converted to a number.")

    start_time = time.time()
    if len(number) <= 3:
        return number

    prefix = ""

    if number[0] == "-":
        number = number.replace("-", "")
        prefix = "-"

    if len(number) <= 3:
        return prefix + number

    s = ""
    for i, c in enumerate(number[::-1]):
        if i % 3 == 0 and i != 0:
            s += f",{c}"
        else:
            s += c

    print(f"elapsed time: {time.time() - start_time}")
    return prefix + s[::-1]


if __name__ == "__main__":
    import sys

    print(commafy_number(sys.argv[1]))
