from concurrent.futures import ThreadPoolExecutor

import colorama
from threading import Thread

from functools import reduce

from util import measure_elapsed_time, perform_operation, perform_io_operation


def build_layer(_):
    tray = []
    start_mixer()
    pour_colour_mixture(colorama.Back.MAGENTA, tray)
    pour_colour_mixture(colorama.Back.GREEN, tray)
    pour_colour_mixture(colorama.Back.WHITE, tray)
    return tray


def start_mixer():
    perform_io_operation(1.0)


def pour_colour_mixture(color, tray):
    perform_operation(0.005)
    tray.append(color + '               ')


@measure_elapsed_time
def main_pool():
    with ThreadPoolExecutor() as pool:
        result = pool.map(build_layer, range(4))
    final_tray = reduce(lambda acc, tray: acc + tray, result, [])

    print(*[layer for layer in final_tray], sep='\n')


if __name__ == '__main__':
    colorama.init(autoreset=True)
    main_pool()
