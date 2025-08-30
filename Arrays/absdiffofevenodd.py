"""✅ Problem: Difference Between Sum of Even and Odd Numbers
🗓️ Date Solved: 29-08-2025
🧠 Approach: Iteration + Simple Arithmetic
First input n → size of array, followed by n numbers.
Traversed through each number in the array.
Maintained two sums:
even_sum → sum of all even numbers
odd_sum → sum of all odd numbers
Final answer = abs(even_sum - odd_sum) (absolute difference).
💡 Key Points:
Straightforward iteration over array.
Used modulo % operator to check even/odd.
abs() ensures result is always non-negative.
⏱ Complexity:
Time: O(n) — traverses the array once.
Space: O(1) — only a few variables used."""

from sys import stdin
def main():
    arr = list(map(int, input().split()))
    n = arr[0]
    nums = arr[1:]

    even_sum = 0
    odd_sum = 0

    for num in nums:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    print(abs(even_sum - odd_sum))

if __name__ == "__main__":
    main()
