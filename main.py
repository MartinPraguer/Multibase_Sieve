import math
import time


# Convert number to custom base with letters (10 -> A, 11 -> B, etc.)
def to_base_with_letters(n, base):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        remainder = n % base
        digits.append(chr(ord('A') + remainder - 10) if remainder >= 10 else str(remainder))
        n //= base
    return ''.join(reversed(digits))


# Custom sieve using base conversions with operation counter
def sieve_fixed_with_letters_with_ops(limit):
    numbers = list(range(2, limit + 1))
    max_base = int(math.sqrt(limit))
    logs = []
    operation_count = 0

    for base in range(2, max_base + 1):
        filtered = []
        zero_ended = []
        removed = []
        log_entry = {
            "base": base,
            "removed": [],
            "kept_zero_end": None,
            "still_has_23": 23 in numbers
        }

        for num in numbers:
            base_repr = to_base_with_letters(num, base)
            operation_count += 1
            if base_repr.endswith('0'):
                zero_ended.append((num, base_repr))
            else:
                filtered.append(num)

        if zero_ended:
            kept = zero_ended[0]
            filtered.append(kept[0])
            operation_count += 1
            removed = zero_ended[1:]
        else:
            removed = []

        log_entry["removed"] = removed
        log_entry["kept_zero_end"] = zero_ended[0] if zero_ended else None
        logs.append(log_entry)
        numbers = sorted(filtered)
        operation_count += len(numbers)

    return numbers, logs, operation_count


# Classic Sieve of Eratosthenes with operation counter
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


# Compare both methods and print stats
def compare_methods_with_ops(limit):
    print(f"\n📊 Comparing methods for limit: {limit:,}".replace(",", "."))

    start1 = time.perf_counter()
    result_custom, _, ops_custom = sieve_fixed_with_letters_with_ops(limit)
    duration1 = time.perf_counter() - start1

    start2 = time.perf_counter()
    result_erat, ops_erat = sieve_eratosthenes(limit)
    duration2 = time.perf_counter() - start2

    print("\n=== 🧮 Custom Multibase Sieve ===")
    print(f"Remaining numbers: {len(result_custom):,}".replace(",", "."))
    print(f"Execution time: {duration1:.6f} seconds")
    print(f"Operations: {ops_custom:,}".replace(",", "."))

    print("\n=== ⚙️ Sieve of Eratosthenes ===")
    print(f"Remaining numbers: {len(result_erat):,}".replace(",", "."))
    print(f"Execution time: {duration2:.6f} seconds")
    print(f"Operations: {ops_erat:,}".replace(",", "."))

    # Speed comparison
    if duration2 > 0:
        ratio = duration1 / duration2
        print(f"\n⏱ Eratosthenes sieve is approximately {ratio:.1f}× faster")
    else:
        print("\n⏱ Eratosthenes sieve is too fast to compare reliably.")


if __name__ == "__main__":
    for test_limit in [100, 1_000, 10_000, 100_000]:
        compare_methods_with_ops(test_limit)


