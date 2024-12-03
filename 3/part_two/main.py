import re

def main():
    content = ''
    with open('input.txt') as f:
        content = f.read()
    value_regexp = re.compile(r'mul\(([0-9]*),([0-9]*)\)')
    result = 0
    index = 0
    while index < len(content):
        end_do = content.find("don't()", index)
        if end_do != -1:
            do_sub = content[index:end_do]
            index = end_do
        else:
            do_sub = content[index:]
            index = len(content)
        print(f'usable sub : {do_sub}')
        mult_data = value_regexp.findall(do_sub)
        for multiplication in mult_data:
            result += int(multiplication[0])*int(multiplication[1])
        if index < len(content):
            index = content.find("do()", index)
            if index == -1:
                index = len(content)
    print(f'result: {result}')
    return True

if __name__ == '__main__':
    main()