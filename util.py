import csv
from datetime import datetime
import time

import os

import asyncio


def measure_elapsed_time(func):
    def function_wrapper(*args):
        start = datetime.now()
        func(*args)
        end = datetime.now()
        print('Total time of {} = {} seconds'.format(func.__name__, (end - start).total_seconds()))

    return function_wrapper


def perform_operation(unit_of_time=1.0):
    total_unit_of_time = int(unit_of_time * 1000000)
    for i in range(1, total_unit_of_time):
        for _ in range(18):
            _ = total_unit_of_time % i


def perform_io_operation(in_seconds=1):
    time.sleep(in_seconds)


async def perform_io_operation_async(in_seconds=1):
    await asyncio.sleep(in_seconds)
