""" 
    1. Replace all features with their int equivalent
    2. Right pass of XOR operation of all values to each other:
            count number of 1s in the result
            if number of 1's  == 1:
                similar_count ++     
            right[i] = similar_count 
            i++    
    3. Left pass of XOR operation of all values to each other:
            count number of 1s in the result
            if number of 1's  == 1:
                similar_count ++     
            left[i] = similar_count
            i++
    5. Add the left and right arrays, return this answer

"""
""" 
    Brian Kernighan's algorithm for counting 1's in binary string
"""


def count_1s(n):
    count = 0
    while (n):
        n &= (n - 1)
        count += 1
    return count


def solution(cars):
    if len(cars) == 1:
        return [1]

    if len(cars) < 1:
        return 'No cars'

    cars = [int(car, 2) for car in cars]
    right = [0] * len(cars)
    left = [0] * len(cars)

    current_idx = 0
    next_idx = 1
    similar_cars = 0
    while current_idx < len(cars) - 1:
        xor = cars[current_idx] ^ cars[next_idx]
        ones = count_1s(xor)
        if ones == 1 or ones == 0:
            similar_cars += 1
        next_idx += 1
        if next_idx == len(cars):
            right[current_idx] = similar_cars
            current_idx += 1
            next_idx = current_idx + 1
            similar_cars = 0

    current_idx = len(cars) - 1
    prev_idx = len(cars) - 2
    similar_cars = 0
    while current_idx > 0:
        xor = cars[current_idx] ^ cars[prev_idx]
        ones = count_1s(xor)
        if ones == 1 or ones == 0:
            similar_cars += 1
        prev_idx -= 1
        if prev_idx == -1:
            left[current_idx] = similar_cars
            current_idx -= 1
            prev_idx = current_idx - 1
            similar_cars = 0

    result = [a + b for a, b in zip(left, right)]
    return result


cars = ["0011", "0111", "0111", "0110", "0000"]
ans = solution(cars)
print(ans)