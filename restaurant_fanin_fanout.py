from concurrent.futures import ProcessPoolExecutor
from datetime import datetime

import asyncio

from util import perform_operation, measure_elapsed_time, perform_io_operation_async


def take_order(_):
    print('customer {} was served at '.format(_), datetime.now())
    perform_operation(1)


async def prepare_kue_lapis():
    await perform_io_operation_async(2)
    perform_operation(1)


async def prepare_milk_shake():
    await perform_io_operation_async(1)
    perform_operation(0.5)


def prepare_ice_cream():
    perform_operation(0.5)


def prepare_sandwich():
    perform_operation(1)


@measure_elapsed_time
def main_multi_process(num_of_customer):
    with ProcessPoolExecutor(4) as pool:
        pool.map(prepare_order, range(num_of_customer))


def prepare_order(_):
    take_order(_)
    policy = asyncio.get_event_loop_policy()
    policy.set_event_loop(policy.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(prepare_food())


async def prepare_food():
    awaiting_kue_lapis = prepare_kue_lapis()
    awaiting_milk_shake = prepare_milk_shake()
    prepare_sandwich()
    prepare_ice_cream()
    await asyncio.wait([awaiting_kue_lapis, awaiting_milk_shake])


if __name__ == '__main__':
    total_num_of_customer = 12
    print('All customer comes at ', datetime.now())
    main_multi_process(total_num_of_customer)
