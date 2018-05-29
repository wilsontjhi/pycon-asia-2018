from concurrent.futures import ProcessPoolExecutor
from datetime import datetime

from util import perform_io_operation, perform_operation, measure_elapsed_time


def take_order(_):
    print('customer {} was served at '.format(_), datetime.now())
    perform_operation(1)


def prepare_kue_lapis():
    perform_io_operation(2)
    perform_operation(1)


def prepare_milk_shake():
    perform_io_operation(1)
    perform_operation(0.5)


def prepare_ice_cream():
    perform_operation(0.5)


def prepare_sandwich():
    perform_operation(1)


@measure_elapsed_time
def main(num_of_customer):
    for _ in range(num_of_customer):
        prepare_order(_)


@measure_elapsed_time
def main_multi_process(num_of_customer):
    with ProcessPoolExecutor(4) as pool:
        pool.map(prepare_order, range(num_of_customer))


def prepare_order(_):
    take_order(_)
    prepare_sandwich()
    prepare_kue_lapis()
    prepare_ice_cream()
    prepare_milk_shake()


if __name__ == '__main__':
    total_num_of_customer = 12
    # print('All customer comes at ', datetime.now())
    # main(total_num_of_customer)
    print('All customer comes at ', datetime.now())
    main_multi_process(total_num_of_customer)
