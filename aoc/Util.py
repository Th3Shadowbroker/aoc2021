def split_by_newline(input: str, allow_empty: bool = False) -> list[str]:
    splitted = input.split("\n")
    if not allow_empty:
        splitted = list(filter(lambda x : x != '', splitted))
    return splitted

def map_to_int_list(input: list[str]) -> list[int]:
    return list(map(lambda x : int(x),input))
