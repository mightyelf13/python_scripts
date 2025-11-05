from collections import namedtuple
from typing import List

# Use named tuple to improve readability of the code
Item = namedtuple("Item", "length, weight")

def support(bridge: Item, wagons: List[Item]) -> int:
    # Check if any wagon's length is greater than the length of the bridge
    if any(wagon.length > bridge.length for wagon in wagons):
        return -1

    # Deal with boundary cases
    if not bridge.length or not wagons:
        return -1

    # initialise the total length of wagons that are completely on the bridge 
    length = 0
    # .... and the total weight of wagons that touch the bridge
    load = wagons[0].weight

    # Some more boundary cases
    if load > bridge.weight:
        return 1
    if len(wagons) == 1:
        return -1

    load += wagons[1].weight
    if load > bridge.weight:
        return 2

    start = 1
    for end in range(1, len(wagons) - 1):
        while length + wagons[end].length >= bridge.length:
            load -= wagons[start - 1].weight
            length -= wagons[start].length
            start += 1

        length += wagons[end].length
        load += wagons[end + 1].weight
        if load > bridge.weight:
            return end + 2
    
    return -1

def read_words_until_empty_line():
    try:
        while True:
            line = input()
            yield from line.split()
    except EOFError:
        pass

def words_to_items(words):
    it = map(int, words)
    for length in it:
        yield Item(length, next(it))

if __name__ == "__main__":
    bridge, *wagons = words_to_items(read_words_until_empty_line())
    print(support(bridge, wagons))
