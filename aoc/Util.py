#
#   Common
#
def split_by_newline(input: str, allow_empty: bool = False) -> list[str]:
    splitted = input.split("\n")
    if not allow_empty:
        splitted = list(filter(lambda x : x != '', splitted))
    return splitted

def map_to_int_list(input: list[str]) -> list[int]:
    return list(map(lambda x : int(x),input))

def tuplerize(input: list[str]) -> list[(str, int)]:
    tuples = []

    for line in input:
        splitted = line.split(' ')
        tuples.append( (splitted[0], int(splitted[1])) )

    return tuples

#
#   Day 2
#
from enum import Enum

class Direction(Enum):

    FORWARD = "forward"
    UP = "up"
    DOWN = "down"

class Submarine:

    def __init__(self, x: int = 0, y: int = 0, aim: int = 0) -> None:
        self.__horizontal = x
        self.__depth = y
        self.__aim = aim
        self.__aiming = False

    def move(self, direction: Direction, amount: int):
        if direction == Direction.FORWARD:
            self.__horizontal += amount

            if self.__aiming:
                self.__depth += self.__aim * amount
        
        elif direction == Direction.DOWN:
            if not self.__aiming:
                self.__depth += amount
            else:
                self.__aim += amount

        elif direction == Direction.UP:
            if not self.__aiming:
                self.__depth -= amount
            else:
                self.__aim -= amount

    def move_in_sequence(self, seq: list[(str, int)]):
        for order in seq:
            self.move(direction=Direction[order[0].upper()], amount=order[1])

    def set_aiming_mode(self, value: bool):
        self.__aiming = True

    def get_final_depth(self):
        return self.__horizontal * self.__depth

