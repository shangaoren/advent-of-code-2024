import logging
from unicodedata import lookup

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def isLineSafe(line :str) -> bool:
    levels = []
    # retrieve all levels from a line
    for level in line.split():
        levels.append(int(level))
    # init loop
    previous_level = levels[0]
    previous_variation = 0
    errors = []
    previous_error_count = 0
    for i in range(1, len(levels)):
        current_level = levels[i]
        variation = current_level - previous_level
        if abs(variation) > 3:
            errors.append(f'variation over 3 for line {levels} at {i}')
        if abs(variation) < 1:
            errors.append(f'variation inferior to 1 for line {levels} at {i}')
        if previous_variation > 0 and variation < 0:
            errors.append(f'variation change for line {levels} at {i}')
        if previous_variation < 0 and variation > 0:
            errors.append(f'variation change for line {levels} at {i}')
        if len(errors) > 1:
            logging.debug(f'too many errors for line {levels}: {errors}')
            return False
        if previous_error_count != len(errors):
            previous_error_count = len(errors)
        else :
            previous_variation = variation
            previous_level = current_level

    if len(errors) > 0:
        logging.debug(f'no fatal errors for line {levels}: {errors}')
    return True


def main():
    logging.basicConfig(level=logging.DEBUG)
    content = ''
    with open('input.txt', 'r') as file:
        content = file.read()
    lines = content.splitlines()
    safe_report_count = 0
    for line in lines:
        if isLineSafe(line):
            safe_report_count += 1
    print(f'safe report count: {safe_report_count}')
    return True

if __name__ == '__main__':
    main()