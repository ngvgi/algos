def solution(N):
    zeros = 0
    ones = 0
    largest_gap = 0
    gap_size = 0

    bin_rep = str(bin(N)[2:])

    for i in range(len(bin_rep)):
        if bin_rep[i] == '1' and ones == 0:
            ones += 1

        if bin_rep[i] == '0' and ones > 0:
            zeros += 1

        if bin_rep[i] == '1' and ones > 0:
            gap_size = zeros
            zeros = 0
            ones = 1
            if gap_size > largest_gap:
                largest_gap = gap_size

    return largest_gap


""" def solution(N):
    return len(max(bin(N)[2:].strip('0').strip('1').split('1')))
 """

print('Enter a number: ')
num = int(input())
print('The binary equivalent of {} is {}. \nIt\'s binary gap is {}'.format(
    num, str(bin(num)[2:]), solution(num)))
