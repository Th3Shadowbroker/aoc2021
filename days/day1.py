from aoc.Util import split_by_newline, map_to_int_list

# Part 1
def firstPart(input: str):
    arr = map_to_int_list(split_by_newline(input))
    counter = 0

    previous = None
    for next in arr:
        if previous is not None:
            if previous < next:
                counter += 1
            previous = next
        else:
            previous = next

    return counter

# Part 2
def secondPart(input: any, output: any):
    arr = map_to_int_list(split_by_newline(input))

    counter = 0

    previous = None
    for i in range(1, len(arr) - 1):
        x = arr[i - 1]
        y = arr[i]
        z = arr[i + 1]

        current = x + y + z

        if previous is not None:
            if previous < current:
                counter += 1
            previous = current
        else:
            previous = current

    return counter
