""" 
steps:
    1.convert number to string in order to count its digits
    2. if the number's total digit count is less than 2, return 0
    3. if the number has more than 2 digits:
        convert the first digit to a one
        replace all following place values with zero
"""


def solution(N):
    # if number has less than two digits, return 0
    num_str = str(N)

    if len(num_str) < 2:
        return 0

    # if number has more than two digits, return first digit, followed by zeros
    else:
        # if first digit > 1, then its smallest possible value is 1
        if(num_str[0] > '1'):
            num_str = '1' + num_str[1:]

        # zeros to be padded after first digit
        padding_zeros = len(num_str) - 1

        # pad the zeros after first digit
        smallest_num_str = num_str[0] + '0' * padding_zeros

        # convert the smallest_num string to int and return
        smallest_num = int(smallest_num_str)

        return smallest_num


print(solution(56433))
