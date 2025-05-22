# String Pattern Matching Program
This program implements a naive pattern matching algorithm to find occurrences of a pattern within text. The naive approach works by checking each possible starting position in the text and comparing the pattern character by character.
## Core Functionality
The `naive_pattern_matching` function:
- Takes two string inputs: a pattern to search for and a text to search within
- Systematically compares the pattern against each possible position in the text
- Returns the total count of pattern occurrences found

## Algorithm Details
The implementation uses a brute-force approach with two nested loops:
1. The outer loop iterates through each potential starting position in the text
2. The inner loop compares each character of the pattern with the corresponding character in the text
3. If all characters match, an occurrence is counted

While simple to implement, this approach has O(n*m) time complexity where n is the text length and m is the pattern length, making it less efficient for very large inputs compared to more advanced algorithms.
