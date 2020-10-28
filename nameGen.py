def nameGen(name):
    first = 0
    second = 1

    while first < len(name) - 1:

        print(name[:first].lower() + name[first].upper() +
              name[first + 1:second].lower() + name[second:].capitalize())
        second += 1

        if second == len(name):
            first += 1
            second = first + 1


print(nameGen('alaia'))