import re

def parse_data(data: str):
    list_a = []
    list_b = []
    get_numbers_expression = re.compile(r'\d+')
    lines = data.splitlines()
    for line in lines:
        numbers = get_numbers_expression.findall(line)
        print(numbers)
        if len(numbers) != 2:
            raise Exception("parsing error, too much argument on single line")
        list_a.append(int(numbers[0]))
        list_b.append(int(numbers[1]))
    return list_a, list_b

def main():
    input_file = open("input.txt", "r")
    input_content = input_file.read()
    input_file.close()
    list_a, list_b = parse_data(input_content)

    list_a.sort()
    list_b.sort()

    if len(list_a) != len(list_b):
        raise Exception("length of lists are different")

    print("Sorted lists :")
    distances = []
    for(num1, num2) in zip(list_a, list_b):
        print(num1, num2)
        distances.append(abs(num1 - num2))

    print("Distances :", distances)

    total_distance = sum(distances)
    print("Total distance :", total_distance)
    return True

if __name__ == '__main__':
    main()