#!/usr/bin/python3
""" Prime game solution implementation """

def isWinner(x, nums):
    """Checks for the winner"""
    if x <= 0 or not nums:
        return None
    max_number = max(nums)

    filter_sort = [True for _ in range(max(max_number + 1, 2))]
    for i in range(2, int(pow(max_number, 0.5)) + 1):
        if not filter_sort[i]:
            continue
        for j in range(i * i, max_number + 1, i):
            filter_sort[j] = False
    filter_sort[0] = filter_sort[1] = False
    a = 0
    for b in range(len(filter_sort)):
        if filter_sort[b]:
            a += 1
        filter_sort[b] = a
    player_1 = 0
    for num in nums:
        player_1 += filter_sort[num] % 2 == 1
    if player_1 * 2 == len(nums):
        return None
    if player_1 * 2 > len(nums):
        return "Maria"
    return "Ben"