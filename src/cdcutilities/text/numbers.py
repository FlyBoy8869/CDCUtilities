"""Provides functions to format numbers in various ways."""

def commafy_number(number: str, *, separator: str = ",") -> str:
    """Separates a number into groups of three separated with separator.

    :param number: The number to group with separators.
    :param separator: The character to use as separator.
    :rtype: str
    :returns: String representation of number with separators inserted.

    >>> commafy_number("123")
    '123'

    >>> commafy_number("1234")
    '1,234'

    >>> commafy_number("1234567")
    '1,234,567'

    >>> commafy_number("1234", separator="_")
    '1_234'

    """

    if "." in number:
        whole_number, mantissa = number.split(".")
        mantissa = f".{mantissa}"
    else:
        whole_number = number
        mantissa = ""

    commafied_number = []
    if leader := len(whole_number) % 3:
        commafied_number.extend([whole_number[:leader], separator])

    for i in range(leader, len(whole_number), 3):
        segment = whole_number[i : i + 3]
        commafied_number.extend([segment, separator])
    commafied_number.pop()

    commafied_number_string = f"{"".join(commafied_number)}{mantissa}"

    return commafied_number_string
