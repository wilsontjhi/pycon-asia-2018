import colorama
from threading import Thread
from multiprocessing import Process, Queue

from util import measure_elapsed_time, perform_operation, perform_io_operation, perform_io_operation_async


def build_layer(tray, result):
    start_mixer()
    pour_colour_mixture(colorama.Back.MAGENTA, tray)
    pour_colour_mixture(colorama.Back.GREEN, tray)
    pour_colour_mixture(colorama.Back.WHITE, tray)

    result.put(tray)


def start_mixer():
    perform_operation(1.0)


def pour_colour_mixture(color, tray):
    perform_operation(0.005)
    tray.append(color + '               ')


@measure_elapsed_time
def main_process():
    tray = []
    processes = []
    result = Queue()
    for _ in range(4):
        p = Process(target=build_layer, args=(tray, result))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

    final_tray = []
    while not result.empty():
        final_tray = final_tray + result.get()
    print(*[layer for layer in final_tray], sep='\n')


if __name__ == '__main__':
    colorama.init(autoreset=True)
    main_process()
