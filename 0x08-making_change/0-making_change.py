king Change interview task """


def makeChange(coins, total):
    """
        determine the fewest number of
        coins needed to meet a given amount total
    """

    if total <= 0:
        return 0

    for i in range(len(coins)):
        count = 0
        amount = 0
        for coin in reversed(sorted(coins[i:])):
            while amount + coin <= total:
                amount += coin
                count += 1
            if amount == total:
                return count

    return -1
