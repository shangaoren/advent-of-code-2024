#list_parser.py
import logging
import re

logger = logging.getLogger(__name__)

def parse_list(data: str):
    list_a = []
    list_b = []
    get_numbers_expression = re.compile(r'\d+')
    lines = data.splitlines()
    for line in lines:
        numbers = get_numbers_expression.findall(line)
        logger.debug(numbers)
        if len(numbers) != 2:
            raise Exception("parsing error, too much argument on single line")
        list_a.append(int(numbers[0]))
        list_b.append(int(numbers[1]))
    return list_a, list_b