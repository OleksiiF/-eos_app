import json
import logging
from typing import List, Union


class Validator:
    """
    Provides functionality for checking the basic parameters of an object.
    """
    def __init__(self, array_dimensions: int, array_element_type: str):
        # this way more safety than eval()
        self.check_types = {
            'int': int,
            'str': str
        }
        self.array_dimensions = array_dimensions
        self.array_element_type = array_element_type
        self.__array = None

    @property
    def array(self):
        return self.__array

    def set_array(self, potential_list: str):
        try:
            array: List = json.loads(potential_list)
            target_type: Union[int, str] = self.check_types[self.array_element_type]

            if not isinstance(array, list):
                logging.error('Object is not array')
                raise TypeError

            if not self.__is_correct_array_parameters(
                array, self.array_dimensions, target_type
                ):
                    logging.error('Array contain not proper data')
                    raise ValueError

            self.__array = array
            logging.info('Property was created.')

        except (json.decoder.JSONDecodeError, TypeError, ValueError):
            # Protected from collisions of values
            # validator can be used several times.
            self.__array = None
            logging.error(
                f'You should provide an array, contains elements of '
                f'{self.array_element_type} type, with '
                f'{self.array_dimensions} dimensions. '
                f'Property was not created.'
            )
            return False

        return True

    def __is_correct_array_parameters(
        self, array: List,
        dimensions: int,
        target_type: Union[int, str]
    ) -> bool:
        """
        Validate array parameters such as dimensions(not less, not greater)
        and elements type.

        :param array: list for check
        :param dimensions: proper dimensions of array
        :param target_type: type of elements inside array
        :return: result of checking
        """
        for element in array:
            if isinstance(element, list):
                # Check that the array dimensions is not greater than the specified size
                if dimensions != 1 and (
                    self.__is_correct_array_parameters(
                        element, dimensions-1, target_type
                )):
                    continue

            elif isinstance(element, target_type) and dimensions == 1:
                continue

            return False

            # there is no else-block, because element type and not less
            # dimensions size was check at elif-block.

        return True
