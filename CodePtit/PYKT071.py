## SỐ KHÔNG GIẢM TRONG FILE NHỊ PHÂN

def readFile(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        return list(data)


def extract(data):
    a = []
    current_number = 0
    for byte in data:
        current_number = (current_number << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            a.append(current_number)
            current_number = 0
    return a


def count_occurrences(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts


def main():
    data1 = readFile("DATA1.in")
    data2 = readFile("DATA2.in")

    numbers1 = extract(data1)
    numbers2 = extract(data2)

    unique_numbers = set(numbers1) | set(numbers2)
    unique_numbers = sorted(unique_numbers)

    for number in unique_numbers:
        count1 = numbers1.count(number)
        count2 = numbers2.count(number)
        print(number, count1, count2)


if __name__ == "__main__":
    main()
