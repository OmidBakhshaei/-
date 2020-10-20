import time
start_time = time.time()


def count_1s_n_2s(number):
    """adds every digit of numbers in a range
    until they are down to one digit,
    and check if there are more 1s or 2s.
    """
#     number = int(input("Please enter a number: "))
    if number == 0 or not isinstance(number, int):
        raise ValueError("Your input is not valid!")

    ones_list = []
    twos_list = []

    for num in range(1, number):
        realnum = num
        Sum = 0
        # add all the digits of a number until they are down to one digit.
        while Sum > 9 or Sum == 0:
            # convert the number to a string and then again to an integer.
            Sum = sum([int(i) for i in str(num)])
            num = Sum
            if Sum == 1:
                ones_list.append(realnum)
            elif Sum == 2:
                twos_list.append(realnum)

    if len(ones_list) > len(twos_list):
        return f'There are more 1s than 2s.\n'
    elif len(ones_list) < len(twos_list):
        return f'There are more 2s than 1s.\n'
    else:
        return f'There is an even number of 1s and 2s({len(ones_list)}).\n'


print(count_1s_n_2s(1000))

print("--- %s seconds ---" % (time.time() - start_time))
