import timeit


def find_coins_greedy(coins, target):
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        if coin <= target:
            result[coin] = result.get(coin, 0) + target // coin
            target = target % coin
    return result


def find_coins_dynamic(coins, target):
    num_coins = [0] + [float('inf')] * target
    max_coin = [0] * (target + 1)
    for s in range(1, target + 1):
        for coin in coins:
            if s >= coin and num_coins[s - coin] + 1 < num_coins[s]:
                num_coins[s] = min(num_coins[s], num_coins[s - coin] + 1)
                max_coin[s] = coin

    result = {}
    test_sum = target
    while test_sum > 0:
        coin = max_coin[test_sum]
        result[coin] = result.get(coin, 0) + 1
        test_sum -= coin

    return result


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    runs = 100

    search_sum_small = 113
    search_sum_large = 113113

    greedy_time_small = timeit.timeit(lambda: find_coins_greedy(coins, search_sum_small), number=runs) / runs
    dynamic_time_small = timeit.timeit(lambda: find_coins_dynamic(coins, search_sum_small), number=runs) / runs
    greedy_time_large = timeit.timeit(lambda: find_coins_greedy(coins, search_sum_large), number=runs) / runs
    dynamic_time_large = timeit.timeit(lambda: find_coins_dynamic(coins, search_sum_large), number=runs) / runs

    print(f"{'Жадібний алгоритм (' + str(search_sum_small) + '):': <35} {'{}'.format(find_coins_greedy(coins, search_sum_small)): <35} заняло {greedy_time_small * 1000000} мікросекунд")
    print(f"{'Динамічний алгоритм (' + str(search_sum_small) + '):': <35} {'{}'.format(find_coins_dynamic(coins, search_sum_small)): <35} заняло {dynamic_time_small * 1000000} мікросекунд")
    print()
    print(f"{'Жадібний алгоритм (' + str(search_sum_large) + '):': <35} {'{}'.format(find_coins_greedy(coins, search_sum_large)): <35} заняло {greedy_time_large * 1000000} мікросекунд")
    print(f"{'Динамічний алгоритм (' + str(search_sum_large) + '):': <35} {'{}'.format(find_coins_dynamic(coins, search_sum_large)): <35} заняло {dynamic_time_large * 1000000} мікросекунд")
