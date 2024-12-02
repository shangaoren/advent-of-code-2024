import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def isLineSafe(line :str) -> bool:
    levels = []
    # retrieve all levels from a line
    for level in line.split():
        levels.append(int(level))
    # init loop
    current_level = levels[0]
    current_way = 0
    for i in range(1, len(levels)):
        previous_level = current_level
        current_level = levels[i]
        variation = current_level - previous_level
        if abs(variation) > 3:
            return False
        if abs(variation) < 1:
            return False
        if current_way == 0:
            current_way = 1 if variation > 0 else -1
        if variation > 0 > current_way:
            return False
        if variation < 0 < current_way:
            return False
    return True





def main():
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