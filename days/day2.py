from aoc.Util import split_by_newline, tuplerize, Submarine


# Part 1
def firstPart(input: str):
    arr = tuplerize(split_by_newline(input))
    sub = Submarine()

    sub.move_in_sequence(arr)

    return sub.get_final_depth()

# Part 2
def secondPart(input: any, output: any):
    arr = tuplerize(split_by_newline(input))
    sub = Submarine()

    sub.set_aiming_mode(True)
    sub.move_in_sequence(arr)

    return sub.get_final_depth()


