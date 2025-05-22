def naive_pattern_matching(pattern, text):
    """
    A function that implements the naive string pattern matching algorithm. It searches
    for occurrences of a given pattern within a given text and returns the count of
    occurrences. The method performs this task by checking each possible alignment of
    the pattern with the text to determine if all characters match.

    :param pattern: The sub-string pattern that needs to be searched in the text.
    :param text: The full text within which the pattern is searched.
    :return: The total count of occurrences of the pattern found within the text.
    """
    pattern_length = len(pattern)
    text_length = len(text)
    occurrences = 0
    #add double for loop here to serch for pattern in text
    for i in range(text_length - pattern_length + 1):
        pattern_match = True
        for j in range(pattern_length):
          if (pattern[j] != text[i+j]):
            pattern_match = False
            break
        if (pattern_match):
          occurrences += 1
    return occurrences

pattern = 1000*'A'
text = 100000*'A'
print(naive_pattern_matching(pattern, text))


