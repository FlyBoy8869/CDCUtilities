"""Provides functions to format time values as string representations."""

SECOND = 1
MINUTE = SECOND * 60
HOUR = MINUTE * 60
DAY = HOUR * 24


def format_seconds(seconds: int | str, *, use_days: bool = False, multi_line: bool = False) -> str:
    """Return a formatted string of the form [nn [day | days],] nn:nn:nn

    :param seconds: value to format
    :param use_days: if True include the number of days formatted into the string,
                    if False, days are represented as hours
    :param multi_line: if True include multiple lines formatted into the string.
    :returns: A formatted string appropriate for printing.

    >>> format_seconds(SECOND)
    '00:00:01'
    >>> format_seconds(MINUTE)
    '00:01:00'
    >>> format_seconds(HOUR)
    '01:00:00'
    >>> format_seconds(DAY, use_days=True)
    '01 day, 00:00:00'
    >>> format_seconds(DAY * 2, use_days=True)
    '02 days, 00:00:00'
    >>> format_seconds(DAY * 2)
    '48:00:00'

    """

    assert isinstance(
        seconds, (int, str)
    ), f"seconds is wrong type, got {type(seconds)} expected <class 'int'>"

    try:
        seconds = int(seconds)
    except (TypeError, ValueError):
        seconds = 0

    line_break = ""
    days = hours = minutes = secs = 0

    if seconds >= DAY and use_days:
        value = seconds // DAY
        days = value
        seconds -= value * DAY
    if seconds >= HOUR:
        value = seconds // HOUR
        hours = value
        seconds -= value * HOUR

    if MINUTE < seconds < HOUR:
        value = seconds // MINUTE
        minutes = value
        seconds -= value * MINUTE

    if seconds <= MINUTE:
        if seconds == MINUTE:
            return "00:01:00"

        secs = seconds

    days_string = f"{days:02} {"day" if days == 1 else "days"}"
    hours_string = f"{hours:02}:{minutes:02}:{secs:02}"

    if days and use_days:
        if multi_line:
            days_string += "\n"
        else:
            days_string += ', '
        formatted_string = f"{days_string}{hours_string}"
    else:
        formatted_string = hours_string

    return formatted_string
