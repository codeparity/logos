from enum import Enum
import os
import drawsvg as draw
import argparse
import logging
import sys
from codeparity_gruvbox import Dark, Light


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)


class Choice(draw.Rectangle):
    def __init__(self, x, y, width, height, **kwargs):
        super().__init__(x, y, width, height, **kwargs)

        # do calculations here
        self.mid_x = x + width // 2
        self.mid_y = y + height // 2


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
    d.append(p.M(0, 0).Q(x_33, y_33, 400, 300))


def make_bg_squares(d: draw.Drawing):
    x_33 = d.width // 3
    y_33 = d.height // 3
    # test_colors(d)
    # Curve only (left)
    bg = Choice(0, 0, d.width, d.height, fill=Dark.bg, stroke=None)
    d.append(bg)
    for x in range(0, d.width, x_33):
        for y in range(0, d.height, y_33):
            rect = draw.Rectangle(
                x, y, x + x_33, y + y_33, stroke=Dark.fg, stroke_width=1
            )
            d.append(rect)
            # now draw the middle points
    test(d)


def make_square_logos(d: draw.Drawing):
    # line = draw.Line(0, 0, d.width, d.height, stroke=Dark.fg, stoke_width=5)
    # d.append(line)
    # test(d)
    make_bg_squares(d)


def create_svg(size: int, filename: str):
    # d = draw.Drawing(size, size, transform="scale(1,-1)")
    trans_form_cartesian = f"translate(0,{size}) scale(1,-1)"
    log.debug(trans_form_cartesian)
    d = draw.Drawing(size, size, transform=trans_form_cartesian)
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
