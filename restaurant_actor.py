import asyncio
import multiprocessing
from datetime import datetime

from util import measure_elapsed_time, perform_operation, perform_io_operation_async


class Actor(multiprocessing.Process):

    def __init__(self, input_queue, result_queue, action):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.result_queue = result_queue
        self.action = action

    def run(self):
        while True:
            input_param = self.input_queue.get()
            if input_param is None:
                self.result_queue.put(input_param)
                self.input_queue.task_done()
                break
            self.action(input_param)
            self.input_queue.task_done()
            self.result_queue.put(input_param)
        return


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


def prepare_order(_):
    policy = asyncio.get_event_loop_policy()
    policy.set_event_loop(policy.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(prepare_order_async(_))


async def prepare_order_async(_):
    awaiting_kue_lapis = prepare_kue_lapis()
    awaiting_milk_shake = prepare_milk_shake()
    prepare_sandwich()
    prepare_ice_cream()
    await asyncio.wait([awaiting_kue_lapis, awaiting_milk_shake])


@measure_elapsed_time
def main(num_of_user):
    customer_queue = multiprocessing.JoinableQueue()
    order_queue = multiprocessing.JoinableQueue()
    completed_queue = multiprocessing.Queue()

    cashier = Actor(customer_queue, order_queue, take_order)
    preparer1 = Actor(order_queue, completed_queue, prepare_order)
    preparer2 = Actor(order_queue, completed_queue, prepare_order)
    preparer3 = Actor(order_queue, completed_queue, prepare_order)
    preparer4 = Actor(order_queue, completed_queue, prepare_order)

    cashier.start()
    preparer1.start()
    preparer2.start()
    preparer3.start()
    preparer4.start()

    for user_no in range(num_of_user):
        customer_queue.put(user_no + 1)

    customer_queue.put(None)

    customer_queue.join()
    order_queue.join()

    for _ in range(num_of_user):
        result = completed_queue.get()

    cashier.terminate()
    preparer1.terminate()
    preparer2.terminate()
    preparer3.terminate()
    preparer4.terminate()


if __name__ == '__main__':
    total_num_of_customer = 12
    print('All customer comes at ', datetime.now())
    main(total_num_of_customer)
