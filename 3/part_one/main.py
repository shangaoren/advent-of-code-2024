import re

def main():
    content = ''
    with open('input.txt') as f:
        content = f.read()
    value_regexp = re.compile(r'mul\(([0-9]*),([0-9]*)\)')
    values = re.findall(value_regexp, content)
    print(values)
    result = 0
    for tuple_values in values:
        result += int(tuple_values[0])*int(tuple_values[1])
    print(f'final result {result}')
    return True

if __name__ == '__main__':
    main()