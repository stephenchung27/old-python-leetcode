'''
Given a range of routing numbers, determine what bank it belongs to.
Example:
(123400, 123500, BOA)
(12538, 12548, GCU)
'''

def bank_from_routing_number(banks, number):
    banks.sort()
    starts = [bank[0] for bank in banks]

    def binary_search(start, end, array, target):
        if start == end: return start

        mid = (start + end) // 2

        if target < array[mid]:
            return binary_search(start, mid - 1, array, target)
        elif target > array[mid]:
            # You want to preserve the mid in this case
            # You want to highest start lower than the target
            return binary_search(mid, end, array, target)
        else:
            return mid

    bank = banks[binary_search(0, len(banks), starts, number)][2]

    if bank[1] < target:
        return None
    else:
        return bank[2]

1 5 7 10