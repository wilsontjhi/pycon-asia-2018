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


def split(file_path, row_limit=10000,
          output_name_template='output_%s.csv', output_path='.', keep_headers=True):
    """
    Splits a CSV file into multiple pieces.

    A quick bastardization of the Python CSV library.
    Arguments:
        `row_limit`: The number of rows you want in each output file. 10,000 by default.
        `output_name_template`: A %s-style template for the numbered output files.
        `output_path`: Where to stick the output files.
        `keep_headers`: Whether or not to print the headers in each output file.
    Example usage:

        >> from toolbox import csv_splitter;
        >> csv_splitter.split(open('/home/ben/input.csv', 'r'));

    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError()

    if os.stat(file_path).st_size == 0:
        raise ValueError("File cannot be empty")

    with open(file_path) as file_handler:
        reader = csv.reader(file_handler)
        current_piece = 1
        current_out_path = os.path.join(
            output_path,
            output_name_template % current_piece
        )

        current_out_file_handler = open(current_out_path, 'w')

        current_out_writer = csv.writer(current_out_file_handler)
        current_limit = row_limit
        headers = next(reader)
        if keep_headers:
            current_out_writer.writerow(headers)

        created_file_paths = [current_out_path]

        for i, row in enumerate(reader):
            if i + 1 > current_limit:
                current_piece += 1
                current_limit = row_limit * current_piece
                current_out_path = os.path.join(
                    output_path,
                    output_name_template % current_piece
                )
                created_file_paths.append(current_out_path)
                current_out_file_handler.close()
                current_out_file_handler = open(current_out_path, 'w')
                current_out_writer = csv.writer(current_out_file_handler)
                if keep_headers:
                    current_out_writer.writerow(headers)
            current_out_writer.writerow(row)

        current_out_file_handler.close()
        return created_file_paths
