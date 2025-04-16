import math
import time


# Optimized sieve without text conversion
import math

def multibase_sieve(limit):
    numbers = list(range(2, limit + 1))
    max_base = int(math.sqrt(limit))
    operation_count = 0
    used_bases = []

    for base in range(2, max_base + 1):
        if any(base % b == 0 for b in used_bases):
            continue

        used_bases.append(base)
        filtered = []
        zero_ended = []

        for num in numbers:
            operation_count += 1
            if num % base == 0:
                zero_ended.append(num)
            else:
                filtered.append(num)

        if zero_ended:
            filtered.append(zero_ended[0])  # keep the first occurrence
            operation_count += 1

        numbers = sorted(filtered)
        operation_count += len(numbers)

    return numbers, operation_count


# Classical Sieve of Eratosthenes
def sieve_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    operation_count = 0

    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                if sieve[multiple]:
                    sieve[multiple] = False
                    operation_count += 1

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes, operation_count


# Performance comparison between both methods
def compare_methods(limit):
    print(f"\n📊 Comparison for limit: {limit:,}".replace(",", "."))

    # Custom sieve (modulo filtering)
    start1 = time.perf_counter()
    result_custom, ops_custom = multibase_sieve(limit)
    duration1 = time.perf_counter() - start1

    # Classical Eratosthenes sieve
    start2 = time.perf_counter()
    result_erat, ops_erat = sieve_eratosthenes(limit)
    duration2 = time.perf_counter() - start2

    print("\n=== 🧮 Multibase Sieve ===")
    print(f"Survivors: {len(result_custom):,}".replace(",", "."))
    print(f"Execution time: {duration1:.6f} seconds")
    print(f"Operations: {ops_custom:,}".replace(",", "."))

    print("\n=== ⚙️ Eratosthenes Sieve ===")
    print(f"Survivors: {len(result_erat):,}".replace(",", "."))
    print(f"Execution time: {duration2:.6f} seconds")
    print(f"Operations: {ops_erat:,}".replace(",", "."))

    # Speed ratio
    if duration2 > 0:
        ratio = duration1 / duration2
        print(f"\n⏱ Eratosthenes sieve is approximately {ratio:.1f}× faster")
    else:
        print("\n⏱ Eratosthenes sieve is too fast for accurate comparison.")


if __name__ == "__main__":
    # Test with multiple limits
    for test_limit in [
        1_000,
        10_000,
        100_000,
        1_000_000,
        10_000_000,
        100_000_000,
        1_000_000_000,
    ]:
        compare_methods(test_limit)
