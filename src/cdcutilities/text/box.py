u_left: str = "\U0000256D"
u_right: str = "\U0000256E"
b_left: str = "\U00002570"
b_right: str = "\U0000256F"
vertical: str = "\U00002502"
horizontal: str = "\U00002500"
space: str = " "


def message_box(message: str, x_padding: int = 2):
    if x_padding % 2 != 0:
        raise ValueError(f"invalid x_padding {x_padding}, must be a multiple of 2")

    lines = message.split("\n")
    longest = len(max(lines, key=len))
    shortest = len(min(lines, key=len))

    print(f"{u_left}{horizontal * (longest + (x_padding * 2))}{u_right}")
    for line in lines:
        filler = longest - shortest if len(line) < longest else 0
        print(f"{vertical}{space * x_padding}{line}{space * (x_padding + filler)}{vertical}")
    print(f"{b_left}{horizontal * (longest + (x_padding * 2))}{b_right}")


def print_box_characters() -> None:
    print(f"{u_left=}")
    print(f"{u_right=}")
    print(f"{b_left=}")
    print(f"{b_right=}")
    print(f"{vertical=}")
    print(f"{horizontal=}")

    message_box("Unicode box characters.")


if __name__ == '__main__':
    print_box_characters()

    message_box("Hello, from Hollywood!", x_padding=6)
    message_box("Hello, from Hollywood!\nHello in T.V. Land!")
