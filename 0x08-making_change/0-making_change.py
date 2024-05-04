#!/usr/bin/python3
"""
Making Change - Minimum number of coins to make a sum
"""


def makeChange(coins, total):
    """
    Make-change function implementation
    """
    coins = sorted(coins)
    coin_count = 0
    idx = len(coins) - 1

    if total == 0:
        return 0
    if total < 0 or len(coins) == 0:
        return -1
    
    if coins[idx] <= total:
        new_total = total - coins[idx]
        coin_count += 1
        if coins[idx] <= new_total:
            result = makeChange(coins, new_total)
        if coins[idx] > new_total and total > 0:
            result = makeChange(coins[:idx], new_total)
        if result < 0:
            return -1
        coin_count += result
        return coin_count
    else:
        result = makeChange(coins[:idx], total)
        if result < 0:
            return -1
        coin_count += result
        return coin_count
