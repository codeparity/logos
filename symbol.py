import os
import drawsvg as draw
import argparse
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)


def create_svg(size: int, filename: str):
    d = draw.Drawing(size, size, origin="center")
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
