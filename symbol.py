import os
import drawsvg as draw
import argparse
import logging
import sys
from codeparity_gruvbox import Dark, Light


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)


def make_square_logos(d: draw.Drawing):
    x_33 = d.width // 3
    y_33 = d.height // 3

    line = draw.Line(0, 0, d.width, d.height, stroke="black")
    d.append(line)


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
