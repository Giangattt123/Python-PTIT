p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
is_prime = [True] * (1e7 + 1)
is_prime[0] = is_prime[1] = False
def sieve_of_eratosthenes(limit):
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [num for num in range(limit + 1) if is_prime[num]]


def count_numbers(L, R, N):
    primes = sieve_of_eratosthenes(N)

    def count_divisible_up_to(limit):
        result = 0
        for num in range(1, limit + 1):
            divisible = any(num % prime == 0 for prime in primes)
            result += divisible
        return result

    count_up_to_R = count_divisible_up_to(R)
    count_up_to_L_minus_1 = count_divisible_up_to(L - 1)
    result = R - L + 1 - (count_up_to_R - count_up_to_L_minus_1)

    return result


def main():
    while True:
        L, R = map(int, input().split())
        if L == -1:
            break
        N = int(input())
        result = count_numbers(L, R, N)
        print(result)


if __name__ == "__main__":
    main()
