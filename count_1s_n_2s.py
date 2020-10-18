def count_1s_n_2s():
    """adds every digit of numbers in a range
    until they are down to one digit,
    and check if there are more 1s or 2s.
    """
    number = int(input("Please enter a number: "))

    numOf1s = 0
    numOf2s = 0
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
                numOf1s += 1
            elif Sum == 2:
                twos_list.append(realnum)
                numOf2s += 1

    print(
        f'\nThere are "{numOf1s}" 1s and "{numOf2s}" 2s in the provided range.')

    if numOf1s > numOf2s:
        print(f'So there are more 1s than 2s.\n')
    elif numOf1s < numOf2s:
        print(f'So there are more 2s than 1s.\n')
    else:
        print(f'So there is an even number of 1s and 2s.\n')

    yes_or_no = input(
        f'If you want to see the numbers that lead to 1s and 2s between 0 and {number} please enter "Yes": ')
    if yes_or_no.lower() in ["yes", "y", ""]:
        print(
            f"\nThe numbers which lead to a 1 are: {ones_list} \n\nThe numbers which lead to a 2 are: {twos_list}")


count_1s_n_2s()
