import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.boardsource_blok import pinout as pins
from kmk.scanners import DiodeOrientation
from kmk.scanners.square import SquareMatrixScanner


class KMKKeyboard(_KMKKeyboard):
    left_side_pins = [pins[7], pins[8], pins[9], pins[10], pins[11]]
    right_side_pins = [pins[16], pins[15], pins[14], pins[13], pins[12]]

    def __init__(self):
        # create and register the scanner
        self.matrix = [
            SquareMatrixScanner(pins=self.left_side_pins),
            SquareMatrixScanner(pins=self.right_side_pins, offset=100),
        ]

    diode_orientation = DiodeOrientation.COLUMNS
    data_pin = pins[1]
    rgb_pixel_pin = board.NEOPIXEL
    rgb_num_pixels = 1
    i2c = board.I2C

    # NOQA
    # flake8: noqa
    # fmt: off
    coord_mapping = [
        1, 2, 3, 4,  5, 30,29,28,27,26,
        7, 8, 9, 10,11, 36,35,34,33,32,
        13,14,15,16,17, 42,41,40,39,38,
              20,21,22, 47,46,45
    ]
