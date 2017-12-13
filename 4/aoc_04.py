#!/usr/bin/env python

from collections import Counter


def only_unique_words(passphrase):
    words = passphrase.strip().split(" ")
    counter = Counter(words)
    return len(counter.most_common()) == len(words)

def anagrams_restricted(passphrase):
    words = passphrase.strip().split(" ")
    counter = Counter("".join(sorted(word)) for word in words)
    return len(counter.most_common()) == len(words)


def count_valid(file_content, validator):
    valid_lines = list(filter(validator, file_content.strip().split("\n")))
    return len(valid_lines)


# Tests
assert only_unique_words("aa bb cc dd ee") == True
assert only_unique_words("aa bb cc dd aa") == False
assert only_unique_words("aa bb cc dd aaa") == True

multiline = "aa bb cc dd ee\naa bb cc dd aa\naa bb cc dd aaa"
assert count_valid(multiline, validator=only_unique_words) == 2


assert anagrams_restricted("abcde fghij") == True
assert anagrams_restricted("abcde xyz ecdab") == False
assert anagrams_restricted("a ab abc abd abf abj") == True
assert anagrams_restricted("iiii oiii ooii oooi oooo") == True
assert anagrams_restricted("oiii ioii iioi iiio") == False


# Solution
with open("input.txt") as f:
    task_input = f.read()

print("Part 1 answer is {}".format(count_valid(task_input, validator=only_unique_words)))
print("Part 2 answer is {}".format(count_valid(task_input, validator=anagrams_restricted)))
