#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Activity 2.1: Recurrence Experimentation and Analysis
Course: CS 5329 – Algorithm Design and Analysis

This script compares the performance of a naive recursive Fibonacci implementation
with optimized dynamic programming versions (memoization and bottom-up).
"""

import time
import sys

# Increase recursion limit for larger memoization tests (use with caution)
sys.setrecursionlimit(2000)

# =============================================================================
# APPROACH 1: Naive Recursive (Exponential Time Complexity)
# =============================================================================
def fib_recursive(n):
    """
    Calculates the nth Fibonacci number using a naive recursive approach.
    
    Time Complexity: O(2^n) - Exponential
    Space Complexity: O(n) - Due to call stack depth
    
    WARNING: This function is extremely slow for n > 35.
    """
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# =============================================================================
# APPROACH 2: Dynamic Programming - Memoization (Top-Down)
# =============================================================================
# Dictionary used to store previously computed values for memoization
fib_memo = {}

def fib_dp_memo(n):
    """
    Calculates the nth Fibonacci number using top-down dynamic programming
    (memoization).
    
    Time Complexity: O(n) - Linear
    Space Complexity: O(n) - For the memoization dictionary and call stack
    
    This approach uses recursion but stores computed values in a dictionary
    to avoid redundant calculations.
    """
    # Check if the value is already in our cache
    if n in fib_memo:
        return fib_memo[n]
    
    # Base cases
    if n < 2:
        result = n
    else:
        # Recursive step
        result = fib_dp_memo(n - 1) + fib_dp_memo(n - 2)
    
    # Cache the result before returning
    fib_memo[n] = result
    return result


# =============================================================================
# APPROACH 3: Dynamic Programming - Tabulation (Bottom-Up)
# =============================================================================
def fib_dp_bottomup(n):
    """
    Calculates the nth Fibonacci number using bottom-up dynamic programming
    (tabulation).
    
    Time Complexity: O(n) - Linear
    Space Complexity: O(1) - Constant (only stores last two values)
    
    This is the most efficient approach as it avoids recursion overhead
    and uses minimal memory.
    """
    if n < 2:
        return n
    
    # We only need to keep track of the last two Fibonacci numbers
    prev2 = 0  # fib(0)
    prev1 = 1  # fib(1)
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


# =============================================================================
# Wrapper function for the assignment (uses memoization by default)
# =============================================================================
def fib_dp(n):
    """
    Wrapper function that implements dynamic programming for Fibonacci.
    Uses memoization (top-down) approach.
    
    For very large n (> 500), consider using fib_dp_bottomup() instead
    to avoid Python's recursion limit.
    """
    global fib_memo
    # Clear the memo for fresh calculation
    fib_memo = {}
    return fib_dp_memo(n)


# =============================================================================
# Main Execution
# =============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("Activity 2.1: Fibonacci - Recursive vs Dynamic Programming")
    print("=" * 70)
    
    # --- Required Test Values ---
    print("\n--- Part 1: Comparing Recursive vs. Dynamic Programming ---\n")
    test_values = [10, 20, 30, 35]
    
    for n in test_values:
        # Clear the memoization cache for a fair DP test each time
        fib_memo = {}
        
        # --- Naive Recursive ---
        start_rec = time.time()
        res1 = fib_recursive(n)
        t1 = time.time() - start_rec
        
        # --- Dynamic Programming (Memoization) ---
        start_dp = time.time()
        res2 = fib_dp_memo(n)
        t2 = time.time() - start_dp
        
        print(
            f"n={n}: fib_recursive -> {res1} (time {t1:.4f}s), "
            f"fib_dp -> {res2} (time {t2:.6f}s)"
        )
    
    # --- Additional Large Values for DP Only ---
    print("\n--- Part 2: Testing Dynamic Programming with Larger Values ---\n")
    print("(Using bottom-up approach to avoid recursion limit issues)\n")
    
    large_test_values = [50, 100, 500, 1000]
    
    for n in large_test_values:
        start_dp_large = time.time()
        res_large = fib_dp_bottomup(n)
        t_large = time.time() - start_dp_large
        
        # Format the result for readability
        result_str = str(res_large)
        if len(result_str) > 50:
            result_str = f"{result_str[:25]}...({len(result_str)} digits)"
        
        print(f"n={n}: fib_dp -> {result_str} (time {t_large:.6f}s)")
    
    print("\n" + "=" * 70)
    print("Experiment Complete!")
    print("=" * 70)
