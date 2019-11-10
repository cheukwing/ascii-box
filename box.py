import argparse


def box(w: int, h: int) -> str:
    """Returns a string representation of a box, with the given width and height.

    e.g. box(4, 4)
    ┌--┐
    |  |
    |  |
    └--┘
    """

    # The minimum we can return is a box which is just corners, there are no
    # other legal characters which would be suitable and unambiguous.
    if w < 2 or h < 2:
        raise ValueError(
            f"Box cannot be drawn with dimensions {w}x{h}; boxes must have dimensions at least 2x2")

    # The dimensions of the 'gap' in the box, by removing corners
    centre_cols = w - 2
    centre_rows = h - 2

    horizontal_edge = '-' * centre_cols
    result = f"┌{horizontal_edge}┐\n"

    centre_spaces = ' ' * centre_cols
    result += f"|{centre_spaces}|\n" * centre_rows

    result += f"└{horizontal_edge}┘"
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('width', type=int, help='width of the box to draw')
    parser.add_argument('height', type=int, help='height of the box to draw')
    args = parser.parse_args()
    print(box(args.width, args.height))


if __name__ == '__main__':
    main()
