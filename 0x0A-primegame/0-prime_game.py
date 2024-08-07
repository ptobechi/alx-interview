#!/usr/bin/python3
"""
Module for determining the winner of the Prime Game.
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    
    Args:
        x (int): The number of rounds.
        nums (list): List of integers for each round.
    
    Returns:
        str: The name of the player that won the most rounds.
        If the winner cannot be determined, return None.
    """
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False
    
    primes = [i for i in range(max_num + 1) if sieve[i]]
    
    def count_prime_moves(n):
        """Count the number of moves in a game with n elements."""
        taken = set()
        moves = 0
        for prime in primes:
            if prime > n:
                break
            if prime not in taken:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    taken.add(multiple)
        return moves
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if count_prime_moves(n) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
