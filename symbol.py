from dataclasses import dataclass
from enum import Enum
import os
import drawsvg as draw
import argparse
import logging
import sys
from codeparity_gruvbox import Dark, Light


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)


@dataclass
class Choice:
    "a modal for choices of all squares"

    " doing a class thing to interact and update different choice squares"
    id: int
    rect: draw.Rectangle
    state: bool


def test_colors(d: draw.Drawing):
    start = 0
    for i, value in enumerate(Dark):
        y = (start + 1) * 10
        start = start + 1
        d.append(draw.Line(10, y, 390, y, stroke=value, stroke_width=10))


def test(d: draw.Drawing):
    x_33 = d.width // 3
    y_33 = d.height // 3
    p = draw.Path(stroke=Dark.gray_40_pc, fill="none", stroke_width=1)
    d.append(p.M(65, 65).Q(200, 133, 200, 200))


def make_square_logos(d: draw.Drawing):
    # line = draw.Line(0, 0, d.width, d.height, stroke=Dark.fg, stoke_width=5)
    x_33 = d.width // 3
    y_33 = d.height // 3
    # test_colors(d)
    # Curve only (left)
    # bg = Choice(0, 0, d.width, d.height, fill=Dark.bg, stroke=None)
    # d.append(bg)
    choices = list()

    rect_id = 0
    for x in range(3):
        for y in range(3):
            rect_id = rect_id + 1
            rect = draw.Rectangle(
                x * x_33,
                y * y_33,
                x * x_33 + x_33,
                y * y_33 + y_33,
                stroke=Dark.fg,
                stroke_width=1,
            )
            choice = Choice(rect_id, rect, False)
            choices.append(choice)
            # log.debug(choice)
            # now draw the middle points

    for choice in choices:
        d.append(choice.rect)
        log.debug(choice)
    test(d)
    # d.append(line)
    # test(d)


def create_svg(size: int, filename: str):
    # d = draw.Drawing(size, size, transform="scale(1,-1)")
    trans_form_cartesian = f"translate(0,{size}) scale(1,-1)"
    log.debug(trans_form_cartesian)
    d = draw.Drawing(size, size, transform=trans_form_cartesian)
    # d = draw.Drawing(size, size, origin=(-200, -200))
    # d = draw.Drawing(size, size, transform="translate(0,400) scale(1,-1)")
    # transform='translate(0,100) scale(1,-1)'
    # d = draw.Drawing(size, size)
    make_square_logos(d)
    d.save_svg(filename)
    log.info(f"Output file saved as {filename}")


def main(size: int, filename: str = "logos.svg"):
    create_svg(size, filename)
    os.system(f"feh {filename}")
    # os.system("feh example.svg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-size", help="size of the logo", type=int, default=400)
    args = parser.parse_args()
    if args.size:
        log.info("size is :" + str(args.size))
    main(args.size)
