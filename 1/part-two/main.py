import sys

import list_parser
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def main():
    logging.basicConfig(level=logging.DEBUG)
    file = open('input.txt', 'r')
    input_data = file.read()
    file.close()

    list_a, list_b = list_parser.parse_list(input_data)

    similarity_score = 0
    for num in list_a:
        iteration_of_num_in_list_b = list_b.count(num)
        logger.debug(f'{num} is present {iteration_of_num_in_list_b} times in list b')
        similarity_score += iteration_of_num_in_list_b * num
        logger.debug(f'current similarity score is : {similarity_score}')

    print("final similarity score is", similarity_score)

if __name__ == '__main__':
    main()