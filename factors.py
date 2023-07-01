#!/usr/bin/env python3

import sys


def factorize(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append((i, n // i))
            n //= i
    if n > 1:
        factors.append((n, 1))
    return factors


def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            for line in file:
                n = int(line)
                factor_pairs = factorize(n)
                for p, q in factor_pairs:
                    print(f"{n}={p}*{q}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError:
        print("Invalid number in the file")


if __name__ == "__main__":
    main()
