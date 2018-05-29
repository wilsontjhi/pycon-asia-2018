import colorama
from threading import Thread

from util import measure_elapsed_time, perform_operation, perform_io_operation


def build_layer(tray, index):
    start_index = 3 * index
    start_mixer()
    pour_colour_mixture(colorama.Back.MAGENTA, tray, start_index)
    pour_colour_mixture(colorama.Back.GREEN, tray, start_index + 1)
    pour_colour_mixture(colorama.Back.WHITE, tray, start_index + 2)


def start_mixer():
    perform_io_operation(1.0)


def pour_colour_mixture(color, tray, index):
    perform_operation(0.005)
    tray.append((index, color + '               '))


@measure_elapsed_time
def main_thread():
    position_colour_tray = []
    threads = []
    for index in range(4):
        t = Thread(target=build_layer, args=(position_colour_tray, index))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    print('Incorrect:')
    print(*[layer[1] for layer in position_colour_tray], sep='\n')

    final_tray = order_by_position(position_colour_tray)
    print('Corrected:')
    print(*[layer for layer in final_tray], sep='\n')


def order_by_position(position_colour_tray):
    return [value[1] for value in sorted(position_colour_tray, key=lambda v: v[0])]


if __name__ == '__main__':
    colorama.init(autoreset=True)
    main_thread()
