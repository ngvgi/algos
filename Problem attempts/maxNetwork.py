from typing import List


def maxNetwork(starts: List[int], ends: List[int]) -> int:
    roads_dict = {city: [] for city in starts}

    for i in range(len(starts)):
        roads_dict[starts[i]].append((starts[i], ends[i]))

    for i in range(len(ends)):
        if ends[i] in roads_dict:
            roads_dict[ends[i]].append((ends[i], starts[i]))
            continue
        roads_dict[ends[i]] = [(ends[i], starts[i])]

    max_net = 0
    current_max = 0
    roads = 0
    duplicates = 0
    city_one = 1
    city_two = city_one + 1

    while city_one < len(starts):

        roads += len(roads_dict[city_one])

        for i in roads_dict[city_two]:
            if (i[1], i[0]) in roads_dict[city_one]:
                duplicates += 1
            roads += 1

        current_max = roads - duplicates

        if current_max > max_net:
            max_net = current_max

        city_two += 1
        roads = 0
        duplicates = 0
        if city_two > len(starts):
            city_one += 1
            city_two = city_one + 1

    return max_net


starts = [1, 2, 3, 3]
ends = [2, 3, 1, 4]
print(maxNetwork(starts, ends))
