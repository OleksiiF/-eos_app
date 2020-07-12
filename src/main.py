#!/usr/bin/env python3
import logging
from argparse import Namespace, ArgumentParser

from array_handler import Saver, Validator


logging.basicConfig(level=logging.INFO)


def get_arg_parser() -> ArgumentParser:
    """
    Provides a parser of arguments entered when the module starts.

    :return: parser object
    """
    parser = ArgumentParser()
    parser.add_argument('path', help='path to file creating')
    parser.add_argument('array', help='the array which will be save')
    parser.add_argument(
        '-t',
        '--type',
        help='set up type of elements inside array',
        default='int'
    )
    parser.add_argument(
        '-d',
        '--dimensions',
        help='set up dimensions of the array',
        type=int,
        default=2
    )

    return parser


def save_array(
    str_array: str,
    file_path: str,
    array_dimensions: int,
    elements_type: str
):
    """
    Checks and saves the string representation of the array to a
    file at the requested path

    :param str_array: array string representation
    :param file_path: path to the file to which the object will be saved
    :param array_dimensions: parameter required for array  validation
    :param elements_type: parameter required for array validation
    """
    validator = Validator(array_dimensions, elements_type)
    saver = Saver()

    if validator.set_array(str_array) and (
        saver.array_save(file_path, validator.array)
    ):
        logging.info('Uhuu!')

    else:
        logging.warning("D'oh!")


if __name__ == '__main__':
    arg_parser: ArgumentParser = get_arg_parser()
    args: Namespace = arg_parser.parse_args()

    save_array(
        args.array, args.path, args.dimensions, args.type
    )
