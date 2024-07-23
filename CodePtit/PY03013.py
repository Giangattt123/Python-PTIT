## ĐẾM CHỮ SỐ
#
# def count_digits(A, B):
#     frequency = [0] * 10
#     for num in range(A, B + 1):
#         for digit in str(num):
#             frequency[int(digit)] += 1
#     return frequency
#
# T = int(input())
#
# for _ in range(T):
#     A, B = map(int, input().split())
#     result = count_digits(A, B)
#     print(*result)

def count_digits(A, B):
    frequency = [0] * 10
    def count_digits_at_position(n, pos):
        return (n // (10 ** pos)) * (10 ** pos // 10) + min(max(n % (10 ** pos) - 10 ** pos + 1, 0), 10 ** pos // 10)

    for pos in range(len(str(B))):
        for digit in range(10):
            digit_count = count_digits_at_position(B, pos) - count_digits_at_position(A - 1, pos)
            frequency[digit] += digit_count

    return frequency

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    result = count_digits(A, B)
    print(*result)

