import random

def fall_asleep():
    numbers_from_input = [n.rstrip() for n in open('c-input.in')]
    test_cases = int(input("Enter T test cases: "))
    list_of_numbers = numbers_from_input[:test_cases]

    for n in list_of_numbers:
        count_to_sleep(int(n))


def count_to_sleep(number):
    list_of_digits = []
    matrix_head = []
    last_number_before_sleep = ""

    for i in range(201):
        matrix_head.append([])
        for j in range(201):
            num = i * j
            matrix_head[i].append(str(num))

    for num in matrix_head[number]:

        if len(num) == 1:
            if num not in list_of_digits:
                list_of_digits.append(num)
        else:
            for d in num:
                if d not in list_of_digits:
                    list_of_digits.append(d)

    print(list_of_digits)

    if len(list_of_digits) == 10:
        print("SLEEP")

    else:
        print("INSOMNIA")

if __name__ == "__main__":
    fall_asleep()