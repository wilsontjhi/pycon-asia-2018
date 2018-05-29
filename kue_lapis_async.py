import asyncio
import colorama

from util import measure_elapsed_time, perform_operation, perform_io_operation_async


async def build_layer(tray):
    await start_mixer()
    pour_colour_mixture(colorama.Back.MAGENTA, tray)
    pour_colour_mixture(colorama.Back.GREEN, tray)
    pour_colour_mixture(colorama.Back.WHITE, tray)


async def start_mixer():
    await perform_io_operation_async(1.0)


def pour_colour_mixture(color, tray):
    perform_operation(0.005)
    tray.append(color + '               ')


@measure_elapsed_time
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(actual_main())


async def actual_main():
    tray = []
    awaitable = []
    for _ in range(4):
        awaitable.append(build_layer(tray))
    await asyncio.wait(awaitable)

    print(*[layer for layer in tray], sep='\n')


if __name__ == '__main__':
    colorama.init(autoreset=True)
    main()
