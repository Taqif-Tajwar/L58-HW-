def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_two_digit_primes():
    """Finds and returns all prime numbers having 2 digits (from 10 to 99)."""
    primes = []
    for number in range(10, 100):
        if is_prime(number):
            primes.append(number)
    return primes


# --- Sample Test Execution ---
if __name__ == "__main__":
    two_digit_primes = find_two_digit_primes()

    print("Execution Results:")
    print("-" * 30)
    print(f"Total 2-digit primes found: {len(two_digit_primes)}")
    print(f"List of 2-digit primes:\n{two_digit_primes}")
